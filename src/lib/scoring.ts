import { GRACE_PERIOD_MS, SPEED_BONUS_RATIO } from "./config";
import type { Difficulty } from "./types";

export const POINTS_BY_DIFFICULTY: Record<Difficulty, number> = {
  facile: 100,
  moyen: 200,
  challenge: 300,
};

export interface ScoreInput {
  basePoints: number;
  timeLimitSeconds: number;
  servedAt: number;
  answeredAt: number;
  isCorrect: boolean;
}

export interface ScoreOutput {
  gained: number;
  speedBonus: number;
  timedOut: boolean;
}

/**
 * Calcule les points d'une reponse. Toujours execute cote serveur : le
 * navigateur n'envoie que la lettre choisie, jamais un score.
 */
export function computeScore(input: ScoreInput): ScoreOutput {
  const limitMs = input.timeLimitSeconds * 1000;
  const elapsed = Math.max(0, input.answeredAt - input.servedAt);
  const timedOut = elapsed > limitMs + GRACE_PERIOD_MS;

  if (!input.isCorrect || timedOut) {
    return { gained: 0, speedBonus: 0, timedOut };
  }

  const remaining = Math.max(0, limitMs - elapsed);
  const speedBonus = Math.round(input.basePoints * SPEED_BONUS_RATIO * (remaining / limitMs));
  return { gained: input.basePoints + speedBonus, speedBonus, timedOut: false };
}

const CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";

/** Code de session lisible a voix haute (sans caracteres ambigus). */
export function generateSessionCode(length = 6): string {
  let code = "";
  for (let i = 0; i < length; i += 1) {
    code += CODE_ALPHABET[Math.floor(Math.random() * CODE_ALPHABET.length)];
  }
  return code;
}

export function sanitizeName(raw: string): string {
  return raw.replace(/\s+/g, " ").trim().slice(0, 24);
}
