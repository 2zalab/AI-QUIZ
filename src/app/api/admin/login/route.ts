import { NextResponse } from "next/server";
import {
  ADMIN_COOKIE, adminPassword, adminToken, isAdmin, passwordDiagnostics,
} from "@/lib/admin";

export const dynamic = "force-dynamic";

/**
 * Etat de la session organisateur, accompagne d'un diagnostic de configuration.
 *
 * Le diagnostic ne revele jamais le mot de passe : il signale seulement les
 * erreurs de saisie courantes dans la variable d'environnement, pour eviter de
 * chercher a l'aveugle apres un deploiement.
 */
export async function GET() {
  return NextResponse.json({
    authenticated: await isAdmin(),
    config: passwordDiagnostics(),
  });
}

export async function POST(request: Request) {
  let payload: { password?: string };
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "Requete invalide." }, { status: 400 });
  }

  // Le mot de passe saisi est nettoye comme la variable : un espace ajoute par
  // le clavier d'un telephone ne doit pas bloquer l'organisateur.
  if ((payload.password ?? "").trim() !== adminPassword()) {
    return NextResponse.json(
      { error: "Mot de passe incorrect.", config: passwordDiagnostics() },
      { status: 401 },
    );
  }

  const response = NextResponse.json({ authenticated: true });
  response.cookies.set(ADMIN_COOKIE, adminToken(), {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/",
    maxAge: 60 * 60 * 12,
  });
  return response;
}

export async function DELETE() {
  const response = NextResponse.json({ authenticated: false });
  response.cookies.delete(ADMIN_COOKIE);
  return response;
}
