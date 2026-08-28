"use client";

import type { LeaderboardEntry } from "@/lib/types";

const MEDALS = ["\u{1F947}", "\u{1F948}", "\u{1F949}"];

const STATUS_STYLE: Record<LeaderboardEntry["status"], { dot: string; label: string }> = {
  waiting: { dot: "bg-amber-400", label: "En attente" },
  playing: { dot: "bg-emerald-400", label: "En jeu" },
  finished: { dot: "bg-rose-400", label: "Termine" },
};

const GAME_EMOJI: Record<string, string> = {
  entrepreneuriat: "\u{1F4BC}",
  cameroun: "\u{1F1E8}\u{1F1F2}",
  "innovation-ia": "\u{1F4A1}",
  mixte: "\u{1F3AF}",
};

export function Leaderboard({
  entries,
  highlight,
  compact = false,
}: {
  entries: LeaderboardEntry[];
  highlight?: string;
  compact?: boolean;
}) {
  if (entries.length === 0) {
    return (
      <div className="card flex flex-col items-center gap-3 p-10 text-center">
        <span className="text-5xl">{"\u{1F4E1}"}</span>
        <p className="text-lg font-semibold">En attente des premiers joueurs</p>
        <p className="text-sm text-slate-400">Scannez le QR code pour ouvrir le bal.</p>
      </div>
    );
  }

  return (
    <ol className="space-y-2">
      {entries.map((entry) => {
        const status = STATUS_STYLE[entry.status];
        const isTop = entry.rank <= 3;
        const isMe = highlight && entry.name === highlight;
        return (
          <li
            key={`${entry.rank}-${entry.name}`}
            className={[
              "card flex items-center gap-4 px-4 transition-all duration-300 animate-fade-up",
              compact ? "py-2.5" : "py-3.5",
              isTop ? "border-gold-400/40 bg-gold-400/[0.07]" : "",
              isMe ? "ring-2 ring-brand-400/70" : "",
            ].join(" ")}
          >
            <span
              className={[
                "flex shrink-0 items-center justify-center font-black tabular-nums",
                compact ? "w-9 text-lg" : "w-12 text-2xl",
                isTop ? "text-gold-400" : "text-slate-400",
              ].join(" ")}
            >
              {isTop ? MEDALS[entry.rank - 1] : entry.rank}
            </span>

            <div className="min-w-0 flex-1">
              <p className={compact ? "truncate font-semibold" : "truncate text-xl font-bold"}>
                {entry.name}
              </p>
              <p className="flex items-center gap-2 text-xs text-slate-400">
                <span className={`h-2 w-2 rounded-full ${status.dot}`} aria-hidden />
                {status.label}
                <span aria-hidden>&middot;</span>
                <span>{GAME_EMOJI[entry.gameSlug] ?? ""}</span>
                <span>
                  {entry.correctCount}/{entry.answeredCount} bonnes reponses
                </span>
              </p>
            </div>

            <span
              className={[
                "shrink-0 font-black tabular-nums",
                compact ? "text-lg" : "text-3xl",
                isTop ? "text-gold-400" : "text-slate-100",
              ].join(" ")}
            >
              {entry.score.toLocaleString("fr-FR")}
            </span>
          </li>
        );
      })}
    </ol>
  );
}
