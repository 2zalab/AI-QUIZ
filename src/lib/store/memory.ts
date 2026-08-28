import { GAMES, GAME_BY_SLUG } from "../config";
import { computeScore, generateSessionCode, sanitizeName } from "../scoring";
import type {
  AnswerResult, Game, LeaderboardEntry, Letter, Player, PublicQuestion, Question,
  SessionState, Stats,
} from "../types";
import type { Store } from "./index";
import { loadQuestionsFromCsv, pickSessionQuestions } from "./questions";

interface Session {
  player: Player;
  questions: Question[];
  cursor: number;
  servedAt: number | null;
}

interface MemoryState {
  sessions: Map<string, Session>;
  version: number;
}

/** Etat conserve sur l'objet global pour survivre au rechargement a chaud de Next.js. */
const globalRef = globalThis as unknown as { __iclanMemory?: MemoryState };
const state: MemoryState = globalRef.__iclanMemory ?? { sessions: new Map(), version: 0 };
globalRef.__iclanMemory = state;

function bump() {
  state.version += 1;
}

function rankOf(sessionCode: string): { position: number; total: number } {
  const sorted = [...state.sessions.values()].sort((a, b) => b.player.score - a.player.score);
  const index = sorted.findIndex((session) => session.player.sessionCode === sessionCode);
  return { position: index >= 0 ? index + 1 : sorted.length + 1, total: sorted.length };
}

function toPublic(question: Question, index: number, total: number, servedAt: number): PublicQuestion {
  return {
    id: question.id,
    index,
    total,
    difficulty: question.difficulty,
    question: question.question,
    options: question.options,
    points: question.points,
    timeLimit: question.timeLimit,
    deadlineAt: servedAt + question.timeLimit * 1000,
  };
}

export function createMemoryStore(): Store {
  return {
    mode: "memory",

    async listGames(): Promise<Game[]> {
      const pools = loadQuestionsFromCsv();
      return GAMES.map((game) => ({
        ...game,
        questionCount: pools.get(game.slug)?.length ?? 0,
      }));
    },

    async createSession(rawName, gameSlug) {
      const name = sanitizeName(rawName);
      if (!name) throw new Error("Le nom du joueur est obligatoire.");
      if (!GAME_BY_SLUG.has(gameSlug)) throw new Error("Categorie de jeu inconnue.");

      const pool = loadQuestionsFromCsv().get(gameSlug) ?? [];
      if (pool.length === 0) throw new Error("Aucune question disponible pour cette categorie.");

      let sessionCode = generateSessionCode();
      while (state.sessions.has(sessionCode)) sessionCode = generateSessionCode();

      state.sessions.set(sessionCode, {
        player: {
          id: sessionCode,
          name,
          gameSlug,
          sessionCode,
          score: 0,
          correctCount: 0,
          answeredCount: 0,
          status: "waiting",
          startedAt: Date.now(),
          finishedAt: null,
        },
        questions: pickSessionQuestions(pool),
        cursor: 0,
        servedAt: null,
      });
      bump();
      return { sessionCode };
    },

    async getState(sessionCode): Promise<SessionState | null> {
      const session = state.sessions.get(sessionCode);
      if (!session) return null;
      const game = GAME_BY_SLUG.get(session.player.gameSlug)!;
      const finished = session.cursor >= session.questions.length;
      const { position, total } = rankOf(sessionCode);

      let question: PublicQuestion | null = null;
      if (!finished && session.servedAt !== null) {
        question = toPublic(
          session.questions[session.cursor], session.cursor + 1,
          session.questions.length, session.servedAt,
        );
      }
      return {
        player: {
          name: session.player.name,
          gameSlug: session.player.gameSlug,
          score: session.player.score,
          correctCount: session.player.correctCount,
          answeredCount: session.player.answeredCount,
          status: session.player.status,
        },
        game,
        question,
        finished,
        position,
        totalPlayers: total,
      };
    },

    async serveQuestion(sessionCode) {
      const session = state.sessions.get(sessionCode);
      if (!session) return null;
      if (session.cursor >= session.questions.length) {
        if (session.player.status !== "finished") {
          session.player.status = "finished";
          session.player.finishedAt = Date.now();
          bump();
        }
        return null;
      }
      if (session.player.status === "waiting") session.player.status = "playing";
      session.servedAt = Date.now();
      bump();
      return toPublic(
        session.questions[session.cursor], session.cursor + 1,
        session.questions.length, session.servedAt,
      );
    },

    async submitAnswer(sessionCode, questionId, answer): Promise<AnswerResult> {
      const session = state.sessions.get(sessionCode);
      if (!session) throw new Error("Session introuvable.");
      const current = session.questions[session.cursor];
      if (!current) throw new Error("La partie est deja terminee.");
      if (current.id !== questionId) throw new Error("Question hors sequence.");

      const isCorrect = answer === current.correctAnswer;
      const { gained, speedBonus } = computeScore({
        basePoints: current.points,
        timeLimitSeconds: current.timeLimit,
        servedAt: session.servedAt ?? Date.now(),
        answeredAt: Date.now(),
        isCorrect,
      });

      session.player.score += gained;
      session.player.answeredCount += 1;
      if (gained > 0) session.player.correctCount += 1;
      session.cursor += 1;
      session.servedAt = null;

      const finished = session.cursor >= session.questions.length;
      if (finished) {
        session.player.status = "finished";
        session.player.finishedAt = Date.now();
      }
      bump();

      const { position } = rankOf(sessionCode);
      return {
        correct: gained > 0,
        correctAnswer: current.correctAnswer,
        explanation: current.explanation,
        gained,
        speedBonus,
        score: session.player.score,
        position,
        finished,
        correctCount: session.player.correctCount,
        answeredCount: session.player.answeredCount,
        total: session.questions.length,
      };
    },

    async leaderboard({ gameSlug, limit = 20 } = {}): Promise<LeaderboardEntry[]> {
      return [...state.sessions.values()]
        .map((session) => session.player)
        .filter((player) => !gameSlug || player.gameSlug === gameSlug)
        .sort((a, b) => b.score - a.score || a.startedAt - b.startedAt)
        .slice(0, limit)
        .map((player, index) => ({
          rank: index + 1,
          name: player.name,
          gameSlug: player.gameSlug,
          score: player.score,
          status: player.status,
          correctCount: player.correctCount,
          answeredCount: player.answeredCount,
        }));
    },

    async stats(): Promise<Stats> {
      const players = [...state.sessions.values()].map((session) => session.player);
      const total = players.length;
      return {
        totalPlayers: total,
        playing: players.filter((p) => p.status === "playing").length,
        finished: players.filter((p) => p.status === "finished").length,
        waiting: players.filter((p) => p.status === "waiting").length,
        averageScore: total ? Math.round(players.reduce((sum, p) => sum + p.score, 0) / total) : 0,
        byGame: GAMES.map((game) => ({
          slug: game.slug,
          name: game.name,
          emoji: game.emoji,
          players: players.filter((p) => p.gameSlug === game.slug).length,
        })),
      };
    },

    async reset() {
      state.sessions.clear();
      bump();
    },

    async version() {
      return state.version;
    },
  };
}
