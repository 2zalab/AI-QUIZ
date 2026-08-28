/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  eslint: { ignoreDuringBuilds: true },

  /**
   * Le mode demonstration lit les questions dans data/*.csv, avec un chemin
   * construit a l'execution. L'analyse statique de Next.js ne peut donc pas le
   * detecter, et le dossier serait absent du paquet deploye sur un hebergeur
   * sans systeme de fichiers complet (Vercel notamment). On force son inclusion.
   */
  outputFileTracingIncludes: {
    "/api/**/*": ["./data/**/*.csv"],
  },
};

export default nextConfig;
