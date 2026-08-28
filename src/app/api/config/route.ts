import { NextResponse } from "next/server";
import { appUrl } from "@/lib/config";
import { getStore, hasSupabaseConfig } from "@/lib/store";

export const dynamic = "force-dynamic";

/** Informations publiques necessaires aux ecrans (URL du QR code, mode de stockage). */
export async function GET() {
  const store = await getStore();
  return NextResponse.json({
    appUrl: appUrl(),
    joinUrl: `${appUrl()}/join`,
    mode: store.mode,
    realtime: hasSupabaseConfig() && Boolean(process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY),
  });
}
