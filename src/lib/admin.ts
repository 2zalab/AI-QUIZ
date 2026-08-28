import { cookies } from "next/headers";

export const ADMIN_COOKIE = "iclan_admin";

export function adminPassword(): string {
  return process.env.ADMIN_PASSWORD ?? "iclan2026";
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
