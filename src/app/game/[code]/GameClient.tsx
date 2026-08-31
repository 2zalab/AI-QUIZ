"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { Leaderboard } from "@/components/Leaderboard";
import { useLeaderboard } from "@/lib/useLeaderboard";
import type { AnswerResult, Letter, SessionState } from "@/lib/types";

const LETTERS: Letter[] = ["A", "B", "C", "D"];

const DIFFICULTY_LABEL: Record<string, { label: string; className: string }> = {
  facile: { label: "Facile", className: "bg-emerald-400/15 text-emerald-700 dark:text-emerald-300" },
  moyen: { label: "Moyen", className: "bg-amber-400/15 text-amber-700 dark:text-amber-300" },
  challenge: { label: "Challenge", className: "bg-rose-400/15 text-rose-700 dark:text-rose-300" },
};

export function GameClient({ sessionCode }: { sessionCode: string }) {
  const [state, setState] = useState<SessionState | null>(null);
  const [result, setResult] = useState<AnswerResult | null>(null);
  const [chosen, setChosen] = useState<Letter | null>(null);
  const [remaining, setRemaining] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const submittedFor = useRef<string | null>(null);
  const resultRef = useRef<HTMLDivElement | null>(null);

  const loadState = useCallback(async () => {
    try {
      const response = await fetch(`/api/game/${sessionCode}`, { cache: "no-store" });
      if (response.status === 404) {
        setError("Cette session n'existe plus. Rejoignez le defi a nouveau.");
        return;
      }
      const payload: SessionState = await response.json();
      setState(payload);
      setResult(null);
      setChosen(null);
      submittedFor.current = null;
    } catch {
      setError("Connexion perdue. Verifiez votre reseau.");
    }
  }, [sessionCode]);

  useEffect(() => {
    void loadState();
  }, [loadState]);

  const submit = useCallback(
    async (answer: Letter | null) => {
      const question = state?.question;
      if (!question || busy || submittedFor.current === question.id) return;
      submittedFor.current = question.id;
      setBusy(true);
      setChosen(answer);
      try {
        const response = await fetch(`/api/game/${sessionCode}/answer`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ questionId: question.id, answer }),
        });
        const payload = await response.json();
        if (!response.ok) throw new Error(payload.error ?? "Reponse refusee.");
        setResult(payload as AnswerResult);
      } catch (cause) {
        setError(cause instanceof Error ? cause.message : "Reponse refusee.");
        submittedFor.current = null;
      } finally {
        setBusy(false);
      }
    },
    [busy, sessionCode, state?.question],
  );

  // Amene automatiquement le retour de reponse dans le champ de vision.
  useEffect(() => {
    if (result) resultRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [result]);

  // Compte a rebours pilote par l'echeance calculee par le serveur.
  useEffect(() => {
    const question = state?.question;
    if (!question || result) return;

    const tick = () => {
      const left = Math.max(0, question.deadlineAt - Date.now());
      setRemaining(left);
      if (left === 0) void submit(null);
    };
    tick();
    const timer = setInterval(tick, 200);
    return () => clearInterval(timer);
  }, [state?.question, result, submit]);

  if (error) {
    return (
      <Centered>
        <p className="text-5xl">{"⚠️"}</p>
        <p className="mt-4 text-lg font-semibold">{error}</p>
        <Link href="/join" className="btn-primary mt-6">
          Revenir a l&apos;accueil
        </Link>
      </Centered>
    );
  }

  if (!state) {
    return (
      <Centered>
        <p className="animate-pulse text-lg text-muted">Preparation de votre partie...</p>
      </Centered>
    );
  }

  if (state.finished && !state.question) {
    return <FinalScreen state={state} />;
  }

  const question = state.question;
  if (!question) {
    return (
      <Centered>
        <p className="animate-pulse text-lg text-muted">Chargement de la question...</p>
      </Centered>
    );
  }

  const seconds = Math.ceil(remaining / 1000);
  const ratio = Math.max(0, Math.min(1, remaining / (question.timeLimit * 1000)));
  const difficulty = DIFFICULTY_LABEL[question.difficulty] ?? DIFFICULTY_LABEL.facile;

  return (
    <main className="mx-auto flex min-h-screen w-full max-w-xl flex-col px-5 py-6">
      <header className="flex items-center justify-between text-sm">
        <span className="font-semibold text-muted">
          Question {question.index}/{question.total}
        </span>
        <span className={`badge ${difficulty.className}`}>
          {difficulty.label} &middot; {question.points} pts
        </span>
      </header>

      <div className="mt-3 h-2 overflow-hidden rounded-full bg-chip" aria-hidden>
        <div
          className="timer-bar h-full rounded-full"
          style={{
            width: `${ratio * 100}%`,
            backgroundColor: ratio > 0.5 ? "#2f80ed" : ratio > 0.25 ? "#f4b93e" : "#f43f5e",
          }}
        />
      </div>
      <p className="mt-2 text-right text-xs tabular-nums text-muted">
        {result ? "Temps arrete" : `${seconds} s restantes`}
      </p>

      <h1 className="mt-6 text-2xl font-bold leading-snug">{question.question}</h1>

      <div className="mt-6 grid gap-3">
        {LETTERS.map((letter) => {
          const isChosen = chosen === letter;
          const isRight = result?.correctAnswer === letter;
          let tone = "border-line bg-surface hover:border-line-strong hover:bg-surface-hover";
          if (result) {
            if (isRight) tone = "border-emerald-400 bg-emerald-400/15";
            else if (isChosen) tone = "border-rose-400 bg-rose-400/15";
            else tone = "border-line bg-surface-soft opacity-60";
          } else if (isChosen) {
            tone = "border-mit-400 bg-accent-soft";
          }

          return (
            <button
              key={letter}
              type="button"
              disabled={Boolean(result) || busy}
              onClick={() => void submit(letter)}
              className={`flex items-center gap-3 rounded-xl border p-4 text-left transition ${tone}`}
            >
              <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-chip font-bold">
                {letter}
              </span>
              <span className="flex-1 leading-snug">{question.options[letter]}</span>
              {result && isRight && <span aria-hidden>{"✅"}</span>}
              {result && isChosen && !isRight && <span aria-hidden>{"❌"}</span>}
            </button>
          );
        })}
      </div>

      {result && (
        <div ref={resultRef} className="mt-6 animate-pop">
          <div
            className={[
              "card p-5",
              result.correct ? "border-emerald-400/40 bg-emerald-400/10" : "border-rose-400/40 bg-rose-400/10",
            ].join(" ")}
          >
            <p className="text-xl font-bold">
              {result.correct ? "✅ Bonne reponse !" : chosen ? "❌ Mauvaise reponse" : "⏱️ Temps ecoule"}
            </p>
            <p className="mt-1 text-3xl font-black text-accent">
              +{result.gained}
              {result.speedBonus > 0 && (
                <span className="ml-2 text-sm font-semibold text-emerald-700 dark:text-emerald-300">
                  dont {result.speedBonus} de rapidite
                </span>
              )}
            </p>
            {result.explanation && (
              <p className="mt-3 text-sm leading-relaxed text-muted">{result.explanation}</p>
            )}
            <div className="mt-4 flex items-center justify-between text-sm">
              <span className="text-muted">
                Score : <strong className="text-fg">{result.score}</strong>
              </span>
              <span className="text-muted">
                Position : <strong className="text-fg">#{result.position}</strong>
              </span>
            </div>
          </div>

          <button type="button" onClick={() => void loadState()} className="btn-primary mt-4 w-full text-lg">
            {result.finished ? "Voir mon resultat" : "Question suivante"}
          </button>
        </div>
      )}
    </main>
  );
}

function FinalScreen({ state }: { state: SessionState }) {
  const { entries } = useLeaderboard();
  const accuracy = state.player.answeredCount
    ? Math.round((state.player.correctCount / state.player.answeredCount) * 100)
    : 0;

  return (
    <main className="mx-auto flex min-h-screen w-full max-w-xl flex-col px-5 py-8">
      <div className="card animate-pop p-7 text-center">
        <p className="text-5xl">{"\u{1F3C6}"}</p>
        <h1 className="mt-3 text-2xl font-black">Bravo {state.player.name} !</h1>
        <p className="mt-1 text-sm text-muted">Defi termine : {state.game.name}</p>

        <p className="mt-6 text-6xl font-black text-accent tabular-nums">
          {state.player.score.toLocaleString("fr-FR")}
        </p>
        <p className="text-sm uppercase tracking-widest text-muted">points</p>

        <div className="mt-6 grid grid-cols-3 gap-3 text-center">
          <Stat label="Position" value={`#${state.position}`} />
          <Stat label="Bonnes reponses" value={`${state.player.correctCount}/${state.player.answeredCount}`} />
          <Stat label="Reussite" value={`${accuracy}%`} />
        </div>
      </div>

      <h2 className="mt-8 text-lg font-bold">Classement en direct</h2>
      <div className="mt-3">
        <Leaderboard entries={entries.slice(0, 10)} highlight={state.player.name} compact />
      </div>

      <Link href="/join" className="btn-ghost mt-6 w-full">
        Relancer un autre defi
      </Link>
    </main>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-line bg-surface p-3">
      <p className="text-xl font-bold tabular-nums">{value}</p>
      <p className="mt-0.5 text-[11px] uppercase tracking-wide text-muted">{label}</p>
    </div>
  );
}

function Centered({ children }: { children: React.ReactNode }) {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center px-6 text-center">
      {children}
    </main>
  );
}
