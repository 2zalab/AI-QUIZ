# -*- coding: utf-8 -*-
"""Outils communs de generation des questions du iCLAN Entrepreneur Challenge.

Chaque question est decrite de facon compacte (enonce, bonne reponse, mauvaises
reponses) puis transformee en ligne CSV : les options sont melangees de maniere
deterministe (seed derivee de l'enonce) pour que la bonne reponse ne soit pas
toujours a la meme place, tout en gardant des exports reproductibles.
"""

from __future__ import annotations

import hashlib
import random
import re
import unicodedata
from dataclasses import dataclass, field

FACILE = "facile"
MOYEN = "moyen"
CHALLENGE = "challenge"

POINTS = {FACILE: 100, MOYEN: 200, CHALLENGE: 300}
TIME_LIMIT = {FACILE: 20, MOYEN: 25, CHALLENGE: 30}

LETTERS = ["A", "B", "C", "D"]


@dataclass
class Q:
    """Une question a choix multiple avant melange des options."""

    question: str
    correct: str
    wrong: list[str] = field(default_factory=list)
    difficulty: str = FACILE
    tags: str = ""
    explanation: str = ""


def _seed(text: str) -> int:
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:12], 16)


def normalize(text: str) -> str:
    """Cle de deduplication : minuscules, sans accents ni ponctuation."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return text.strip()


def pick_wrongs(q: Q) -> list[str]:
    """Choisit 3 mauvaises reponses distinctes, de maniere deterministe."""
    pool: list[str] = []
    seen = {normalize(q.correct)}
    for w in q.wrong:
        key = normalize(w)
        if key in seen:
            continue
        seen.add(key)
        pool.append(w)
    if len(pool) < 3:
        raise ValueError(
            f"Pas assez de distracteurs ({len(pool)}) pour : {q.question!r}"
        )
    if len(pool) == 3:
        return pool
    rng = random.Random(_seed(q.question + "|wrongs"))
    return rng.sample(pool, 3)


def build_row(q: Q, category: str, slug: str, qid: str) -> dict:
    """Transforme une Q en ligne CSV prete a l'import."""
    options = [q.correct] + pick_wrongs(q)
    rng = random.Random(_seed(q.question + "|shuffle"))
    rng.shuffle(options)
    index = options.index(q.correct)
    return {
        "id": qid,
        "category": category,
        "category_slug": slug,
        "difficulty": q.difficulty,
        "question": clean(q.question),
        "option_a": clean(options[0]),
        "option_b": clean(options[1]),
        "option_c": clean(options[2]),
        "option_d": clean(options[3]),
        "correct_answer": LETTERS[index],
        "points": POINTS[q.difficulty],
        "time_limit": TIME_LIMIT[q.difficulty],
        "explanation": clean(q.explanation),
        "tags": q.tags,
    }


ELISIONS = [
    (r"\bde le\b", "du"),
    (r"\bde les\b", "des"),
    (r"\bde un\b", "d'un"),
    (r"\bde une\b", "d'une"),
]


def cap(text: str) -> str:
    """Met une majuscule initiale sans toucher au reste (noms propres preserves)."""
    text = str(text)
    return text[:1].upper() + text[1:] if text else text


def clean(text: str) -> str:
    text = re.sub(r"\s+", " ", str(text)).strip()
    for pattern, replacement in ELISIONS:
        text = re.sub(pattern, replacement, text)
    return text


def dedupe(questions: list[Q]) -> list[Q]:
    """Supprime les enonces en double (premiere occurrence gardee)."""
    seen: set[str] = set()
    out: list[Q] = []
    for q in questions:
        key = normalize(q.question)
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
    return out


def others(value: str, universe: list[str], count: int = 6) -> list[str]:
    """Distracteurs pris dans la meme famille (ex : autres chefs-lieux)."""
    rng = random.Random(_seed(value + "|others"))
    pool = [v for v in universe if normalize(v) != normalize(value)]
    rng.shuffle(pool)
    return pool[:count]
