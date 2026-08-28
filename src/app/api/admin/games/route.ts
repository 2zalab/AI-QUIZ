import { NextResponse } from "next/server";
import { MAX_QUESTIONS_PER_SESSION, MIN_QUESTIONS_PER_SESSION } from "@/lib/config";
import { isAdmin } from "@/lib/admin";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

/** Liste complete des categories, categories desactivees comprises. */
export async function GET() {
  if (!(await isAdmin())) {
    return NextResponse.json({ error: "Acces reserve a l'organisateur." }, { status: 401 });
  }
  const store = await getStore();
  return NextResponse.json({
    games: await store.listGames(),
    limits: { min: MIN_QUESTIONS_PER_SESSION, max: MAX_QUESTIONS_PER_SESSION },
  });
}

/** Reglage d'une categorie : nombre de questions par partie, activation. */
export async function POST(request: Request) {
  if (!(await isAdmin())) {
    return NextResponse.json({ error: "Acces reserve a l'organisateur." }, { status: 401 });
  }

  let payload: { slug?: string; questionsPerSession?: number; isActive?: boolean };
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "Requete invalide." }, { status: 400 });
  }

  const slug = (payload.slug ?? "").trim();
  if (!slug) return NextResponse.json({ error: "Categorie manquante." }, { status: 400 });

  const { questionsPerSession, isActive } = payload;
  if (questionsPerSession !== undefined) {
    if (!Number.isFinite(questionsPerSession)) {
      return NextResponse.json({ error: "Nombre de questions invalide." }, { status: 400 });
    }
    if (
      questionsPerSession < MIN_QUESTIONS_PER_SESSION ||
      questionsPerSession > MAX_QUESTIONS_PER_SESSION
    ) {
      return NextResponse.json(
        {
          error: `Le nombre de questions doit etre compris entre ${MIN_QUESTIONS_PER_SESSION} et ${MAX_QUESTIONS_PER_SESSION}.`,
        },
        { status: 400 },
      );
    }
  }

  try {
    const store = await getStore();
    const game = await store.updateGame(slug, { questionsPerSession, isActive });
    return NextResponse.json({ game });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Reglage impossible.";
    return NextResponse.json({ error: message }, { status: 400 });
  }
}
