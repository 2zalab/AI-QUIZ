import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

export async function POST(request: Request) {
  let payload: { name?: string; game?: string };
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "Requete invalide." }, { status: 400 });
  }

  const name = (payload.name ?? "").trim();
  const game = (payload.game ?? "").trim();
  if (!name) return NextResponse.json({ error: "Merci d'indiquer votre nom." }, { status: 400 });
  if (!game) return NextResponse.json({ error: "Merci de choisir un defi." }, { status: 400 });

  try {
    const store = await getStore();
    const { sessionCode } = await store.createSession(name, game);
    return NextResponse.json({ sessionCode, redirectTo: `/game/${sessionCode}` });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Impossible de rejoindre la partie.";
    return NextResponse.json({ error: message }, { status: 400 });
  }
}
