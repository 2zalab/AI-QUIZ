import QRCode from "qrcode";
import { appUrl } from "@/lib/config";

export const dynamic = "force-dynamic";

/** QR code SVG pointant vers la page de participation, pour l'ecran public. */
export async function GET(request: Request) {
  const url = new URL(request.url);
  const target = url.searchParams.get("url") ?? `${appUrl()}/join`;

  const svg = await QRCode.toString(target, {
    type: "svg",
    errorCorrectionLevel: "M",
    margin: 1,
    width: 512,
    color: { dark: "#070b18", light: "#ffffff" },
  });

  return new Response(svg, {
    headers: {
      "Content-Type": "image/svg+xml; charset=utf-8",
      "Cache-Control": "public, max-age=60",
    },
  });
}
