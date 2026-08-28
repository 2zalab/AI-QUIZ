import { readFileSync } from "node:fs";
import path from "node:path";
import { parse } from "csv-parse/sync";

import { DIFFICULTY_PLAN, QUESTIONS_PER_SESSION } from "../config";
import type { Difficulty, Letter, Question } from "../types";

const CSV_BY_SLUG: Record<string, string> = {
  entrepreneuriat: "questions_entrepreneuriat.csv",
  cameroun: "questions_cameroun.csv",
  "innovation-ia": "questions_innovation_ia.csv",
  mixte: "questions_mixte.csv",
};

interface CsvRow {
  id: string;
  category_slug: string;
  difficulty: Difficulty;
  question: string;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  correct_answer: Letter;
  points: string;
  time_limit: string;
  explanation: string;
  tags: string;
}

let cache: Map<string, Question[]> | null = null;

/** Charge les CSV du dossier data/ une seule fois par processus. */
export function loadQuestionsFromCsv(dataDir = path.join(process.cwd(), "data")): Map<string, Question[]> {
  if (cache) return cache;
  const loaded = new Map<string, Question[]>();

  for (const [slug, file] of Object.entries(CSV_BY_SLUG)) {
    const fullPath = path.join(dataDir, file);
    let raw: string;
    try {
      raw = readFileSync(fullPath, "utf-8");
    } catch (error) {
      // Sans ce journal, une banque vide passerait totalement inapercue.
      console.error(
        `[iCLAN] Fichier de questions illisible : ${fullPath}. ` +
          "En mode demonstration, verifiez que le dossier data/ est bien deploye " +
          `(${error instanceof Error ? error.message : String(error)}).`,
      );
      loaded.set(slug, []);
      continue;
    }
    const rows = parse(raw, { columns: true, skip_empty_lines: true, bom: true }) as CsvRow[];
    loaded.set(
      slug,
      rows.map((row) => ({
        id: row.id,
        gameSlug: slug,
        difficulty: row.difficulty,
        question: row.question,
        options: { A: row.option_a, B: row.option_b, C: row.option_c, D: row.option_d },
        correctAnswer: row.correct_answer,
        points: Number(row.points),
        timeLimit: Number(row.time_limit),
        explanation: row.explanation,
        tags: row.tags,
      })),
    );
  }

  cache = loaded;
  return cache;
}

function shuffle<T>(items: T[]): T[] {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

/**
 * Tire au sort les questions d'une partie en respectant la repartition de
 * difficulte prevue, puis complete avec le reste du vivier si besoin.
 */
export function pickSessionQuestions<T extends { difficulty: Difficulty }>(
  pool: T[],
  count = QUESTIONS_PER_SESSION,
): T[] {
  const byDifficulty = new Map<string, T[]>();
  for (const question of pool) {
    const bucket = byDifficulty.get(question.difficulty) ?? [];
    bucket.push(question);
    byDifficulty.set(question.difficulty, bucket);
  }

  const chosen: T[] = [];
  const used = new Set<T>();
  const scale = count / Object.values(DIFFICULTY_PLAN).reduce((a, b) => a + b, 0);

  for (const [difficulty, planned] of Object.entries(DIFFICULTY_PLAN)) {
    const target = Math.round(planned * scale);
    const bucket = shuffle(byDifficulty.get(difficulty) ?? []);
    for (const question of bucket.slice(0, target)) {
      chosen.push(question);
      used.add(question);
    }
  }

  if (chosen.length < count) {
    const leftovers = shuffle(pool.filter((question) => !used.has(question)));
    chosen.push(...leftovers.slice(0, count - chosen.length));
  }

  // Ordre final : du plus facile au plus difficile, pour une montee en puissance.
  const weight: Record<Difficulty, number> = { facile: 0, moyen: 1, challenge: 2 };
  return shuffle(chosen)
    .slice(0, count)
    .sort((a, b) => weight[a.difficulty] - weight[b.difficulty]);
}
