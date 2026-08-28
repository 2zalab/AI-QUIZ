import { NextResponse } from "next/server";
import { isAdmin } from "@/lib/admin";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";

/** Remet le classement a zero entre deux sessions de jeu. */
export async function POST() {
  if (!(await isAdmin())) {
    return NextResponse.json({ error: "Acces reserve a l'organisateur." }, { status: 401 });
  }
  const store = await getStore();
  await store.reset();
  return NextResponse.json({ ok: true });
}
