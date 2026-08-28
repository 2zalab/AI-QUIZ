#!/usr/bin/env node
/**
 * Importe les fichiers CSV du dossier data/ dans la base Supabase.
 *
 * Prerequis :
 *   1. avoir execute supabase/schema.sql puis supabase/seed_games.sql ;
 *   2. renseigner NEXT_PUBLIC_SUPABASE_URL et SUPABASE_SERVICE_ROLE_KEY.
 *
 * Usage :
 *   node scripts/import-questions.mjs            # importe les 4 categories
 *   node scripts/import-questions.mjs cameroun   # importe une seule categorie
 */

import { readFileSync, existsSync } from "node:fs";
import path from "node:path";
import { createClient } from "@supabase/supabase-js";
import { parse } from "csv-parse/sync";

const FILES = {
  entrepreneuriat: "questions_entrepreneuriat.csv",
  cameroun: "questions_cameroun.csv",
  "innovation-ia": "questions_innovation_ia.csv",
  mixte: "questions_mixte.csv",
};

const BATCH_SIZE = 500;

function loadEnv() {
  // Petit chargeur .env.local, pour eviter une dependance supplementaire.
  for (const file of [".env.local", ".env"]) {
    const full = path.join(process.cwd(), file);
    if (!existsSync(full)) continue;
    for (const line of readFileSync(full, "utf-8").split("\n")) {
      const match = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
      if (match && !process.env[match[1]]) {
        process.env[match[1]] = match[2].replace(/^["']|["']$/g, "");
      }
    }
  }
}

async function main() {
  loadEnv();
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !key) {
    console.error(
      "Variables manquantes : NEXT_PUBLIC_SUPABASE_URL et SUPABASE_SERVICE_ROLE_KEY sont requises.",
    );
    process.exit(1);
  }

  const only = process.argv.slice(2);
  const slugs = only.length > 0 ? only : Object.keys(FILES);
  const db = createClient(url, key, { auth: { persistSession: false } });

  const { data: games, error: gamesError } = await db.from("games").select("id, slug");
  if (gamesError) {
    console.error("Impossible de lire la table games :", gamesError.message);
    console.error("Avez-vous execute supabase/seed_games.sql ?");
    process.exit(1);
  }
  const gameIdBySlug = new Map(games.map((game) => [game.slug, game.id]));

  let grandTotal = 0;
  for (const slug of slugs) {
    const file = FILES[slug];
    if (!file) {
      console.warn(`Categorie inconnue, ignoree : ${slug}`);
      continue;
    }
    const gameId = gameIdBySlug.get(slug);
    if (!gameId) {
      console.error(`Categorie absente de la table games : ${slug}`);
      process.exit(1);
    }

    const csvPath = path.join(process.cwd(), "data", file);
    if (!existsSync(csvPath)) {
      console.error(`Fichier introuvable : ${csvPath}`);
      console.error("Lancez d'abord : npm run questions:generate");
      process.exit(1);
    }

    const rows = parse(readFileSync(csvPath, "utf-8"), {
      columns: true,
      skip_empty_lines: true,
      bom: true,
    });

    const payload = rows.map((row) => ({
      id: row.id,
      game_id: gameId,
      difficulty: row.difficulty,
      question: row.question,
      option_a: row.option_a,
      option_b: row.option_b,
      option_c: row.option_c,
      option_d: row.option_d,
      correct_answer: row.correct_answer,
      points: Number(row.points),
      time_limit: Number(row.time_limit),
      explanation: row.explanation,
      tags: row.tags,
    }));

    for (let start = 0; start < payload.length; start += BATCH_SIZE) {
      const batch = payload.slice(start, start + BATCH_SIZE);
      const { error } = await db.from("questions").upsert(batch, { onConflict: "id" });
      if (error) {
        console.error(`Erreur d'import (${slug}, lot ${start}) :`, error.message);
        process.exit(1);
      }
      process.stdout.write(`\r${slug} : ${Math.min(start + BATCH_SIZE, payload.length)}/${payload.length}`);
    }
    process.stdout.write("\n");
    grandTotal += payload.length;
  }

  console.log(`\n${grandTotal} questions importees dans Supabase.`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
