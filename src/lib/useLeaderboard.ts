"use client";

import { useEffect, useRef, useState } from "react";
import type { LeaderboardEntry, Stats } from "./types";

export interface LiveData {
  entries: LeaderboardEntry[];
  stats: Stats | null;
  connected: boolean;
}

const EMPTY: LiveData = { entries: [], stats: null, connected: false };

/**
 * Classement en direct.
 *
 * Le flux principal est un canal Server-Sent Events maintenu par le serveur : il
 * fonctionne aussi bien avec Supabase qu'en mode demonstration. Quand Supabase
 * Realtime est configure, on s'y abonne en plus pour declencher un
 * rafraichissement immediat des qu'une ligne de la table players change.
 */
export function useLeaderboard(): LiveData {
  const [data, setData] = useState<LiveData>(EMPTY);
  const refreshRef = useRef<() => void>(() => {});

  useEffect(() => {
    let cancelled = false;

    const refresh = async () => {
      try {
        const response = await fetch("/api/leaderboard?limit=20", { cache: "no-store" });
        if (!response.ok) return;
        const payload = await response.json();
        if (!cancelled) {
          setData({ entries: payload.entries, stats: payload.stats, connected: true });
        }
      } catch {
        /* le flux SSE prendra le relais */
      }
    };
    refreshRef.current = refresh;
    void refresh();

    const source = new EventSource("/api/leaderboard/stream");
    source.addEventListener("leaderboard", (event) => {
      const payload = JSON.parse((event as MessageEvent).data);
      if (!cancelled) {
        setData({ entries: payload.entries, stats: payload.stats, connected: true });
      }
    });
    source.addEventListener("error", () => {
      if (!cancelled) setData((current) => ({ ...current, connected: false }));
    });

    return () => {
      cancelled = true;
      source.close();
    };
  }, []);

  // Abonnement Supabase Realtime optionnel : reactions instantanees sur players.
  useEffect(() => {
    const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
    const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
    if (!url || !key) return;

    let cleanup = () => {};
    let active = true;

    void (async () => {
      const { createClient } = await import("@supabase/supabase-js");
      if (!active) return;
      const client = createClient(url, key, { auth: { persistSession: false } });
      const channel = client
        .channel("classement-live")
        .on("postgres_changes", { event: "*", schema: "public", table: "players" }, () => {
          refreshRef.current();
        })
        .subscribe();
      cleanup = () => {
        void client.removeChannel(channel);
      };
    })();

    return () => {
      active = false;
      cleanup();
    };
  }, []);

  return data;
}
