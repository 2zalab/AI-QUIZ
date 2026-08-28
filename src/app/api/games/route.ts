import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const store = await getStore();
    const games = await store.listGames();
    return NextResponse.json({ games: games.filter((game) => game.isActive) });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Base de donnees indisponible.";
    return NextResponse.json({ error: message, games: [] }, { status: 503 });
  }
}
