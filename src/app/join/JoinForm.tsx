"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import type { Game } from "@/lib/types";

export function JoinForm() {
  const router = useRouter();
  const [games, setGames] = useState<Game[]>([]);
  const [name, setName] = useState("");
  const [selected, setSelected] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    fetch("/api/games", { cache: "no-store" })
      .then((response) => response.json())
      .then((payload) => setGames(payload.games ?? []))
      .catch(() => setError("Impossible de charger les categories."));
  }, []);

  // Le prenom saisi est conserve localement pour eviter de le retaper.
  useEffect(() => {
    const stored = window.localStorage.getItem("iclan-name");
    if (stored) setName(stored);
  }, []);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    setError(null);

    if (!name.trim()) return setError("Merci d'indiquer votre nom.");
    if (!selected) return setError("Choisissez votre defi pour continuer.");

    setSubmitting(true);
    try {
      window.localStorage.setItem("iclan-name", name.trim());
      const response = await fetch("/api/join", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name.trim(), game: selected }),
      });
      const payload = await response.json();
      if (!response.ok) throw new Error(payload.error ?? "Impossible de rejoindre la partie.");
      router.push(payload.redirectTo);
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Une erreur est survenue.");
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="mt-8 flex flex-1 flex-col gap-6">
      <div>
        <label htmlFor="player-name" className="mb-2 block text-sm font-semibold text-slate-300">
          Votre nom ou celui de votre equipe
        </label>
        <input
          id="player-name"
          className="field"
          value={name}
          onChange={(event) => setName(event.target.value)}
          placeholder="Ex. : Isaac"
          maxLength={24}
          autoComplete="off"
          autoFocus
        />
      </div>

      <div>
        <p className="mb-2 text-sm font-semibold text-slate-300">Choisissez votre defi</p>
        <div className="grid gap-3">
          {games.length === 0 && (
            <div className="card animate-pulse p-6 text-center text-sm text-slate-500">
              Chargement des categories...
            </div>
          )}
          {games.map((game) => {
            const active = selected === game.slug;
            return (
              <button
                key={game.slug}
                type="button"
                onClick={() => setSelected(game.slug)}
                aria-pressed={active}
                className={[
                  "card flex items-center gap-4 p-4 text-left transition",
                  active
                    ? "border-gold-400 bg-gold-400/10 ring-2 ring-gold-400/40"
                    : "hover:border-white/25 hover:bg-white/[0.07]",
                ].join(" ")}
              >
                <span className="text-3xl">{game.emoji}</span>
                <span className="min-w-0 flex-1">
                  <span className="block font-bold">{game.name}</span>
                  <span className="block text-xs leading-snug text-slate-400">{game.description}</span>
                </span>
                <span
                  className={[
                    "flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-xs",
                    active ? "border-gold-400 bg-gold-400 text-ink-950" : "border-white/25",
                  ].join(" ")}
                  aria-hidden
                >
                  {active ? "✓" : ""}
                </span>
              </button>
            );
          })}
        </div>
      </div>

      {error && (
        <p role="alert" className="rounded-xl border border-rose-500/40 bg-rose-500/10 px-4 py-3 text-sm text-rose-200">
          {error}
        </p>
      )}

      <div className="mt-auto pt-2">
        <button type="submit" className="btn-primary w-full text-lg" disabled={submitting}>
          {submitting ? "Preparation de la partie..." : "Commencer"}
        </button>
        <p className="mt-3 text-center text-xs text-slate-500">
          10 questions &middot; plus vous repondez vite, plus vous marquez de points.
        </p>
      </div>
    </form>
  );
}
