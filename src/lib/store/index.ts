import type {
  AnswerResult, Game, LeaderboardEntry, Letter, PublicQuestion, SessionState, Stats,
} from "../types";

export interface GameSettings {
  questionsPerSession?: number;
  isActive?: boolean;
}

export interface Store {
  readonly mode: "supabase" | "memory";
  listGames(): Promise<Game[]>;
  /** Applique un reglage de categorie depuis l'espace organisateur. */
  updateGame(slug: string, settings: GameSettings): Promise<Game>;
  createSession(name: string, gameSlug: string): Promise<{ sessionCode: string }>;
  getState(sessionCode: string): Promise<SessionState | null>;
  serveQuestion(sessionCode: string): Promise<PublicQuestion | null>;
  submitAnswer(sessionCode: string, questionId: string, answer: Letter | null): Promise<AnswerResult>;
  leaderboard(options?: { gameSlug?: string; limit?: number }): Promise<LeaderboardEntry[]>;
  stats(): Promise<Stats>;
  reset(): Promise<void>;
  version(): Promise<number>;
}

let instance: Store | null = null;

export function hasSupabaseConfig(): boolean {
  return Boolean(process.env.NEXT_PUBLIC_SUPABASE_URL && process.env.SUPABASE_SERVICE_ROLE_KEY);
}

/**
 * Retourne le magasin de donnees actif : Supabase quand il est configure,
 * sinon un magasin en memoire alimente par les CSV (mode demonstration).
 */
export async function getStore(): Promise<Store> {
  if (instance) return instance;
  if (hasSupabaseConfig()) {
    const { createSupabaseStore } = await import("./supabase");
    instance = createSupabaseStore();
  } else {
    const { createMemoryStore } = await import("./memory");
    instance = createMemoryStore();
  }
  return instance;
}
