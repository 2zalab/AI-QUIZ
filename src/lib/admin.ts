import { cookies } from "next/headers";

export const ADMIN_COOKIE = "iclan_admin";

/** Mot de passe de repli, utilise uniquement si ADMIN_PASSWORD n'est pas defini. */
export const FALLBACK_PASSWORD = "iclan2026";

/**
 * Mot de passe attendu.
 *
 * La valeur est nettoyee de ses espaces et retours a la ligne : un copier-coller
 * dans un tableau de bord d'hebergeur en ajoute tres souvent, et cela rendrait
 * la connexion impossible sans aucun message explicite.
 */
export function adminPassword(): string {
  const configured = (process.env.ADMIN_PASSWORD ?? "").trim();
  return configured || FALLBACK_PASSWORD;
}

/** Vrai lorsque la variable d'environnement est reellement definie. */
export function isPasswordConfigured(): boolean {
  return (process.env.ADMIN_PASSWORD ?? "").trim().length > 0;
}

/**
 * Anomalies detectables dans la variable, signalees sans jamais reveler sa
 * valeur. Elles couvrent les erreurs de saisie les plus frequentes.
 */
export function passwordDiagnostics() {
  const raw = process.env.ADMIN_PASSWORD ?? "";
  const trimmed = raw.trim();
  return {
    configured: trimmed.length > 0,
    usingFallback: trimmed.length === 0,
    // Espaces ou retour a la ligne autour de la valeur (copier-coller).
    hasWhitespaceEdges: raw.length !== raw.trim().length,
    // La ligne entiere « ADMIN_PASSWORD=... » collee dans le champ Value.
    looksLikeAssignment: /^ADMIN_PASSWORD\s*=/i.test(trimmed),
    // Guillemets conserves autour de la valeur.
    hasSurroundingQuotes:
      trimmed.length > 1 &&
      ((trimmed.startsWith('"') && trimmed.endsWith('"')) ||
        (trimmed.startsWith("'") && trimmed.endsWith("'"))),
  };
}

/** Jeton derive du mot de passe : il change des que le mot de passe change. */
export function adminToken(): string {
  let hash = 5381;
  const secret = `iclan|${adminPassword()}`;
  for (let i = 0; i < secret.length; i += 1) {
    hash = ((hash << 5) + hash + secret.charCodeAt(i)) >>> 0;
  }
  return hash.toString(36);
}

export async function isAdmin(): Promise<boolean> {
  const store = await cookies();
  return store.get(ADMIN_COOKIE)?.value === adminToken();
}
