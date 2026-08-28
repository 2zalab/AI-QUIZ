"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Leaderboard } from "@/components/Leaderboard";
import { useLeaderboard } from "@/lib/useLeaderboard";

interface AppConfig {
  joinUrl: string;
  mode: "supabase" | "memory";
  realtime: boolean;
}

export function AdminClient() {
  const [authenticated, setAuthenticated] = useState<boolean | null>(null);
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/admin/login", { cache: "no-store" })
      .then((response) => response.json())
      .then((payload) => setAuthenticated(Boolean(payload.authenticated)))
      .catch(() => setAuthenticated(false));
  }, []);

  async function login(event: React.FormEvent) {
    event.preventDefault();
    setError(null);
    const response = await fetch("/api/admin/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    });
    if (response.ok) {
      setAuthenticated(true);
      setPassword("");
    } else {
      const payload = await response.json().catch(() => ({}));
      setError(payload.error ?? "Connexion refusee.");
    }
  }

  if (authenticated === null) {
    return (
      <main className="flex min-h-screen items-center justify-center">
        <p className="animate-pulse text-muted">Verification...</p>
      </main>
    );
  }

  if (!authenticated) {
    return (
      <main className="mx-auto flex min-h-screen max-w-sm flex-col justify-center px-6">
        <h1 className="text-2xl font-black">Espace organisateur</h1>
        <p className="mt-2 text-sm text-muted">
          Saisissez le mot de passe defini dans la variable ADMIN_PASSWORD.
        </p>
        <form onSubmit={login} className="mt-6 space-y-4">
          <input
            type="password"
            className="field"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Mot de passe"
            autoFocus
          />
          {error && (
            <p role="alert" className="text-sm text-rose-700 dark:text-rose-300">
              {error}
            </p>
          )}
          <button type="submit" className="btn-primary w-full">
            Se connecter
          </button>
        </form>
        <Link href="/" className="mt-6 text-center text-sm text-faint hover:text-muted">
          Retour a l&apos;accueil
        </Link>
      </main>
    );
  }

  return <Dashboard onLogout={() => setAuthenticated(false)} />;
}

function Dashboard({ onLogout }: { onLogout: () => void }) {
  const { entries, stats, connected } = useLeaderboard();
  const [config, setConfig] = useState<AppConfig | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [confirming, setConfirming] = useState(false);

  useEffect(() => {
    fetch("/api/config", { cache: "no-store" })
      .then((response) => response.json())
      .then(setConfig)
      .catch(() => setConfig(null));
  }, []);

  async function reset() {
    const response = await fetch("/api/admin/reset", { method: "POST" });
    setMessage(
      response.ok
        ? "Classement remis a zero."
        : "La remise a zero a echoue. Reconnectez-vous puis reessayez.",
    );
    setConfirming(false);
  }

  async function logout() {
    await fetch("/api/admin/login", { method: "DELETE" });
    onLogout();
  }

  return (
    <main className="mx-auto w-full max-w-6xl px-6 py-8">
      <header className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-black">Espace organisateur</h1>
          <p className="mt-1 flex items-center gap-2 text-sm text-muted">
            <span
              className={`h-2 w-2 rounded-full ${connected ? "bg-emerald-400" : "bg-rose-400"}`}
              aria-hidden
            />
            {connected ? "Donnees en direct" : "Reconnexion en cours"}
            {config && (
              <>
                <span aria-hidden>&middot;</span>
                <span>
                  stockage : {config.mode === "supabase" ? "Supabase" : "memoire (demonstration)"}
                </span>
              </>
            )}
          </p>
        </div>
        <div className="flex gap-3">
          <Link href="/display" className="btn-ghost" target="_blank">
            Ouvrir l&apos;ecran public
          </Link>
          <button type="button" onClick={() => void logout()} className="btn-ghost">
            Deconnexion
          </button>
        </div>
      </header>

      {config?.mode === "memory" && (
        <p className="mt-6 rounded-xl border border-amber-400/40 bg-amber-400/10 px-4 py-3 text-sm text-amber-800 dark:text-amber-100">
          Mode demonstration : les parties sont stockees en memoire et disparaissent au redemarrage
          du serveur. Renseignez les variables Supabase pour un evenement reel.
        </p>
      )}

      <section className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Metric label="Joueurs" value={stats?.totalPlayers ?? 0} accent />
        <Metric label="En jeu" value={stats?.playing ?? 0} />
        <Metric label="Termines" value={stats?.finished ?? 0} />
        <Metric label="Score moyen" value={stats?.averageScore ?? 0} />
      </section>

      <div className="mt-8 grid gap-8 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <section>
          <h2 className="mb-3 text-xl font-bold">Classement general</h2>
          <Leaderboard entries={entries} compact />
        </section>

        <aside className="space-y-5">
          <div className="card p-5">
            <h3 className="text-sm font-bold uppercase tracking-widest text-muted">
              Participation par defi
            </h3>
            <ul className="mt-3 space-y-2 text-sm">
              {(stats?.byGame ?? []).map((game) => (
                <li key={game.slug} className="flex items-center justify-between">
                  <span>
                    {game.emoji} {game.name}
                  </span>
                  <span className="font-bold tabular-nums">{game.players}</span>
                </li>
              ))}
            </ul>
          </div>

          {config && (
            <div className="card p-5">
              <h3 className="text-sm font-bold uppercase tracking-widest text-muted">
                Lien de participation
              </h3>
              <p className="mt-2 break-all text-sm text-fg">{config.joinUrl}</p>
              <div className="mt-3 rounded-xl bg-white p-2">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/api/qr" alt="QR code de participation" className="h-auto w-full" />
              </div>
            </div>
          )}

          <div className="card p-5">
            <h3 className="text-sm font-bold uppercase tracking-widest text-muted">
              Nouvelle manche
            </h3>
            <p className="mt-2 text-sm text-muted">
              Efface tous les joueurs et repart d&apos;un classement vierge.
            </p>
            {confirming ? (
              <div className="mt-3 flex gap-2">
                <button type="button" onClick={() => void reset()} className="btn-primary flex-1">
                  Confirmer
                </button>
                <button type="button" onClick={() => setConfirming(false)} className="btn-ghost flex-1">
                  Annuler
                </button>
              </div>
            ) : (
              <button type="button" onClick={() => setConfirming(true)} className="btn-ghost mt-3 w-full">
                Remettre le classement a zero
              </button>
            )}
            {message && <p className="mt-3 text-sm text-muted">{message}</p>}
          </div>
        </aside>
      </div>
    </main>
  );
}

function Metric({ label, value, accent = false }: { label: string; value: number; accent?: boolean }) {
  return (
    <div className="card p-5">
      <p className={`text-4xl font-black tabular-nums ${accent ? "text-accent" : ""}`}>
        {value.toLocaleString("fr-FR")}
      </p>
      <p className="mt-1 text-xs uppercase tracking-widest text-muted">{label}</p>
    </div>
  );
}
