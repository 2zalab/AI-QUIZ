"use client";

import { useEffect, useState } from "react";
import { Leaderboard } from "@/components/Leaderboard";
import { useLeaderboard } from "@/lib/useLeaderboard";

export function DisplayClient({ joinUrl }: { joinUrl: string }) {
  const { entries, stats, connected } = useLeaderboard();
  const [displayUrl, setDisplayUrl] = useState(joinUrl);

  // Sur un reseau local, l'adresse vue par le videoprojecteur est la bonne.
  useEffect(() => {
    if (typeof window !== "undefined") {
      setDisplayUrl(`${window.location.origin}/join`);
    }
  }, []);

  const started = entries.length > 0;

  return (
    <main className="flex min-h-screen flex-col px-8 py-6">
      <header className="flex items-center justify-between">
        <div>
          <p className="badge bg-accent-soft text-accent">Business &middot; Innovation &middot; Cameroun</p>
          <h1 className="mt-2 text-4xl font-black leading-none xl:text-5xl">
            <span className="title-shine">iCLAN Entrepreneur Challenge</span>
          </h1>
        </div>
        <div className="text-right">
          <p className="flex items-center justify-end gap-2 text-sm text-muted">
            <span
              className={`h-2.5 w-2.5 rounded-full ${connected ? "bg-emerald-400 animate-pulse-slow" : "bg-rose-400"}`}
              aria-hidden
            />
            {connected ? "Classement en direct" : "Reconnexion..."}
          </p>
          <p className="mt-1 text-5xl font-black tabular-nums text-accent">
            {stats?.totalPlayers ?? 0}
          </p>
          <p className="text-xs uppercase tracking-widest text-muted">joueurs connectes</p>
        </div>
      </header>

      <div className="mt-6 grid flex-1 gap-8 lg:grid-cols-[minmax(0,26rem)_minmax(0,1fr)]">
        <section className="flex flex-col gap-5">
          <div className="card flex flex-col items-center p-6 text-center">
            <p className="text-lg font-bold uppercase tracking-widest text-accent">
              Scannez pour jouer
            </p>
            <div className="mt-4 w-full max-w-[19rem] overflow-hidden rounded-2xl bg-white p-3">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={`/api/qr?url=${encodeURIComponent(displayUrl)}`}
                alt="QR code pour rejoindre le jeu"
                className="h-auto w-full"
              />
            </div>
            <p className="mt-4 break-all text-sm font-semibold text-muted">{displayUrl}</p>
            <p className="mt-1 text-xs text-faint">
              Aucune application a installer : tout se passe dans le navigateur.
            </p>
          </div>

          {stats && (
            <div className="card p-5">
              <p className="text-sm font-bold uppercase tracking-widest text-muted">
                Participation par defi
              </p>
              <ul className="mt-3 space-y-2">
                {stats.byGame.map((game) => (
                  <li key={game.slug} className="flex items-center justify-between text-lg">
                    <span className="flex items-center gap-2">
                      <span aria-hidden>{game.emoji}</span>
                      <span className="text-fg">{game.name}</span>
                    </span>
                    <span className="font-bold tabular-nums text-accent">{game.players}</span>
                  </li>
                ))}
              </ul>
              <div className="mt-4 flex justify-between border-t border-line pt-3 text-sm">
                <StatusPill color="bg-emerald-400" label="En jeu" value={stats.playing} />
                <StatusPill color="bg-amber-400" label="En attente" value={stats.waiting} />
                <StatusPill color="bg-rose-400" label="Termines" value={stats.finished} />
              </div>
            </div>
          )}
        </section>

        <section className="flex min-w-0 flex-col">
          <h2 className="mb-4 flex items-center gap-3 text-3xl font-black">
            <span aria-hidden>{"\u{1F3C6}"}</span>
            Classement en direct
          </h2>
          <div className="min-h-0 flex-1 overflow-y-auto pr-1">
            <Leaderboard entries={entries} />
          </div>
          {started && stats && (
            <p className="mt-4 text-sm text-faint">
              Score moyen : {stats.averageScore.toLocaleString("fr-FR")} points
            </p>
          )}
        </section>
      </div>
    </main>
  );
}

function StatusPill({ color, label, value }: { color: string; label: string; value: number }) {
  return (
    <span className="flex items-center gap-2 text-muted">
      <span className={`h-2 w-2 rounded-full ${color}`} aria-hidden />
      {label}
      <strong className="tabular-nums text-fg">{value}</strong>
    </span>
  );
}
