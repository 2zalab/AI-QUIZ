import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        // Jetons semantiques : leur valeur change avec le theme clair / sombre
        // (voir les variables CSS de globals.css).
        canvas: "var(--canvas)",
        fg: "var(--fg)",
        muted: "var(--muted)",
        faint: "var(--faint)",
        surface: {
          DEFAULT: "var(--surface)",
          hover: "var(--surface-hover)",
          soft: "var(--surface-soft)",
        },
        chip: "var(--chip)",
        line: {
          DEFAULT: "var(--line)",
          strong: "var(--line-strong)",
        },
        accent: {
          DEFAULT: "var(--accent)",
          soft: "var(--accent-soft)",
          line: "var(--accent-line)",
        },
        ink: {
          950: "#070b18",
          900: "#0b1024",
          800: "#131a35",
          700: "#1d2649",
          600: "#2b3765",
        },
        // Bleu MIT : couleur d'accent principale de l'application.
        mit: {
          300: "#a9cdff",
          400: "#7ab5ff",
          500: "#2f80ed",
          600: "#1b5fc1",
          700: "#14458f",
        },
        brand: {
          400: "#5eead4",
          500: "#22c8b0",
          600: "#12a695",
        },
      },
      fontFamily: {
        display: ["var(--font-display)", "system-ui", "sans-serif"],
      },
      animation: {
        "pulse-slow": "pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        "fade-up": "fadeUp .45s ease-out both",
        "pop": "pop .35s cubic-bezier(.2,1.3,.5,1) both",
        "shine": "shine 2.5s linear infinite",
      },
      keyframes: {
        fadeUp: {
          "0%": { opacity: "0", transform: "translateY(12px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        pop: {
          "0%": { opacity: "0", transform: "scale(.9)" },
          "100%": { opacity: "1", transform: "scale(1)" },
        },
        shine: {
          "0%": { backgroundPosition: "-200% center" },
          "100%": { backgroundPosition: "200% center" },
        },
      },
    },
  },
  plugins: [],
};

export default config;
