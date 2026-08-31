"use client";

import { useEffect, useState } from "react";

export type Theme = "light" | "dark";

export const THEME_KEY = "mit-theme";

function apply(theme: Theme) {
  document.documentElement.classList.toggle("dark", theme === "dark");
  document.documentElement.style.colorScheme = theme;
}

/**
 * Bascule entre le theme sombre (par defaut, pensé pour la projection en salle)
 * et le theme clair. Le choix est conserve dans le navigateur et applique avant
 * le premier rendu par le script de app/layout.tsx, pour eviter tout clignotement.
 */
export function ThemeToggle({ className = "" }: { className?: string }) {
  const [theme, setTheme] = useState<Theme>("dark");
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    const current = document.documentElement.classList.contains("dark") ? "dark" : "light";
    setTheme(current);
    setMounted(true);
  }, []);

  function toggle() {
    const next: Theme = theme === "dark" ? "light" : "dark";
    setTheme(next);
    apply(next);
    try {
      window.localStorage.setItem(THEME_KEY, next);
    } catch {
      /* navigation privee : le choix ne sera simplement pas memorise */
    }
  }

  const isDark = theme === "dark";
  const label = isDark ? "Passer au theme clair" : "Passer au theme sombre";

  return (
    <button
      type="button"
      onClick={toggle}
      title={label}
      aria-label={label}
      aria-pressed={isDark}
      className={[
        "group inline-flex items-center gap-2 rounded-full border border-line bg-surface",
        "px-3 py-1.5 text-xs font-semibold text-muted backdrop-blur-sm transition",
        "hover:border-accent-line hover:bg-surface-hover hover:text-accent",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-mit-400/40",
        className,
      ].join(" ")}
    >
      <span aria-hidden className="text-sm leading-none">
        {mounted ? (isDark ? "☀️" : "\u{1F319}") : "\u{1F319}"}
      </span>
      <span>{mounted ? (isDark ? "Mode clair" : "Mode sombre") : "Theme"}</span>
    </button>
  );
}
