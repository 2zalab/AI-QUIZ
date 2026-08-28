import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const gameSlug = url.searchParams.get("game") ?? undefined;
  const limit = Number(url.searchParams.get("limit") ?? 20);

  const store = await getStore();
  const [entries, stats] = await Promise.all([
    store.leaderboard({ gameSlug, limit: Number.isFinite(limit) ? limit : 20 }),
    store.stats(),
  ]);
  return NextResponse.json({ entries, stats });
}
