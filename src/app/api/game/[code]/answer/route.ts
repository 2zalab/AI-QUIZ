import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";
import type { Letter } from "@/lib/types";

export const dynamic = "force-dynamic";

const LETTERS: Letter[] = ["A", "B", "C", "D"];

/**
 * Verification de la reponse cote serveur. Le navigateur envoie uniquement
 * l'identifiant de la question et la lettre choisie ; le score est calcule ici.
 */
export async function POST(request: Request, context: { params: Promise<{ code: string }> }) {
  const { code } = await context.params;

  let payload: { questionId?: string; answer?: string | null };
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "Requete invalide." }, { status: 400 });
  }

  const questionId = (payload.questionId ?? "").trim();
  if (!questionId) return NextResponse.json({ error: "Question manquante." }, { status: 400 });

  const raw = payload.answer;
  const answer = raw && LETTERS.includes(raw as Letter) ? (raw as Letter) : null;

  try {
    const store = await getStore();
    const result = await store.submitAnswer(code, questionId, answer);
    return NextResponse.json(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : "Reponse refusee.";
    return NextResponse.json({ error: message }, { status: 400 });
  }
}
