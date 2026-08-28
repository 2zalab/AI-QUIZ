import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const gameSlug = url.searchParams.get("game") ?? undefined;
  const limit = Number(url.searchParams.get("limit") ?? 20);

  try {
    const store = await getStore();
    const [entries, stats] = await Promise.all([
      store.leaderboard({ gameSlug, limit: Number.isFinite(limit) ? limit : 20 }),
      store.stats(),
    ]);
    return NextResponse.json({ entries, stats });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Base de donnees indisponible.";
    return NextResponse.json({ error: message, entries: [], stats: null }, { status: 503 });
  }
}
