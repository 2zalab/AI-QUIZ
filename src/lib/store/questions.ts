import { DIFFICULTY_PLAN, QUESTIONS_PER_SESSION } from "../config";
import type { Difficulty } from "../types";

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
