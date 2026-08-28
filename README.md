# 🏆 iCLAN Entrepreneur Challenge

Quiz de competition **temps reel**, joue directement dans le navigateur du
telephone. L'organisateur projette un ecran avec un QR code, les participants
le scannent, entrent leur nom, choisissent un defi et jouent. Le classement se
met a jour en direct sur le grand ecran. **Aucune application a installer.**

> Business &middot; Innovation &middot; Culture camerounaise — 4 categories, 4 000 questions.

---

## Sommaire

- [Principe](#principe)
- [Les trois interfaces](#les-trois-interfaces)
- [Categories et questions](#categories-et-questions)
- [Systeme de score](#systeme-de-score)
- [Demarrage](#demarrage)
- [Mise en place avec Supabase](#mise-en-place-avec-supabase)
- [Deploiement](#deploiement-sur-vercel)
- [Le jour de l'evenement](#le-jour-de-levenement)
- [Anti-triche](#anti-triche)
- [Architecture](#architecture)
- [Variables d'environnement](#variables-denvironnement)
- [Commandes](#commandes)

---

## Principe

```
                    ORGANISATEUR
                         │
                 ┌───────┴────────┐
                 │  /display      │   Ecran / videoprojecteur
                 │  QR + classement│
                 └───────┬────────┘
                         │  scan
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    Joueur 1         Joueur 2         Joueur 3      (navigateur mobile)
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                 /join  →  /game/:code
                         │
                         ▼
              API Next.js  (verification + score)
                         │
                 ┌───────┴────────┐
                 │   Supabase     │  PostgreSQL + Realtime
                 └───────┬────────┘
                         ▼
              Classement live → /display
```

---

## Les trois interfaces

| Route | Pour qui | Role |
| --- | --- | --- |
| `/display` | Ecran de la salle | QR code d'acces, classement en direct, participation par defi, statuts des joueurs |
| `/join` puis `/game/:code` | Participants | Saisie du nom, choix du defi, questions chronometrees, resultat final |
| `/admin` | Organisateur | Reglage du nombre de questions par defi, activation des categories, statistiques, classement, lien et QR de participation, remise a zero entre deux manches |

Le theme choisi sur la page d'accueil s'applique partout (voir ci-dessous).

`/` est une page d'accueil qui renvoie vers les trois.

### Theme clair / sombre

Un bouton en haut de la page d'accueil bascule entre le **theme sombre**
(par defaut, pensé pour la projection en salle) et un **theme clair**, utile
sur un videoprojecteur peu contraste ou en plein jour. Le choix est memorise
dans le navigateur et s'applique a toutes les pages, y compris `/display`,
`/game/:code` et `/admin`. Il est reapplique avant le premier rendu, sans
clignotement au chargement.

---

## Categories et questions

| Categorie | Contenu |
| --- | --- |
| 💼 **Entrepreneuriat** | Notions cles, mises en situation, cas chiffres (marge, seuil de rentabilite, TVA, ROI), marketing, financement, droit OHADA, figures de l'entrepreneuriat africain et mondial |
| 🇨🇲 **Cameroun** | 10 regions et 58 departements, histoire, institutions, personnalites, gastronomie, economie, musique, sport, expressions populaires |
| 💡 **Innovation & IA** | L'IA et le numerique au quotidien, usages concrets en PME, cybersecurite, metiers et outils, ecosysteme tech africain |
| 🎯 **Challenge Mixte** | Tirage equilibre des trois categories precedentes |

**1 000 questions par categorie**, soit 4 000 au total, dans `data/`.
Voir [`data/README.md`](data/README.md) pour le format et la procedure d'ajout.

Les questions restent volontairement **accessibles** : pas de technique pointue,
mais du raisonnement entrepreneurial, de la culture generale et des mises en
situation concretes.

---

## Systeme de score

| Difficulte | Points de base | Temps imparti |
| --- | --- | --- |
| 🟢 Facile | 100 | 20 s |
| 🟠 Moyen | 200 | 25 s |
| 🔴 Challenge | 300 | 30 s |

S'ajoute un **bonus de rapidite** pouvant atteindre 50 % des points de base,
proportionnel au temps restant. Repondre juste en 5 secondes a une question
« challenge » rapporte donc jusqu'a 450 points ; repondre juste au buzzer en
rapporte 300. Une mauvaise reponse ou un temps ecoule rapporte 0.

Chaque partie sert **10 questions par defaut** (4 faciles, 4 moyennes,
2 challenge), tirees au hasard et servies de la plus facile a la plus difficile.

Ce nombre se regle **categorie par categorie depuis `/admin`**, sans plafond
arbitraire : une manche courte de 5 questions pour un passage rapide, une finale
de 20 pour departager, ou davantage. La seule limite est la taille de la banque
de la categorie (1 000 questions) ; une valeur superieure est automatiquement
ramenee a ce maximum, et l'interface le signale. La repartition des difficultes est adaptee proportionnellement. Le
reglage s'applique aux parties lancees ensuite ; celles deja en cours gardent
leur nombre de questions initial. Chaque categorie peut aussi etre **masquee**,
elle disparait alors de la page de participation.

---

## Demarrage

Supabase est **obligatoire** : il n'existe pas de mode de repli. Une application
qui parait fonctionner mais perd tous les scores au moindre redemarrage serait
plus dangereuse qu'une erreur franche.

```bash
npm install
cp .env.example .env.local   # puis renseignez les cles Supabase
npm run db:check             # verifie que le projet est pret
npm run dev
```

Puis ouvrez :

- l'ecran public : <http://localhost:3000/display>
- l'interface joueur : <http://localhost:3000/join>
- l'espace organisateur : <http://localhost:3000/admin>

Si les variables manquent, chaque page l'indique explicitement et nomme les
variables absentes, plutot que d'afficher un jeu vide.

Pour que les telephones du reseau wifi local atteignent le serveur, indiquez
l'adresse IP de la machine :

```bash
NEXT_PUBLIC_APP_URL=http://192.168.1.24:3000 npm run dev
```

---

## Mise en place avec Supabase

1. **Creer un projet** sur [supabase.com](https://supabase.com).

2. **Executer les scripts SQL** dans l'editeur SQL du projet, dans cet ordre :

   | Fichier | Role |
   | --- | --- |
   | `supabase/schema.sql` | Tables, index, vue `leaderboard`, activation du temps reel |
   | `supabase/policies.sql` | Politiques RLS (voir [Anti-triche](#anti-triche)) |
   | `supabase/seed_games.sql` | L'evenement et les quatre categories |

3. **Renseigner les variables** dans `.env.local` (voir `.env.example`) :

   ```bash
   cp .env.example .env.local
   ```

   Les cles se trouvent dans *Project Settings → API*.

4. **Importer les questions** — etape indispensable, souvent oubliee :

   ```bash
   npm run questions:generate   # si data/ est vide
   npm run db:import            # 4 000 questions vers Supabase
   ```

   Renseigner les variables d'environnement ne suffit pas : sans cet import,
   la table `questions` reste vide et les joueurs voient le message
   « Aucune question n'a encore ete importee pour ce defi ».

5. **Verifier** : `npm run db:check`. Le script controle les variables, la
   connexion, les tables, les quatre categories, le nombre de questions
   importees et l'etancheite des politiques RLS.

6. **Demarrer** : `npm run dev`. L'espace organisateur affiche desormais
   « stockage : Supabase ».

---

## Deploiement sur Vercel

1. Poussez le depot sur GitHub, puis importez-le dans Vercel.
2. Dans **Settings > Environment Variables**, ajoutez les memes variables que
   dans `.env.local`, en definissant `NEXT_PUBLIC_APP_URL` sur l'URL de
   production : c'est elle qui sera encodee dans le QR code. Ne prefixez jamais
   `SUPABASE_SERVICE_ROLE_KEY` ni `ADMIN_PASSWORD` par `NEXT_PUBLIC_`, ce
   prefixe exposerait la valeur au navigateur.
3. **Redeployez** : les variables ne s'appliquent qu'aux nouveaux deploiements,
   celui deja en ligne conserve les anciennes valeurs.
4. Les questions vivent dans Supabase, pas dans le code deploye : l'import
   (`npm run db:import`) se lance depuis votre machine et n'a a etre fait
   qu'une fois. Verifiez avec `npm run db:check`.

### Le deploiement fonctionne mais aucune question n'apparait

Ouvrez `https://votre-projet.vercel.app/api/config` : cette page indique, sans
rien reveler de secret, le mode de stockage actif, les variables que le
deploiement voit reellement et le nombre de questions accessibles par categorie.

| Ce que vous lisez | Ce que cela signifie |
| --- | --- |
| `"configured": false` | les variables nommees dans `missing` ne sont pas arrivees jusqu'a l'application : verifiez qu'elles sont bien dans **Vercel > Settings > Environment Variables** (et non dans le tableau de bord Supabase), pour l'environnement Production, puis **redeployez** |
| `SUPABASE_SERVICE_ROLE_KEY: false` | la cle de service manque : c'est elle qui autorise le serveur a lire les bonnes reponses. Sans elle, rien ne fonctionne |
| `"configured": true` et `banks` a 0 | la table `questions` est vide : lancez `npm run db:import` depuis votre machine, puis `npm run db:check` |

Rappel : les variables d'environnement ne s'appliquent qu'aux **nouveaux**
deploiements. Apres les avoir ajoutees, relancez un deploiement.

---

## Le jour de l'evenement

1. Ouvrir `/display` sur l'ordinateur relie au videoprojecteur, en plein ecran.
2. Le QR code s'affiche : les participants le scannent avec l'appareil photo.
3. Chacun saisit son nom, choisit son defi et joue ses 10 questions.
4. Le classement se met a jour en direct sur l'ecran, sans rafraichissement.
5. Entre deux manches, l'organisateur remet le classement a zero depuis `/admin`.

Prevoir un **repli** : la page `/join` fonctionne aussi si un participant tape
l'adresse a la main (elle est affichee sous le QR code).

---

## Anti-triche

Le jeu part du principe qu'un participant peut ouvrir la console de son
navigateur. Trois protections repondent a ce risque.

**1. Les bonnes reponses ne quittent jamais le serveur.**
La charge utile envoyee au navigateur pour une question contient uniquement
l'enonce, les quatre options, la difficulte, les points et l'echeance :

```json
{ "id": "cmr-0042", "index": 3, "total": 10, "difficulty": "moyen",
  "question": "...", "options": { "A": "...", "B": "...", "C": "...", "D": "..." },
  "points": 200, "timeLimit": 25, "deadlineAt": 1730000000000 }
```

La colonne `correct_answer` n'apparait qu'apres la reponse, avec l'explication.

**2. Le score est calcule cote serveur.**
Le navigateur envoie seulement `{ questionId, answer }`. Le serveur retrouve la
question, compare, calcule le bonus de rapidite a partir de l'horodatage de
service qu'il a lui-meme enregistre, et met a jour le score. Un score envoye
depuis le client serait purement et simplement ignore.

**3. Les politiques RLS ferment les tables sensibles.**
Avec `supabase/policies.sql`, le role anonyme ne peut lire que `games` et
`players` (nom, score, statut — rien de confidentiel, c'est ce qui alimente le
classement en direct). Les tables `questions`, `player_questions` et `answers`
n'ont **aucune politique** : sous RLS, elles sont donc inaccessibles depuis le
navigateur. Les routes API utilisent la cle de service, qui reste cote serveur.

En complement, le serveur refuse une reponse a une question hors sequence ou
deja repondue (pas de rejeu), et applique le temps imparti avec une tolerance
reseau de 1,5 seconde.

---

## Architecture

```
src/
├── app/
│   ├── page.tsx                    Accueil
│   ├── display/                    Ecran public (QR + classement live)
│   ├── join/                       Saisie du nom et choix du defi
│   ├── game/[code]/                Deroulement de la partie
│   ├── admin/                      Espace organisateur
│   └── api/
│       ├── games/                  Categories actives
│       ├── join/                   Creation d'une partie
│       ├── game/[code]/            Etat de la partie + service des questions
│       ├── game/[code]/answer/     Verification et calcul du score
│       ├── leaderboard/            Classement + statistiques
│       ├── leaderboard/stream/     Flux Server-Sent Events du classement
│       ├── qr/                     QR code SVG
│       └── admin/                  Authentification, reglage des defis, remise a zero
├── components/
│   ├── Leaderboard.tsx
│   └── ThemeToggle.tsx             Bascule clair / sombre (jetons CSS)
└── lib/
    ├── config.ts                   Categories, quotas de difficulte
    ├── scoring.ts                  Calcul des points et bonus de rapidite
    ├── useLeaderboard.ts           Classement live (SSE + Supabase Realtime)
    └── store/
        ├── index.ts                Interface commune, controle de configuration
        ├── supabase.ts             Implementation PostgreSQL
        └── questions.ts            Tirage des questions d'une partie

scripts/
├── qgen/                           Banques thematiques de questions (Python)
├── generate_questions.py           Generation des CSV
├── check_questions.py              Controle qualite des CSV
└── import-questions.mjs            Import des CSV vers Supabase

supabase/
├── schema.sql                      Tables, vue leaderboard, temps reel
├── policies.sql                    Politiques RLS
└── seed_games.sql                  Evenement et categories
```

### Le classement en direct

Deux mecanismes se completent :

- un flux **Server-Sent Events** (`/api/leaderboard/stream`) que le serveur
  alimente des qu'un score change — il fonctionne dans les deux modes de
  stockage et le navigateur se reconnecte automatiquement ;
- un abonnement **Supabase Realtime** sur la table `players`, active des que les
  cles publiques sont presentes, qui declenche un rafraichissement immediat.

---

## Variables d'environnement

| Variable | Obligatoire | Role |
| --- | --- | --- |
| `NEXT_PUBLIC_APP_URL` | recommande | Adresse encodee dans le QR code |
| `NEXT_PUBLIC_SUPABASE_URL` | **oui** | URL du projet |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | recommande | Active Supabase Realtime cote client |
| `SUPABASE_SERVICE_ROLE_KEY` | **oui** | Cle serveur — **ne jamais exposer au client** |
| `ADMIN_PASSWORD` | recommande | Acces a `/admin` (defaut : `iclan2026`) |
| `QUESTIONS_PER_SESSION` | non | Valeur initiale du nombre de questions par partie (defaut : 10). Une fois l'application lancee, le reglage se fait depuis `/admin` |

Sans `NEXT_PUBLIC_SUPABASE_URL` **et** `SUPABASE_SERVICE_ROLE_KEY`, l'application
refuse de servir les parties et affiche les variables manquantes sur chaque
ecran. C'est volontaire : aucun repli silencieux.

---

## Commandes

```bash
npm run dev                  # serveur de developpement
npm run build                # build de production
npm run start                # serveur de production
npm run typecheck            # verification TypeScript
npm run questions:generate   # regenere les 4 CSV de questions
npm run questions:check      # controle qualite des CSV
npm run db:check             # verifie le projet Supabase (tables, questions, RLS)
npm run db:import            # importe les CSV dans Supabase
```

---

## Pile technique

Next.js 15 (App Router) &middot; React 19 &middot; TypeScript &middot; Tailwind CSS
&middot; Supabase (PostgreSQL + Realtime) &middot; Server-Sent Events &middot;
generation des questions en Python.
