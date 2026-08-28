#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controle qualite des fichiers CSV de questions.

Verifie pour chaque fichier :
  - le nombre de lignes et l'unicite des identifiants et des enonces ;
  - la presence des quatre options, toutes distinctes et non vides ;
  - la coherence de la lettre de reponse (A/B/C/D) ;
  - la coherence points / temps imparti avec la difficulte ;
  - la repartition des bonnes reponses entre les positions A, B, C et D.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

POINTS = {"facile": 100, "moyen": 200, "challenge": 300}
TIME_LIMIT = {"facile": 20, "moyen": 25, "challenge": 30}
LETTERS = ["A", "B", "C", "D"]


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    questions: set[str] = set()
    letters: Counter[str] = Counter()
    difficulties: Counter[str] = Counter()
    rows = 0

    with path.open(encoding="utf-8", newline="") as handle:
        for line, row in enumerate(csv.DictReader(handle), start=2):
            rows += 1
            prefix = f"{path.name}:{line}"
            if row["id"] in ids:
                errors.append(f"{prefix} identifiant duplique : {row['id']}")
            ids.add(row["id"])

            key = row["question"].strip().lower()
            if key in questions:
                errors.append(f"{prefix} enonce duplique : {row['question'][:60]}...")
            questions.add(key)

            options = [row[f"option_{c}"] for c in "abcd"]
            if any(not o.strip() for o in options):
                errors.append(f"{prefix} option vide")
            if len(set(o.strip().lower() for o in options)) != 4:
                errors.append(f"{prefix} options non distinctes")
            if row["correct_answer"] not in LETTERS:
                errors.append(f"{prefix} lettre invalide : {row['correct_answer']}")
            else:
                letters[row["correct_answer"]] += 1

            difficulty = row["difficulty"]
            difficulties[difficulty] += 1
            if difficulty not in POINTS:
                errors.append(f"{prefix} difficulte inconnue : {difficulty}")
            else:
                if int(row["points"]) != POINTS[difficulty]:
                    errors.append(f"{prefix} points incoherents")
                if int(row["time_limit"]) != TIME_LIMIT[difficulty]:
                    errors.append(f"{prefix} temps imparti incoherent")
            if not row["question"].strip():
                errors.append(f"{prefix} enonce vide")

    spread = ", ".join(f"{letter} {letters[letter]}" for letter in LETTERS)
    diff = ", ".join(f"{k} {v}" for k, v in sorted(difficulties.items()))
    print(f"{path.name:<34} {rows:>5} lignes | difficultes : {diff} | reponses : {spread}")
    return errors


def main() -> int:
    data_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "data")
    files = sorted(data_dir.glob("questions_*.csv"))
    if not files:
        print(f"Aucun fichier questions_*.csv dans {data_dir}")
        return 1
    all_errors: list[str] = []
    for path in files:
        all_errors.extend(check_file(path))
    if all_errors:
        print(f"\n{len(all_errors)} probleme(s) detecte(s) :")
        for error in all_errors[:40]:
            print(" -", error)
        return 1
    print("\nTous les controles sont passes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
