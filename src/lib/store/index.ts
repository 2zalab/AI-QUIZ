import type {
  AnswerResult, Game, LeaderboardEntry, Letter, PublicQuestion, SessionState, Stats,
} from "../types";

export interface GameSettings {
  questionsPerSession?: number;
  isActive?: boolean;
}

export interface Store {
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

export const MISSING_CONFIG_MESSAGE =
  "La base de donnees n'est pas configuree. Renseignez NEXT_PUBLIC_SUPABASE_URL et " +
  "SUPABASE_SERVICE_ROLE_KEY dans les variables d'environnement, puis redeployez.";

/** Variables indispensables au fonctionnement de l'application. */
export function missingSupabaseVars(): string[] {
  return (["NEXT_PUBLIC_SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY"] as const).filter(
    (name) => !(process.env[name] ?? "").trim(),
  );
}

export function hasSupabaseConfig(): boolean {
  return missingSupabaseVars().length === 0;
}

/**
 * Magasin de donnees de l'application : Supabase, et rien d'autre.
 *
 * Il n'existe volontairement aucun mode de repli. Un repli silencieux donnerait
 * une application qui parait fonctionner mais perd tous les scores au moindre
 * redemarrage : mieux vaut une erreur explicite au demarrage.
 */
export async function getStore(): Promise<Store> {
  if (instance) return instance;
  const missing = missingSupabaseVars();
  if (missing.length > 0) {
    console.error(`[MIT] Variables manquantes : ${missing.join(", ")}. ${MISSING_CONFIG_MESSAGE}`);
    throw new Error(MISSING_CONFIG_MESSAGE);
  }
  const { createSupabaseStore } = await import("./supabase");
  instance = createSupabaseStore();
  return instance;
}
