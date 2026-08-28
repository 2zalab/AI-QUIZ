import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const store = await getStore();
    return NextResponse.json(await store.stats());
  } catch (error) {
    const message = error instanceof Error ? error.message : "Base de donnees indisponible.";
    return NextResponse.json({ error: message }, { status: 503 });
  }
}
