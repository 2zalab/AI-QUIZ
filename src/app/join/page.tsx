import { JoinForm } from "./JoinForm";

export const dynamic = "force-dynamic";

export default function JoinPage() {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-xl flex-col px-5 py-10">
      <header className="text-center">
        <p className="badge mx-auto w-fit bg-brand-400/15 text-brand-400">iCLAN Challenge</p>
        <h1 className="mt-4 text-3xl font-black leading-tight">
          <span className="title-shine">Bienvenue au defi</span>
        </h1>
        <p className="mt-2 text-sm text-slate-400">
          Entrez votre nom, choisissez votre categorie et lancez la partie.
        </p>
      </header>
      <JoinForm />
    </main>
  );
}
