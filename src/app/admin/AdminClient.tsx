"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Leaderboard } from "@/components/Leaderboard";
import { useLeaderboard } from "@/lib/useLeaderboard";
import type { Game } from "@/lib/types";

interface PasswordConfig {
  configured: boolean;
  usingFallback: boolean;
  hasWhitespaceEdges: boolean;
  looksLikeAssignment: boolean;
  hasSurroundingQuotes: boolean;
}

/** Traduit le diagnostic serveur en conseil actionnable pour l'organisateur. */
function configHint(config: PasswordConfig | null): string | null {
  if (!config) return null;
  if (config.looksLikeAssignment) {
    return "La variable contient la ligne entiere « ADMIN_PASSWORD=... ». Dans le champ Value de votre hebergeur, ne mettez que le mot de passe, sans le nom de la variable ni le signe egal.";
  }
  if (config.hasSurroundingQuotes) {
    return "La variable est entouree de guillemets. Retirez-les : la valeur doit etre le mot de passe seul.";
  }
  if (config.hasWhitespaceEdges) {
    return "La variable contient un espace ou un retour a la ligne en debut ou en fin. Il est ignore par l'application, mais verifiez la valeur enregistree.";
  }
  if (config.usingFallback) {
    return "La variable ADMIN_PASSWORD n'est pas visible par l'application : soit elle n'a pas ete enregistree pour cet environnement, soit le projet n'a pas ete redeploye depuis. Le mot de passe de repli est actuellement actif.";
  }
  return null;
}

interface AppConfig {
  joinUrl: string;
  configured: boolean;
  missing: string[];
  realtime: boolean;
}

export function AdminClient() {
  const [authenticated, setAuthenticated] = useState<boolean | null>(null);
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [config, setConfig] = useState<PasswordConfig | null>(null);

  useEffect(() => {
    fetch("/api/admin/login", { cache: "no-store" })
      .then((response) => response.json())
      .then((payload) => {
        setAuthenticated(Boolean(payload.authenticated));
        if (payload.config) setConfig(payload.config as PasswordConfig);
      })
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
      if (payload.config) setConfig(payload.config as PasswordConfig);
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
          {config?.usingFallback && (
            <>
              {" "}
              <span className="text-amber-700 dark:text-amber-300">
                Cette variable n&apos;est pas encore active sur ce deploiement.
              </span>
            </>
          )}
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
          {error && configHint(config) && (
            <p className="rounded-xl border border-amber-400/40 bg-amber-400/10 px-4 py-3 text-sm leading-relaxed text-amber-800 dark:text-amber-100">
              {configHint(config)}
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
                  {config.configured
                    ? `base Supabase${config.realtime ? " (temps reel actif)" : ""}`
                    : "base non configuree"}
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

      {config && !config.configured && (
        <p className="mt-6 rounded-xl border border-rose-500/40 bg-rose-500/10 px-4 py-3 text-sm leading-relaxed text-rose-700 dark:text-rose-200">
          La base de donnees n&apos;est pas configuree : l&apos;application ne peut pas fonctionner.
          Variables manquantes : <strong>{config.missing.join(", ")}</strong>. Ajoutez-les dans les
          variables d&apos;environnement de votre hebergeur, puis relancez un deploiement.
        </p>
      )}

      <section className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Metric label="Joueurs" value={stats?.totalPlayers ?? 0} accent />
        <Metric label="En jeu" value={stats?.playing ?? 0} />
        <Metric label="Termines" value={stats?.finished ?? 0} />
        <Metric label="Score moyen" value={stats?.averageScore ?? 0} />
      </section>

      <div className="mt-8 grid gap-8 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <section className="space-y-8">
          <GameSettingsPanel />

          <div>
            <h2 className="mb-3 text-xl font-bold">Classement general</h2>
            <Leaderboard entries={entries} compact />
          </div>
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

/**
 * Reglage des categories : nombre de questions servies par partie et
 * activation. Les modifications s'appliquent aux parties lancees ensuite ;
 * les parties deja en cours conservent leur nombre de questions initial.
 */
function GameSettingsPanel() {
  const [games, setGames] = useState<Game[] | null>(null);
  const [limits, setLimits] = useState({ min: 1 });
  const [drafts, setDrafts] = useState<Record<string, string>>({});
  const [saving, setSaving] = useState<string | null>(null);
  const [saved, setSaved] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/admin/games", { cache: "no-store" })
      .then(async (response) => {
        const payload = await response.json();
        if (!response.ok || !payload.games) {
          throw new Error(payload.error ?? "Impossible de charger les categories.");
        }
        setGames(payload.games);
        setLimits(payload.limits ?? { min: 1 });
        setDrafts(
          Object.fromEntries(
            (payload.games as Game[]).map((game) => [game.slug, String(game.questionsPerSession)]),
          ),
        );
      })
      .catch((cause) => {
        // Sans cela, le panneau resterait bloque sur un chargement perpetuel.
        setGames([]);
        setError(cause instanceof Error ? cause.message : "Impossible de charger les categories.");
      });
  }, []);

  async function save(slug: string, patch: { questionsPerSession?: number; isActive?: boolean }) {
    setSaving(slug);
    setError(null);
    setNotice(null);
    try {
      const response = await fetch("/api/admin/games", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ slug, ...patch }),
      });
      const payload = await response.json();
      if (!response.ok) throw new Error(payload.error ?? "Reglage impossible.");

      const updated = payload.game as Game;
      if (payload.notice) setNotice(payload.notice as string);
      setGames((current) =>
        (current ?? []).map((game) => (game.slug === slug ? updated : game)),
      );
      setDrafts((current) => ({ ...current, [slug]: String(updated.questionsPerSession) }));
      setSaved(slug);
      window.setTimeout(() => setSaved((value) => (value === slug ? null : value)), 2000);
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Reglage impossible.");
      // On restaure la valeur enregistree pour ne pas laisser un brouillon trompeur.
      const known = games?.find((game) => game.slug === slug);
      if (known) setDrafts((current) => ({ ...current, [slug]: String(known.questionsPerSession) }));
    } finally {
      setSaving(null);
    }
  }

  function commit(game: Game) {
    const raw = Number(drafts[game.slug]);
    if (!Number.isFinite(raw) || raw === game.questionsPerSession) {
      setDrafts((current) => ({ ...current, [game.slug]: String(game.questionsPerSession) }));
      return;
    }
    void save(game.slug, { questionsPerSession: raw });
  }

  if (!games) {
    return (
      <div className="card animate-pulse p-6 text-sm text-faint">Chargement des categories...</div>
    );
  }

  if (games.length === 0) {
    return (
      <div>
        <h2 className="mb-1 text-xl font-bold">Reglage des defis</h2>
        <p className="rounded-xl border border-rose-500/40 bg-rose-500/10 px-4 py-3 text-sm leading-relaxed text-rose-700 dark:text-rose-200">
          {error ?? "Aucune categorie n'est disponible."}
        </p>
      </div>
    );
  }

  return (
    <div>
      <h2 className="mb-1 text-xl font-bold">Reglage des defis</h2>
      <p className="mb-3 text-sm text-muted">
        Nombre de questions servies par partie. Le seul plafond est la taille de la banque de la
        categorie. La modification s&apos;applique aux parties lancees ensuite ; celles deja en
        cours ne changent pas.
      </p>

      {games.some((game) => game.questionCount === 0) && (
        <p className="mb-3 rounded-xl border border-rose-500/40 bg-rose-500/10 px-4 py-3 text-sm leading-relaxed text-rose-700 dark:text-rose-200">
          Une ou plusieurs categories n&apos;ont aucune question en base : les joueurs ne pourront
          pas y jouer. Lancez l&apos;import depuis le projet, avec les variables Supabase
          renseignees : <code className="font-mono">npm run db:import</code> (puis
          <code className="font-mono"> npm run db:check</code> pour verifier).
        </p>
      )}

      {notice && (
        <p className="mb-3 rounded-xl border border-amber-400/40 bg-amber-400/10 px-4 py-2 text-sm text-amber-800 dark:text-amber-100">
          {notice}
        </p>
      )}

      {error && (
        <p role="alert" className="mb-3 rounded-xl border border-rose-500/40 bg-rose-500/10 px-4 py-2 text-sm text-rose-700 dark:text-rose-200">
          {error}
        </p>
      )}

      <ul className="space-y-2">
        {games.map((game) => (
          <li key={game.slug} className="card flex flex-wrap items-center gap-4 p-4">
            <span className="text-2xl" aria-hidden>
              {game.emoji}
            </span>
            <span className="min-w-0 flex-1">
              <span className="block font-bold">{game.name}</span>
              {game.questionCount === 0 ? (
                <span className="block text-xs font-semibold text-rose-700 dark:text-rose-300">
                  banque vide : aucune question importee
                </span>
              ) : (
                <span className="block text-xs text-faint">
                  banque de {game.questionCount.toLocaleString("fr-FR")} questions &middot; maximum
                  reglable : {game.questionCount.toLocaleString("fr-FR")}
                </span>
              )}
            </span>

            <label className="flex items-center gap-2 text-sm">
              <span className="text-muted">Questions</span>
              <input
                type="number"
                inputMode="numeric"
                min={limits.min}
                max={game.questionCount || undefined}
                value={drafts[game.slug] ?? ""}
                disabled={saving === game.slug}
                onChange={(event) =>
                  setDrafts((current) => ({ ...current, [game.slug]: event.target.value }))
                }
                onBlur={() => commit(game)}
                onKeyDown={(event) => {
                  if (event.key === "Enter") event.currentTarget.blur();
                }}
                aria-label={`Nombre de questions par partie pour ${game.name}`}
                className="w-20 rounded-lg border border-line bg-surface px-3 py-2 text-center font-bold tabular-nums text-fg outline-none focus:border-mit-500"
              />
            </label>

            <button
              type="button"
              onClick={() => void save(game.slug, { isActive: !game.isActive })}
              disabled={saving === game.slug}
              className={[
                "rounded-full border px-3 py-1.5 text-xs font-semibold transition",
                game.isActive
                  ? "border-emerald-500/50 bg-emerald-500/10 text-emerald-700 dark:text-emerald-300"
                  : "border-line text-faint hover:text-muted",
              ].join(" ")}
              aria-pressed={game.isActive}
            >
              {game.isActive ? "Proposee aux joueurs" : "Masquee"}
            </button>

            <span className="w-20 text-right text-xs text-emerald-700 dark:text-emerald-300">
              {saved === game.slug ? "Enregistre" : saving === game.slug ? "..." : ""}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}
