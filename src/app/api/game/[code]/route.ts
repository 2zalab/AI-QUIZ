import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

/**
 * Etat courant de la partie. Si aucune question n'est encore servie, la
 * prochaine est distribuee ici : c'est le serveur qui declenche le chrono.
 * La bonne reponse n'est jamais incluse dans la charge utile.
 */
export async function GET(_request: Request, context: { params: Promise<{ code: string }> }) {
  const { code } = await context.params;
  const store = await getStore();

  let state = await store.getState(code);
  if (!state) return NextResponse.json({ error: "Session introuvable." }, { status: 404 });

  if (!state.finished && !state.question) {
    await store.serveQuestion(code);
    state = await store.getState(code);
  }

  return NextResponse.json(state);
}
