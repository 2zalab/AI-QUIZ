import { createClient, type SupabaseClient } from "@supabase/supabase-js";

import { GAMES, GAME_BY_SLUG, clampQuestionsPerSession } from "../config";
import { computeScore, generateSessionCode, sanitizeName } from "../scoring";
import type {
  AnswerResult, Difficulty, Game, LeaderboardEntry, Letter, PublicQuestion, SessionState, Stats,
} from "../types";
import type { GameSettings, Store } from "./index";
import { pickSessionQuestions } from "./questions";

interface QuestionRow {
  id: string;
  difficulty: Difficulty;
  question: string;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  correct_answer: Letter;
  points: number;
  time_limit: number;
  explanation: string;
}

interface GameRow {
  id: string;
  slug: string;
  name: string;
  description: string;
  emoji: string;
  color: string;
  is_active: boolean;
  questions_per_session: number;
}

/** Convertit une ligne de la table games en categorie exploitable par l'interface. */
function toGame(row: GameRow, questionCount: number): Game {
  const fallback = new Map(GAMES.map((game) => [game.slug, game]));
  const base = fallback.get(row.slug);
  return {
    slug: row.slug,
    name: row.name || base?.name || row.slug,
    description: row.description || base?.description || "",
    emoji: row.emoji || base?.emoji || "",
    color: row.color || base?.color || "#2f80ed",
    isActive: row.is_active,
    questionsPerSession: row.questions_per_session,
    questionCount,
  };
}

/**
 * Client Supabase avec la cle de service. A n'utiliser QUE cote serveur :
 * elle contourne les politiques RLS et donne acces aux bonnes reponses.
 */
function serviceClient(): SupabaseClient {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { persistSession: false, autoRefreshToken: false } },
  );
}

function toPublic(row: QuestionRow, index: number, total: number, servedAt: number): PublicQuestion {
  return {
    id: row.id,
    index,
    total,
    difficulty: row.difficulty,
    question: row.question,
    options: { A: row.option_a, B: row.option_b, C: row.option_c, D: row.option_d },
    points: row.points,
    timeLimit: row.time_limit,
    deadlineAt: servedAt + row.time_limit * 1000,
  };
}

export function createSupabaseStore(): Store {
  const db = serviceClient();

  /** Categorie ouverte aux joueurs, avec son nombre de questions par partie. */
  async function openGame(slug: string): Promise<{ id: string; perSession: number }> {
    const { data, error } = await db
      .from("games")
      .select("id, is_active, questions_per_session")
      .eq("slug", slug)
      .maybeSingle();
    const row = data as
      | { id: string; is_active: boolean; questions_per_session: number }
      | null;
    if (error || !row) throw new Error(`Categorie introuvable : ${slug}`);
    if (!row.is_active) throw new Error("Ce defi n'est plus propose. Choisissez-en un autre.");
    return {
      id: row.id,
      perSession: row.questions_per_session ?? GAME_BY_SLUG.get(slug)?.questionsPerSession ?? 10,
    };
  }

  async function playerByCode(sessionCode: string) {
    const { data } = await db
      .from("players")
      .select("id, name, score, correct_count, answered_count, status, started_at, games(slug)")
      .eq("session_code", sessionCode)
      .maybeSingle();
    return data as
      | {
          id: string; name: string; score: number; correct_count: number;
          answered_count: number; status: "waiting" | "playing" | "finished";
          started_at: string; games: { slug: string } | { slug: string }[];
        }
      | null;
  }

  function slugOf(player: { games: { slug: string } | { slug: string }[] }): string {
    return Array.isArray(player.games) ? player.games[0].slug : player.games.slug;
  }

  async function positionOf(playerId: string): Promise<{ position: number; total: number }> {
    const { data } = await db.from("leaderboard").select("id, rank").order("rank");
    const rows = (data ?? []) as { id: string; rank: number }[];
    const found = rows.find((row) => row.id === playerId);
    return { position: found?.rank ?? rows.length + 1, total: rows.length };
  }

  /** Renvoie la prochaine question non repondue d'une partie. */
  async function nextPending(playerId: string) {
    const { data } = await db
      .from("player_questions")
      .select("id, question_id, order_number, served_at, answered")
      .eq("player_id", playerId)
      .order("order_number");
    const rows = (data ?? []) as {
      id: string; question_id: string; order_number: number;
      served_at: string | null; answered: boolean;
    }[];
    const pending = rows.find((row) => !row.answered) ?? null;
    return { rows, pending };
  }

  async function questionById(id: string): Promise<QuestionRow | null> {
    const { data } = await db
      .from("questions")
      .select("id, difficulty, question, option_a, option_b, option_c, option_d, correct_answer, points, time_limit, explanation")
      .eq("id", id)
      .maybeSingle();
    return (data as QuestionRow) ?? null;
  }

  return {
    async listGames(): Promise<Game[]> {
      const { data } = await db
        .from("games")
        .select("id, slug, name, description, emoji, color, is_active, questions_per_session")
        .order("slug");
      const rows = (data ?? []) as GameRow[];

      const counts = new Map<string, number>();
      for (const row of rows) {
        const { count } = await db
          .from("questions")
          .select("id", { count: "exact", head: true })
          .eq("game_id", row.id);
        counts.set(row.slug, count ?? 0);
      }
      return rows.map((row) => toGame(row, counts.get(row.slug) ?? 0));
    },

    async updateGame(slug, settings): Promise<Game> {
      const { data: existing } = await db
        .from("games")
        .select("id")
        .eq("slug", slug)
        .maybeSingle();
      if (!existing) throw new Error(`Categorie introuvable : ${slug}`);
      const { count: available } = await db
        .from("questions")
        .select("id", { count: "exact", head: true })
        .eq("game_id", (existing as { id: string }).id);

      const patch: Record<string, unknown> = {};
      if (settings.questionsPerSession !== undefined) {
        patch.questions_per_session = clampQuestionsPerSession(
          settings.questionsPerSession,
          available ?? 0,
        );
      }
      if (settings.isActive !== undefined) patch.is_active = settings.isActive;

      const query = Object.keys(patch).length
        ? db.from("games").update(patch).eq("slug", slug)
        : db.from("games").select().eq("slug", slug);

      const { data, error } = await query
        .select("id, slug, name, description, emoji, color, is_active, questions_per_session")
        .single();
      if (error || !data) {
        throw new Error(`Reglage impossible pour ${slug}. ${error?.message ?? ""}`.trim());
      }

      return toGame(data as GameRow, available ?? 0);
    },

    async createSession(rawName, gameSlug) {
      const name = sanitizeName(rawName);
      if (!name) throw new Error("Le nom du joueur est obligatoire.");
      const { id: gameId, perSession } = await openGame(gameSlug);

      const { data: pool } = await db
        .from("questions")
        .select("id, difficulty")
        .eq("game_id", gameId);
      const rows = (pool ?? []) as { id: string; difficulty: Difficulty }[];
      if (rows.length === 0) {
        // Cas typique d'un projet Supabase dont le schema est en place mais dont
        // la banque n'a jamais ete alimentee.
        console.error(
          `[MIT] La table questions est vide pour la categorie "${gameSlug}". ` +
            "Lancez `npm run db:import` avec les variables Supabase du projet.",
        );
        throw new Error(
          "Aucune question n'a encore ete importee pour ce defi. L'organisateur doit lancer l'import des questions.",
        );
      }

      let sessionCode = generateSessionCode();
      let inserted: { id: string } | null = null;
      let lastError: string | null = null;

      for (let attempt = 0; attempt < 5 && !inserted; attempt += 1) {
        const { data, error } = await db
          .from("players")
          .insert({ name, game_id: gameId, session_code: sessionCode })
          .select("id")
          .single();
        if (!error) {
          inserted = data as { id: string };
          break;
        }
        lastError = error.message;
        // 23505 = collision sur session_code : on retente avec un autre code.
        // Toute autre erreur est definitive, inutile d'insister.
        if (error.code !== "23505") break;
        sessionCode = generateSessionCode();
      }
      if (!inserted) {
        throw new Error(`Impossible de creer la session de jeu. ${lastError ?? ""}`.trim());
      }

      const selection = pickSessionQuestions(rows, clampQuestionsPerSession(perSession, rows.length));
      const { error: linkError } = await db.from("player_questions").insert(
        selection.map((question, index) => ({
          player_id: inserted!.id,
          question_id: question.id,
          order_number: index + 1,
        })),
      );
      if (linkError) {
        // La partie serait injouable sans ses questions : on retire le joueur.
        await db.from("players").delete().eq("id", inserted.id);
        throw new Error(`Impossible de preparer les questions de la partie. ${linkError.message}`);
      }

      return { sessionCode };
    },

    async getState(sessionCode): Promise<SessionState | null> {
      const player = await playerByCode(sessionCode);
      if (!player) return null;
      const slug = slugOf(player);
      const game = GAME_BY_SLUG.get(slug) ?? GAMES[0];
      const { rows, pending } = await nextPending(player.id);
      const { position, total } = await positionOf(player.id);

      let question: PublicQuestion | null = null;
      if (pending && pending.served_at) {
        const row = await questionById(pending.question_id);
        if (row) {
          question = toPublic(row, pending.order_number, rows.length, Date.parse(pending.served_at));
        }
      }

      return {
        player: {
          name: player.name,
          gameSlug: slug,
          score: player.score,
          correctCount: player.correct_count,
          answeredCount: player.answered_count,
          status: player.status,
        },
        game,
        question,
        finished: !pending,
        position,
        totalPlayers: total,
      };
    },

    async serveQuestion(sessionCode) {
      const player = await playerByCode(sessionCode);
      if (!player) return null;
      const { rows, pending } = await nextPending(player.id);
      if (!pending) {
        await db
          .from("players")
          .update({ status: "finished", finished_at: new Date().toISOString() })
          .eq("id", player.id);
        return null;
      }
      const servedAt = new Date();
      await db.from("player_questions").update({ served_at: servedAt.toISOString() }).eq("id", pending.id);
      if (player.status === "waiting") {
        await db.from("players").update({ status: "playing" }).eq("id", player.id);
      }
      const row = await questionById(pending.question_id);
      if (!row) return null;
      return toPublic(row, pending.order_number, rows.length, servedAt.getTime());
    },

    async submitAnswer(sessionCode, questionId, answer): Promise<AnswerResult> {
      const player = await playerByCode(sessionCode);
      if (!player) throw new Error("Session introuvable.");
      const { rows, pending } = await nextPending(player.id);
      if (!pending) throw new Error("La partie est deja terminee.");
      if (pending.question_id !== questionId) throw new Error("Question hors sequence.");

      const question = await questionById(questionId);
      if (!question) throw new Error("Question introuvable.");

      const servedAt = pending.served_at ? Date.parse(pending.served_at) : Date.now();
      const answeredAt = Date.now();
      const isCorrect = answer === question.correct_answer;
      const { gained, speedBonus } = computeScore({
        basePoints: question.points,
        timeLimitSeconds: question.time_limit,
        servedAt,
        answeredAt,
        isCorrect,
      });

      await db.from("answers").upsert(
        {
          player_id: player.id,
          question_id: questionId,
          answer,
          is_correct: gained > 0,
          points: gained,
          speed_bonus: speedBonus,
          time_taken_ms: answeredAt - servedAt,
        },
        { onConflict: "player_id,question_id" },
      );
      await db.from("player_questions").update({ answered: true }).eq("id", pending.id);

      const answeredCount = player.answered_count + 1;
      const correctCount = player.correct_count + (gained > 0 ? 1 : 0);
      const finished = answeredCount >= rows.length;
      await db
        .from("players")
        .update({
          score: player.score + gained,
          answered_count: answeredCount,
          correct_count: correctCount,
          status: finished ? "finished" : "playing",
          finished_at: finished ? new Date().toISOString() : null,
        })
        .eq("id", player.id);

      const { position } = await positionOf(player.id);
      return {
        correct: gained > 0,
        correctAnswer: question.correct_answer,
        explanation: question.explanation,
        gained,
        speedBonus,
        score: player.score + gained,
        position,
        finished,
        correctCount,
        answeredCount,
        total: rows.length,
      };
    },

    async leaderboard({ gameSlug, limit = 20 } = {}): Promise<LeaderboardEntry[]> {
      let query = db
        .from("leaderboard")
        .select("name, game_slug, score, status, correct_count, answered_count, rank")
        .order("rank")
        .limit(limit);
      if (gameSlug) query = query.eq("game_slug", gameSlug);
      const { data } = await query;
      return ((data ?? []) as {
        name: string; game_slug: string; score: number;
        status: LeaderboardEntry["status"]; correct_count: number;
        answered_count: number; rank: number;
      }[]).map((row, index) => ({
        rank: gameSlug ? index + 1 : row.rank,
        name: row.name,
        gameSlug: row.game_slug,
        score: row.score,
        status: row.status,
        correctCount: row.correct_count,
        answeredCount: row.answered_count,
      }));
    },

    async stats(): Promise<Stats> {
      const { data } = await db.from("leaderboard").select("game_slug, score, status");
      const rows = (data ?? []) as { game_slug: string; score: number; status: string }[];
      const total = rows.length;
      return {
        totalPlayers: total,
        playing: rows.filter((row) => row.status === "playing").length,
        finished: rows.filter((row) => row.status === "finished").length,
        waiting: rows.filter((row) => row.status === "waiting").length,
        averageScore: total ? Math.round(rows.reduce((sum, row) => sum + row.score, 0) / total) : 0,
        byGame: GAMES.map((game) => ({
          slug: game.slug,
          name: game.name,
          emoji: game.emoji,
          players: rows.filter((row) => row.game_slug === game.slug).length,
        })),
      };
    },

    async reset() {
      await db.from("players").delete().neq("id", "00000000-0000-0000-0000-000000000000");
    },

    async version() {
      const { data } = await db
        .from("players")
        .select("score, answered_count")
        .order("score", { ascending: false })
        .limit(200);
      const rows = (data ?? []) as { score: number; answered_count: number }[];
      return rows.reduce((sum, row) => sum + row.score * 7 + row.answered_count, rows.length);
    },
  };
}
