import { NextResponse } from "next/server";
import { appUrl } from "@/lib/config";
import { getStore, hasSupabaseConfig, missingSupabaseVars } from "@/lib/store";

export const dynamic = "force-dynamic";

/**
 * Informations publiques necessaires aux ecrans, completees d'un etat de
 * configuration du deploiement.
 *
 * Aucune valeur secrete n'est exposee : uniquement la presence ou l'absence de
 * chaque variable, et le nombre de questions reellement accessibles. C'est ce
 * qui permet de comprendre en une requete pourquoi une categorie parait vide.
 */
export async function GET() {
  const present = (name: string) => Boolean((process.env[name] ?? "").trim());
  const missing = missingSupabaseVars();

  let banks: { slug: string; questions: number }[] = [];
  let banksError: string | null = null;
  if (missing.length === 0) {
    try {
      banks = (await getStore().then((store) => store.listGames())).map((game) => ({
        slug: game.slug,
        questions: game.questionCount,
      }));
    } catch (error) {
      banksError = error instanceof Error ? error.message : "lecture impossible";
    }
  } else {
    banksError = `Variables manquantes : ${missing.join(", ")}`;
  }

  return NextResponse.json({
    appUrl: appUrl(),
    joinUrl: `${appUrl()}/join`,
    configured: hasSupabaseConfig(),
    missing,
    realtime: hasSupabaseConfig() && present("NEXT_PUBLIC_SUPABASE_ANON_KEY"),
    env: {
      NEXT_PUBLIC_APP_URL: present("NEXT_PUBLIC_APP_URL"),
      NEXT_PUBLIC_SUPABASE_URL: present("NEXT_PUBLIC_SUPABASE_URL"),
      NEXT_PUBLIC_SUPABASE_ANON_KEY: present("NEXT_PUBLIC_SUPABASE_ANON_KEY"),
      SUPABASE_SERVICE_ROLE_KEY: present("SUPABASE_SERVICE_ROLE_KEY"),
      ADMIN_PASSWORD: present("ADMIN_PASSWORD"),
    },
    banks,
    banksError,
  });
}
