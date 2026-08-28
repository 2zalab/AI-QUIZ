# -*- coding: utf-8 -*-
"""Banque Entrepreneuriat : entrepreneurs celebres, methodes et outils."""

from __future__ import annotations

from .common import CHALLENGE, FACILE, MOYEN, Q, others

# fondateur -> (entreprise, secteur, pays, difficulte)
FONDATEURS = {
    "Aliko Dangote": ("le groupe Dangote", "Le ciment et l'agroalimentaire", "le Nigeria", FACILE),
    "Strive Masiyiwa": ("Econet Wireless", "Les telecommunications", "le Zimbabwe", MOYEN),
    "Mo Ibrahim": ("Celtel", "Les telecommunications", "le Soudan", MOYEN),
    "Tony Elumelu": ("Heirs Holdings", "La banque et l'investissement", "le Nigeria", MOYEN),
    "Shola Akinlade": ("Paystack", "Les paiements en ligne", "le Nigeria", CHALLENGE),
    "Olugbenga Agboola": ("Flutterwave", "Les paiements en ligne", "le Nigeria", CHALLENGE),
    "Jason Njoku": ("IROKOtv", "Le streaming video", "le Nigeria", CHALLENGE),
    "Rebecca Enonchong": ("AppsTech", "Les logiciels d'entreprise", "le Cameroun", MOYEN),
    "Fred Swaniker": ("African Leadership University", "L'education", "le Ghana", CHALLENGE),
    "Verone Mankou": ("VMK", "Les tablettes et smartphones", "le Congo", CHALLENGE),
    "Karim Beguir": ("InstaDeep", "L'intelligence artificielle", "la Tunisie", CHALLENGE),
    "Bethlehem Tilahun Alemu": ("SoleRebels", "La chaussure ecologique", "l'Ethiopie", CHALLENGE),
    "Olivier Madiba": ("Kiro'o Games", "Le jeu video", "le Cameroun", MOYEN),
    "Arthur Zang": ("Himore Medical", "Les dispositifs medicaux", "le Cameroun", MOYEN),
    "Bill Gates": ("Microsoft", "Les logiciels informatiques", "les Etats-Unis", FACILE),
    "Steve Jobs": ("Apple", "L'electronique grand public", "les Etats-Unis", FACILE),
    "Jeff Bezos": ("Amazon", "Le commerce en ligne", "les Etats-Unis", FACILE),
    "Mark Zuckerberg": ("Facebook", "Les reseaux sociaux", "les Etats-Unis", FACILE),
    "Jack Ma": ("Alibaba", "Le commerce en ligne", "la Chine", MOYEN),
    "Elon Musk": ("Tesla", "L'automobile electrique", "les Etats-Unis", FACILE),
    "Reed Hastings": ("Netflix", "Le streaming video", "les Etats-Unis", MOYEN),
    "Brian Chesky": ("Airbnb", "L'hebergement entre particuliers", "les Etats-Unis", MOYEN),
    "Daniel Ek": ("Spotify", "Le streaming musical", "la Suede", MOYEN),
    "Ingvar Kamprad": ("IKEA", "Le mobilier", "la Suede", MOYEN),
    "Walt Disney": ("Disney", "Le divertissement", "les Etats-Unis", FACILE),
    "Henry Ford": ("Ford", "L'automobile", "les Etats-Unis", FACILE),
    "Sara Blakely": ("Spanx", "Le textile", "les Etats-Unis", CHALLENGE),
    "Richard Branson": ("Virgin", "Le transport aerien et la musique", "le Royaume-Uni", MOYEN),
    "Phil Knight": ("Nike", "L'equipement sportif", "les Etats-Unis", MOYEN),
    "Howard Schultz": ("Starbucks", "La restauration et le cafe", "les Etats-Unis", MOYEN),
    "Coco Chanel": ("Chanel", "La mode et le luxe", "la France", MOYEN),
    "Warren Buffett": ("Berkshire Hathaway", "L'investissement", "les Etats-Unis", MOYEN),
    "Jensen Huang": ("Nvidia", "Les processeurs graphiques", "les Etats-Unis", CHALLENGE),
    "Sam Altman": ("OpenAI", "L'intelligence artificielle", "les Etats-Unis", MOYEN),
}

METHODES = [
    ("Combien de blocs compte le Business Model Canvas ?", "Neuf",
     ["Quatre", "Six", "Douze"], MOYEN, "Le canvas d'Osterwalder comporte neuf blocs."),
    ("Quel bloc du Business Model Canvas decrit ce que l'entreprise promet a ses clients ?",
     "La proposition de valeur", ["Les partenaires cles", "La structure de couts", "Les ressources cles"],
     MOYEN, "La proposition de valeur est au centre du canvas."),
    ("Quel bloc du Business Model Canvas recense les sources de revenus ?", "Les flux de revenus",
     ["Les activites cles", "Les canaux", "Les segments de clientele"], MOYEN,
     "Les flux de revenus decrivent comment l'entreprise gagne de l'argent."),
    ("Que preconise l'approche Lean Startup ?", "Construire, mesurer, apprendre et iterer rapidement",
     ["Tout planifier pendant trois ans avant de lancer", "Ne jamais interroger les clients",
      "Copier integralement un concurrent"], MOYEN, "Le cycle build-measure-learn est au coeur du Lean Startup."),
    ("Qu'est-ce que le Design Thinking ?", "Une methode de conception centree sur les besoins reels des utilisateurs",
     ["Une technique de comptabilite", "Une methode de calcul d'impots", "Un logiciel de dessin industriel"],
     MOYEN, "Le Design Thinking part de l'empathie utilisateur."),
    ("Que designe le principe de Pareto applique aux ventes ?",
     "Environ 20 % des causes produisent environ 80 % des effets",
     ["Toutes les ventes se valent", "50 % des clients font 50 % du chiffre",
      "Il faut vendre a perte pour croitre"], MOYEN, "La loi des 20/80 aide a prioriser."),
    ("Que signifient les quatre lettres de l'analyse SWOT ?",
     "Forces, faiblesses, opportunites et menaces",
     ["Ventes, stocks, charges et benefices", "Salaires, water, outils et taxes",
      "Strategie, work, objectifs et temps"], MOYEN, "SWOT vient de Strengths, Weaknesses, Opportunities, Threats."),
    ("Dans une analyse SWOT, ou classe-t-on une equipe tres competente ?", "Dans les forces",
     ["Dans les menaces", "Dans les opportunites", "Dans les faiblesses"], MOYEN,
     "Les forces sont internes et favorables."),
    ("Dans une analyse SWOT, ou classe-t-on l'arrivee d'un concurrent puissant ?", "Dans les menaces",
     ["Dans les forces", "Dans les faiblesses", "Dans les opportunites"], MOYEN,
     "Les menaces sont externes et defavorables."),
    ("Que sont les cinq forces de Porter ?", "Un cadre d'analyse de l'intensite concurrentielle d'un secteur",
     ["Cinq techniques de vente", "Cinq regles comptables", "Cinq types de contrats"],
     CHALLENGE, "Porter analyse concurrents, entrants, substituts, clients et fournisseurs."),
    ("Que designe l'analyse PESTEL ?", "L'etude des facteurs politiques, economiques, sociaux, technologiques, ecologiques et legaux",
     ["Un logiciel de gestion de stock", "Une methode de recrutement", "Un mode de financement"],
     CHALLENGE, "PESTEL analyse le macro-environnement."),
    ("Que propose la strategie ocean bleu ?", "Creer un espace de marche nouveau plutot que d'affronter la concurrence",
     ["Baisser ses prix jusqu'a la perte", "Copier le leader du marche",
      "Vendre uniquement a l'export"], CHALLENGE, "L'ocean bleu evite la concurrence frontale."),
    ("Que mesure un OKR ?", "Un objectif accompagne de resultats cles mesurables",
     ["Le montant des impots", "Le nombre de salaries", "La valeur du stock"],
     CHALLENGE, "Objectives and Key Results structurent les priorites."),
    ("A quoi sert un tableau Kanban ?", "Visualiser l'avancement des taches par colonnes",
     ["Calculer la TVA", "Rediger les statuts", "Etablir un bilan"], MOYEN,
     "Le Kanban rend le flux de travail visible."),
    ("Que designe un MVP dans une demarche de creation ?", "La version minimale du produit permettant de tester le marche",
     ["Le meilleur vendeur de l'annee", "Un plan marketing complet", "Un statut juridique"],
     MOYEN, "Minimum Viable Product."),
    ("Pourquoi lancer un MVP plutot qu'un produit complet ?", "Pour apprendre vite en depensant peu",
     ["Pour tromper les clients", "Pour eviter de vendre", "Pour retarder le projet"],
     MOYEN, "Le MVP reduit le risque d'investir dans une offre non desiree."),
    ("Qu'est-ce qu'un pivot dans une startup ?", "Un changement de strategie apres les enseignements du marche",
     ["Un depot de bilan", "Un changement de logo", "Un recrutement massif"],
     MOYEN, "Le pivot conserve la vision mais change l'approche."),
    ("Que signifie iterer sur un produit ?", "L'ameliorer par versions successives grace aux retours des utilisateurs",
     ["Le vendre une seule fois", "Le breveter immediatement", "Le retirer du marche"],
     MOYEN, "L'iteration est au coeur des methodes agiles."),
    ("Quel est l'objectif d'un test A/B ?", "Comparer deux versions pour retenir la plus performante",
     ["Doubler les prix", "Recruter deux equipes", "Tenir deux comptabilites"],
     CHALLENGE, "Le test A/B mesure l'effet d'une variante."),
    ("Que designe le time to market ?", "Le delai entre l'idee et la mise sur le marche",
     ["Le temps de trajet des livreurs", "La duree d'une reunion", "Le delai de paiement des clients"],
     CHALLENGE, "Un time to market court donne un avantage concurrentiel."),
]


def build() -> list[Q]:
    qs: list[Q] = []
    entreprises = [v[0] for v in FONDATEURS.values()]
    secteurs = sorted({v[1] for v in FONDATEURS.values()})
    noms = list(FONDATEURS.keys())
    for nom, (entreprise, secteur, pays, diff) in FONDATEURS.items():
        qs.append(Q(
            f"Quelle entreprise {nom} a-t-il ou a-t-elle fondee ou dirigee ?",
            entreprise, others(nom, entreprises), diff, "entrepreneuriat,figures",
            f"{nom} : {entreprise} - secteur {secteur.lower()}, {pays}.",
        ))
        qs.append(Q(
            f"Dans quel secteur d'activite {entreprise} s'est-elle developpee ?",
            secteur, others(entreprise, secteurs), diff, "entrepreneuriat,figures",
            f"{entreprise} intervient dans : {secteur.lower()}.",
        ))
        qs.append(Q(
            f"De quel pays {nom} est-il ou est-elle originaire ?",
            pays, others(nom + "pays", sorted({v[2] for v in FONDATEURS.values()})), diff,
            "entrepreneuriat,figures", f"{nom} est originaire de ce pays : {pays}.",
        ))
    for question, correct, wrong, diff, expl in METHODES:
        qs.append(Q(question, correct, wrong, diff, "entrepreneuriat,methodes", expl))
    return qs
