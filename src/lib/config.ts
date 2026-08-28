import type { Game } from "./types";

/**
 * Nombre de questions servies par partie, par defaut. L'organisateur peut le
 * changer categorie par categorie depuis /admin ; cette valeur ne sert qu'au
 * premier demarrage, avant tout reglage.
 */
export const QUESTIONS_PER_SESSION = Number(process.env.QUESTIONS_PER_SESSION ?? 10);

/** Bornes acceptees par le reglage (identiques a la contrainte SQL). */
export const MIN_QUESTIONS_PER_SESSION = 3;
export const MAX_QUESTIONS_PER_SESSION = 50;

/** Ramene une valeur saisie dans les bornes autorisees. */
export function clampQuestionsPerSession(value: number): number {
  if (!Number.isFinite(value)) return QUESTIONS_PER_SESSION;
  return Math.min(MAX_QUESTIONS_PER_SESSION, Math.max(MIN_QUESTIONS_PER_SESSION, Math.round(value)));
}

/** Repartition visee des difficultes dans une partie. Le reste est complete au hasard. */
export const DIFFICULTY_PLAN: Record<string, number> = {
  facile: 4,
  moyen: 4,
  challenge: 2,
};

/** Part maximale des points de base attribuee en bonus de rapidite. */
export const SPEED_BONUS_RATIO = 0.5;

/** Tolerance reseau accordee au joueur au-dela du temps imparti (ms). */
export const GRACE_PERIOD_MS = 1500;

export const GAMES: Game[] = [
  {
    slug: "entrepreneuriat",
    name: "Entrepreneuriat",
    description: "Business, marketing, financement, gestion et innovation.",
    emoji: "\u{1F4BC}",
    color: "#f4b93e",
    isActive: true,
    questionsPerSession: QUESTIONS_PER_SESSION,
    questionCount: 0,
  },
  {
    slug: "cameroun",
    name: "Cameroun",
    description: "Culture, histoire, geographie, economie et personnalites.",
    emoji: "\u{1F1E8}\u{1F1F2}",
    color: "#22c8b0",
    isActive: true,
    questionsPerSession: QUESTIONS_PER_SESSION,
    questionCount: 0,
  },
  {
    slug: "innovation-ia",
    name: "Innovation & IA",
    description: "Le numerique et l'intelligence artificielle au quotidien.",
    emoji: "\u{1F4A1}",
    color: "#8b7cf6",
    isActive: true,
    questionsPerSession: QUESTIONS_PER_SESSION,
    questionCount: 0,
  },
  {
    slug: "mixte",
    name: "Challenge Mixte",
    description: "Un melange des trois univers, pour les plus polyvalents.",
    emoji: "\u{1F3AF}",
    color: "#f472b6",
    isActive: true,
    questionsPerSession: QUESTIONS_PER_SESSION,
    questionCount: 0,
  },
];

export const GAME_BY_SLUG = new Map(GAMES.map((game) => [game.slug, game]));

export function appUrl(): string {
  return (
    process.env.NEXT_PUBLIC_APP_URL ??
    (process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : "http://localhost:3000")
  );
}
