#!/usr/bin/env node
/**
 * Verifie qu'un projet Supabase est pret a accueillir l'evenement.
 *
 * Controle, dans l'ordre :
 *   1. la presence des variables d'environnement ;
 *   2. la connexion au projet ;
 *   3. l'existence des tables et de la vue leaderboard ;
 *   4. la presence des quatre categories (seed_games.sql) ;
 *   5. le nombre de questions importees par categorie ;
 *   6. l'etancheite des politiques RLS : le role anonyme ne doit pas pouvoir
 *      lire la table questions, qui contient les bonnes reponses.
 *
 * Usage : npm run db:check
 */

import { readFileSync, existsSync } from "node:fs";
import path from "node:path";
import { createClient } from "@supabase/supabase-js";

const CATEGORIES = ["entrepreneuriat", "cameroun", "innovation-ia", "mixte"];
const TABLES = ["events", "games", "questions", "players", "player_questions", "answers"];

const OK = "✓";
const KO = "✗";
const WARN = "!";

let failures = 0;
let warnings = 0;

function pass(message) {
  console.log(`  ${OK} ${message}`);
}
function fail(message, remedy) {
  failures += 1;
  console.log(`  ${KO} ${message}`);
  if (remedy) console.log(`      → ${remedy}`);
}
function warn(message, remedy) {
  warnings += 1;
  console.log(`  ${WARN} ${message}`);
  if (remedy) console.log(`      → ${remedy}`);
}

function loadEnv() {
  for (const file of [".env.local", ".env"]) {
    const full = path.join(process.cwd(), file);
    if (!existsSync(full)) continue;
    for (const line of readFileSync(full, "utf-8").split("\n")) {
      const match = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
      if (match && !process.env[match[1]]) {
        process.env[match[1]] = match[2].replace(/^["']|["']$/g, "").trim();
      }
    }
  }
}

async function main() {
  loadEnv();

  console.log("\nVariables d'environnement");
  const url = (process.env.NEXT_PUBLIC_SUPABASE_URL ?? "").trim();
  const serviceKey = (process.env.SUPABASE_SERVICE_ROLE_KEY ?? "").trim();
  const anonKey = (process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ?? "").trim();

  if (url) pass(`NEXT_PUBLIC_SUPABASE_URL = ${url}`);
  else fail("NEXT_PUBLIC_SUPABASE_URL absente", "Project Settings > API > Project URL");

  if (serviceKey) pass("SUPABASE_SERVICE_ROLE_KEY definie");
  else fail("SUPABASE_SERVICE_ROLE_KEY absente", "Project Settings > API > service_role secret");

  if (anonKey) pass("NEXT_PUBLIC_SUPABASE_ANON_KEY definie");
  else warn("NEXT_PUBLIC_SUPABASE_ANON_KEY absente", "sans elle, le classement passe par le flux SSE au lieu de Supabase Realtime");

  if (!url || !serviceKey) {
    console.log("\nImpossible de continuer sans URL ni cle de service.\n");
    process.exit(1);
  }

  const db = createClient(url, serviceKey, { auth: { persistSession: false } });

  console.log("\nConnexion et tables");
  const missing = [];
  for (const table of TABLES) {
    const { error } = await db.from(table).select("*", { count: "exact", head: true });
    if (error) {
      missing.push(table);
    }
  }
  if (missing.length === 0) {
    pass(`les ${TABLES.length} tables sont presentes`);
  } else {
    fail(`tables absentes ou inaccessibles : ${missing.join(", ")}`,
         "executez supabase/schema.sql dans l'editeur SQL de Supabase");
  }

  const { error: viewError } = await db.from("leaderboard").select("*", { head: true, count: "exact" });
  if (viewError) fail("vue leaderboard absente", "executez supabase/schema.sql");
  else pass("vue leaderboard presente");

  console.log("\nCategories");
  const { data: games, error: gamesError } = await db
    .from("games")
    .select("id, slug, name, is_active, questions_per_session")
    .order("slug");
  if (gamesError) {
    fail(`lecture de games impossible : ${gamesError.message}`, "executez supabase/schema.sql");
  } else if (!games || games.length === 0) {
    fail("aucune categorie enregistree", "executez supabase/seed_games.sql");
  } else {
    const slugs = games.map((game) => game.slug);
    const absentes = CATEGORIES.filter((slug) => !slugs.includes(slug));
    if (absentes.length === 0) pass(`les ${games.length} categories sont presentes`);
    else fail(`categories manquantes : ${absentes.join(", ")}`, "executez supabase/seed_games.sql");
  }

  console.log("\nBanque de questions");
  let totalQuestions = 0;
  if (games && games.length > 0) {
    for (const game of games) {
      const { count, error } = await db
        .from("questions")
        .select("id", { count: "exact", head: true })
        .eq("game_id", game.id);
      const total = error ? 0 : count ?? 0;
      totalQuestions += total;
      const label = `${game.slug.padEnd(16)} ${String(total).padStart(5)} questions`;
      if (total === 0) {
        fail(`${label}  (banque vide : les joueurs ne pourront pas jouer)`);
      } else if (total < game.questions_per_session) {
        warn(`${label}  (moins que les ${game.questions_per_session} questions reglees par partie)`);
      } else {
        pass(label);
      }
    }
    if (totalQuestions === 0) {
      console.log("      → lancez : npm run db:import");
    }
  }

  console.log("\nEtancheite des politiques RLS");
  if (!anonKey) {
    warn("controle impossible sans NEXT_PUBLIC_SUPABASE_ANON_KEY");
  } else {
    const anon = createClient(url, anonKey, { auth: { persistSession: false } });

    const { data: leaked, error: questionsError } = await anon
      .from("questions")
      .select("id, correct_answer")
      .limit(1);
    if (questionsError || !leaked || leaked.length === 0) {
      pass("questions : inaccessible au role anonyme (les bonnes reponses sont protegees)");
    } else {
      fail("questions : LISIBLE par le role anonyme, les bonnes reponses fuient !",
           "executez supabase/policies.sql");
    }

    const { data: answersLeak, error: answersError } = await anon.from("answers").select("id").limit(1);
    if (answersError || !answersLeak || answersLeak.length === 0) {
      pass("answers : inaccessible au role anonyme");
    } else {
      fail("answers : lisible par le role anonyme", "executez supabase/policies.sql");
    }

    const { error: playersError } = await anon.from("players").select("name, score").limit(1);
    if (playersError) {
      warn(`players : illisible par le role anonyme (${playersError.message})`,
           "le classement en direct de /display a besoin de cette lecture");
    } else {
      pass("players : lisible par le role anonyme (classement en direct)");
    }

    const { error: writeError } = await anon
      .from("players")
      .insert({ name: "controle-rls", game_id: games?.[0]?.id, session_code: `CTRL${Date.now()}` });
    if (writeError) {
      pass("players : ecriture refusee au role anonyme (les scores ne sont pas falsifiables)");
    } else {
      fail("players : le role anonyme peut ECRIRE, un joueur pourrait se donner des points",
           "executez supabase/policies.sql");
      await db.from("players").delete().eq("name", "controle-rls");
    }
  }

  console.log("");
  if (failures > 0) {
    console.log(`${failures} probleme(s) bloquant(s), ${warnings} avertissement(s).\n`);
    process.exit(1);
  }
  console.log(
    warnings > 0
      ? `Projet operationnel, avec ${warnings} avertissement(s).\n`
      : "Projet operationnel : vous pouvez lancer l'evenement.\n",
  );
}

main().catch((error) => {
  console.error("\nErreur inattendue :", error.message ?? error);
  process.exit(1);
});
