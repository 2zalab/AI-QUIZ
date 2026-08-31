#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere les fichiers CSV de questions du MIT Entrepreneur Challenge.

Usage :
    python3 scripts/generate_questions.py [--out data]

Produit un fichier CSV par categorie, avec exactement 1000 questions chacun :
    data/questions_entrepreneuriat.csv
    data/questions_cameroun.csv
    data/questions_innovation_ia.csv
    data/questions_mixte.csv          (tire des trois autres categories)

Colonnes : id, category, category_slug, difficulty, question, option_a..d,
correct_answer (A/B/C/D), points, time_limit, explanation, tags.
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qgen.common import CHALLENGE, FACILE, MOYEN, Q, build_row, dedupe  # noqa: E402
from qgen import (  # noqa: E402
    cameroun_culture, cameroun_divers, cameroun_economie, cameroun_facile,
    cameroun_geo, cameroun_histoire, cameroun_people,
    entrepreneuriat_calculs, entrepreneuriat_cameroun, entrepreneuriat_complements,
    entrepreneuriat_figures, entrepreneuriat_glossaire, entrepreneuriat_pratique,
    entrepreneuriat_scenarios, entrepreneuriat_scenarios2,
    innovation_afrique, innovation_culture, innovation_glossaire,
    innovation_metiers, innovation_pratiques, innovation_usages,
)

TARGET = 1000
QUOTAS = {FACILE: 350, MOYEN: 450, CHALLENGE: 200}

FIELDNAMES = [
    "id", "category", "category_slug", "difficulty", "question",
    "option_a", "option_b", "option_c", "option_d", "correct_answer",
    "points", "time_limit", "explanation", "tags",
]

CATEGORIES = [
    {
        "slug": "entrepreneuriat",
        "name": "Entrepreneuriat",
        "prefix": "ent",
        "file": "questions_entrepreneuriat.csv",
        "modules": [
            entrepreneuriat_glossaire, entrepreneuriat_scenarios, entrepreneuriat_scenarios2,
            entrepreneuriat_calculs, entrepreneuriat_pratique, entrepreneuriat_figures,
            entrepreneuriat_cameroun, entrepreneuriat_complements,
        ],
    },
    {
        "slug": "cameroun",
        "name": "Cameroun",
        "prefix": "cmr",
        "file": "questions_cameroun.csv",
        "modules": [
            cameroun_geo, cameroun_people, cameroun_histoire, cameroun_culture,
            cameroun_economie, cameroun_divers, cameroun_facile,
        ],
    },
    {
        "slug": "innovation-ia",
        "name": "Innovation & IA",
        "prefix": "inn",
        "file": "questions_innovation_ia.csv",
        "modules": [
            innovation_glossaire, innovation_usages, innovation_culture,
            innovation_pratiques, innovation_afrique, innovation_metiers,
        ],
    },
]

MIXTE = {
    "slug": "mixte",
    "name": "Challenge Mixte",
    "prefix": "mix",
    "file": "questions_mixte.csv",
}


def collect(modules) -> list[Q]:
    questions: list[Q] = []
    for module in modules:
        questions.extend(module.build())
    return dedupe(questions)


def select(questions: list[Q], slug: str, target: int = TARGET) -> list[Q]:
    """Retient exactement `target` questions avec un equilibre de difficulte."""
    if len(questions) < target:
        raise SystemExit(
            f"[{slug}] seulement {len(questions)} questions disponibles, {target} requises."
        )
    rng = random.Random(f"select|{slug}")
    par_difficulte: dict[str, list[Q]] = {FACILE: [], MOYEN: [], CHALLENGE: []}
    for q in questions:
        par_difficulte[q.difficulty].append(q)
    for bucket in par_difficulte.values():
        rng.shuffle(bucket)

    retenues: list[Q] = []
    restes: list[Q] = []
    for difficulty, quota in QUOTAS.items():
        bucket = par_difficulte[difficulty]
        retenues.extend(bucket[:quota])
        restes.extend(bucket[quota:])
    rng.shuffle(restes)
    retenues.extend(restes[: target - len(retenues)])
    rng.shuffle(retenues)
    return retenues[:target]


def build_mixte(par_categorie: dict[str, list[Q]], target: int = TARGET) -> list[Q]:
    """Compose la categorie Mixte a partir des trois autres, de facon equilibree."""
    rng = random.Random("select|mixte")
    slugs = list(par_categorie.keys())
    quota = target // len(slugs)
    melange: list[Q] = []
    for index, slug in enumerate(slugs):
        pool = list(par_categorie[slug])
        rng.shuffle(pool)
        part = quota + (1 if index < target - quota * len(slugs) else 0)
        for q in pool[:part]:
            melange.append(Q(q.question, q.correct, list(q.wrong), q.difficulty,
                             f"mixte,{q.tags}", q.explanation))
    rng.shuffle(melange)
    return melange[:target]


def write_csv(path: Path, questions: list[Q], category: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        for index, q in enumerate(questions, start=1):
            qid = f"{category['prefix']}-{index:04d}"
            writer.writerow(build_row(q, category["name"], category["slug"], qid))


def summarize(name: str, questions: list[Q]) -> str:
    counts = Counter(q.difficulty for q in questions)
    return (f"{name:<18} {len(questions):>5} questions "
            f"(facile {counts[FACILE]}, moyen {counts[MOYEN]}, challenge {counts[CHALLENGE]})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="data", help="dossier de sortie (defaut : data)")
    args = parser.parse_args()
    out_dir = Path(args.out)

    retenues: dict[str, list[Q]] = {}
    for category in CATEGORIES:
        pool = collect(category["modules"])
        chosen = select(pool, category["slug"])
        retenues[category["slug"]] = chosen
        write_csv(out_dir / category["file"], chosen, category)
        print(summarize(category["name"], chosen), f"-> {category['file']}")

    mixte = build_mixte(retenues)
    write_csv(out_dir / MIXTE["file"], mixte, MIXTE)
    print(summarize(MIXTE["name"], mixte), f"-> {MIXTE['file']}")

    total = sum(len(v) for v in retenues.values()) + len(mixte)
    print(f"\nTotal : {total} questions ecrites dans {out_dir}/")


if __name__ == "__main__":
    main()
