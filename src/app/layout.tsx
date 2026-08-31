import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MIT Entrepreneur Challenge",
  description:
    "Quiz web temps reel : business, innovation et culture camerounaise. Scannez le QR code et jouez depuis votre navigateur.",
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#f4f6fb" },
    { media: "(prefers-color-scheme: dark)", color: "#070b18" },
  ],
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
};

/**
 * Applique le theme avant le premier rendu pour eviter le clignotement blanc.
 * Le theme sombre reste le defaut : c'est celui pensé pour la projection.
 */
const THEME_SCRIPT = `
(function () {
  try {
    var stored = localStorage.getItem("mit-theme");
    var dark = stored ? stored === "dark" : true;
    document.documentElement.classList.toggle("dark", dark);
    document.documentElement.style.colorScheme = dark ? "dark" : "light";
  } catch (e) {
    document.documentElement.classList.add("dark");
  }
})();
`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" className="dark" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: THEME_SCRIPT }} />
      </head>
      <body className="min-h-screen">{children}</body>
    </html>
  );
}
