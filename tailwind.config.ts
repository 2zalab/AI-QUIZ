import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        ink: {
          950: "#070b18",
          900: "#0b1024",
          800: "#131a35",
          700: "#1d2649",
          600: "#2b3765",
        },
        gold: {
          400: "#ffd166",
          500: "#f4b93e",
          600: "#d9971a",
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
