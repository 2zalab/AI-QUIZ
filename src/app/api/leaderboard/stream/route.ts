import { NextResponse } from "next/server";
import { getStore } from "@/lib/store";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

const POLL_INTERVAL_MS = 1000;
const MAX_DURATION_MS = 55_000;

/**
 * Flux Server-Sent Events du classement. Il fonctionne quel que soit le mode de
 * stockage : le serveur surveille une empreinte de l'etat et ne pousse un
 * message que lorsqu'un score change. Le navigateur se reconnecte tout seul.
 */
export async function GET() {
  let store;
  try {
    store = await getStore();
  } catch (error) {
    const message = error instanceof Error ? error.message : "Base de donnees indisponible.";
    return NextResponse.json({ error: message }, { status: 503 });
  }
  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    async start(controller) {
      let closed = false;
      let lastVersion = -1;
      const startedAt = Date.now();

      const send = (event: string, data: unknown) => {
        if (closed) return;
        controller.enqueue(encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`));
      };

      const push = async () => {
        const version = await store.version();
        if (version === lastVersion) return;
        lastVersion = version;
        const [entries, stats] = await Promise.all([
          store.leaderboard({ limit: 20 }),
          store.stats(),
        ]);
        send("leaderboard", { entries, stats, version });
      };

      await push();

      const timer = setInterval(async () => {
        if (closed) return;
        try {
          if (Date.now() - startedAt > MAX_DURATION_MS) {
            send("bye", { reason: "rotation" });
            clearInterval(timer);
            closed = true;
            controller.close();
            return;
          }
          await push();
        } catch {
          clearInterval(timer);
          closed = true;
          try { controller.close(); } catch { /* deja ferme */ }
        }
      }, POLL_INTERVAL_MS);
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
      "X-Accel-Buffering": "no",
    },
  });
}
