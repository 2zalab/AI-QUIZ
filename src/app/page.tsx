import Link from "next/link";

const ENTRIES = [
  {
    href: "/display",
    emoji: "\u{1F4FA}",
    title: "Ecran public",
    description: "QR code d'acces et classement en direct, a projeter sur grand ecran.",
  },
  {
    href: "/join",
    emoji: "\u{1F4F1}",
    title: "Rejoindre le defi",
    description: "Entrez votre nom, choisissez votre categorie et jouez depuis votre navigateur.",
  },
  {
    href: "/admin",
    emoji: "\u{1F3AE}",
    title: "Espace organisateur",
    description: "Suivi des participants, statistiques et remise a zero du classement.",
  },
];

export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-screen max-w-5xl flex-col justify-center px-6 py-16">
      <p className="badge w-fit bg-gold-400/15 text-gold-400">Business &middot; Innovation &middot; Cameroun</p>
      <h1 className="mt-5 text-5xl font-black leading-tight sm:text-6xl">
        <span className="title-shine">iCLAN Entrepreneur Challenge</span>
      </h1>
      <p className="mt-5 max-w-2xl text-lg text-slate-300">
        Un quiz de competition en temps reel. Les participants scannent un QR code, jouent depuis
        leur telephone, et le classement se met a jour instantanement sur l&apos;ecran de la salle.
        Aucune application a installer.
      </p>

      <div className="mt-12 grid gap-5 sm:grid-cols-3">
        {ENTRIES.map((entry) => (
          <Link
            key={entry.href}
            href={entry.href}
            className="card group p-6 transition hover:-translate-y-1 hover:border-gold-400/40"
          >
            <div className="text-4xl">{entry.emoji}</div>
            <h2 className="mt-4 text-xl font-bold group-hover:text-gold-400">{entry.title}</h2>
            <p className="mt-2 text-sm leading-relaxed text-slate-400">{entry.description}</p>
          </Link>
        ))}
      </div>

      <p className="mt-12 text-sm text-slate-500">
        4 categories &middot; 4 000 questions &middot; 3 niveaux de difficulte (100, 200 et 300 points)
      </p>
    </main>
  );
}
