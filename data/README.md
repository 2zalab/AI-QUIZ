# Banque de questions

Quatre fichiers CSV, **1 000 questions chacun**, generes par
`python3 scripts/generate_questions.py` a partir des banques thematiques de
`scripts/qgen/`.

| Fichier | Categorie | Contenu |
| --- | --- | --- |
| `questions_entrepreneuriat.csv` | Entrepreneuriat | Notions cles, mises en situation, cas chiffres, marketing, financement, droit OHADA, figures de l'entrepreneuriat |
| `questions_cameroun.csv` | Cameroun | Geographie (10 regions, 58 departements), histoire, institutions, personnalites, gastronomie, economie, expressions populaires |
| `questions_innovation_ia.csv` | Innovation & IA | Numerique au quotidien, usages concrets de l'IA en PME, cybersecurite, metiers et outils, ecosysteme tech africain |
| `questions_mixte.csv` | Challenge Mixte | Tirage equilibre des trois categories precedentes |

## Colonnes

| Colonne | Description |
| --- | --- |
| `id` | Identifiant stable (`ent-0001`, `cmr-0001`, `inn-0001`, `mix-0001`) |
| `category` / `category_slug` | Libelle et identifiant technique de la categorie |
| `difficulty` | `facile`, `moyen` ou `challenge` |
| `question` | Enonce |
| `option_a` a `option_d` | Les quatre propositions |
| `correct_answer` | Lettre de la bonne reponse : `A`, `B`, `C` ou `D` |
| `points` | 100 (facile), 200 (moyen), 300 (challenge) |
| `time_limit` | Temps imparti en secondes : 20, 25 ou 30 |
| `explanation` | Phrase affichee au joueur apres sa reponse |
| `tags` | Mots-cles thematiques, separes par des virgules |

## Regenerer et controler

```bash
npm run questions:generate   # reecrit les quatre CSV
npm run questions:check      # doublons, options, lettres, coherence points/temps
```

La position de la bonne reponse est melangee de facon **deterministe** (graine
derivee de l'enonce) : deux generations successives produisent des fichiers
identiques, mais la bonne reponse n'est jamais systematiquement en A.

## Ajouter ou corriger des questions

Les questions ne se modifient pas directement dans les CSV : ils sont
regeneres. Editez la banque concernee dans `scripts/qgen/` puis relancez la
generation. Chaque question y est decrite de facon compacte :

```python
Q(
    "Quel est le chef-lieu de la region du Littoral ?",
    "Douala",                                   # bonne reponse
    ["Yaounde", "Kribi", "Edea"],               # distracteurs (3 ou plus)
    FACILE,
    "cameroun,geographie",
    "Douala est le chef-lieu de la region du Littoral.",
)
```
