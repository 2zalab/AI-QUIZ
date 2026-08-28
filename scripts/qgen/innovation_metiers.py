# -*- coding: utf-8 -*-
"""Banque Innovation & IA : metiers du numerique et outils du quotidien."""

from __future__ import annotations

from .common import cap, CHALLENGE, FACILE, MOYEN, Q, others

# metier -> (mission, difficulte)
METIERS = {
    "un developpeur web": ("Concevoir et programmer des sites et applications en ligne", FACILE),
    "un developpeur mobile": ("Creer des applications destinees aux telephones", FACILE),
    "un designer d'interface": ("Concevoir l'apparence et l'ergonomie des ecrans", MOYEN),
    "un chef de projet numerique": ("Coordonner les equipes, les delais et le budget d'un projet", MOYEN),
    "un analyste de donnees": ("Exploiter les donnees pour aider a decider", MOYEN),
    "un data scientist": ("Construire des modeles predictifs a partir de donnees", CHALLENGE),
    "un ingenieur en intelligence artificielle": ("Concevoir et entrainer des modeles d'IA", CHALLENGE),
    "un administrateur systeme": ("Maintenir les serveurs et les infrastructures informatiques", MOYEN),
    "un expert en cybersecurite": ("Proteger les systemes et les donnees contre les attaques", MOYEN),
    "un community manager": ("Animer la presence d'une marque sur les reseaux sociaux", FACILE),
    "un redacteur web": ("Produire des contenus ecrits pour internet", FACILE),
    "un specialiste du referencement": ("Ameliorer la visibilite d'un site dans les moteurs de recherche", MOYEN),
    "un graphiste numerique": ("Creer les visuels et l'identite graphique", FACILE),
    "un monteur video": ("Assembler et retoucher des sequences video", FACILE),
    "un technicien de maintenance informatique": ("Reparer et entretenir les equipements informatiques", FACILE),
    "un testeur logiciel": ("Verifier le bon fonctionnement d'un programme avant sa mise en service", MOYEN),
    "un product owner": ("Definir les priorites d'un produit numerique au nom des utilisateurs", CHALLENGE),
    "un formateur numerique": ("Former les equipes a l'usage des outils digitaux", FACILE),
    "un electronicien": ("Concevoir et reparer des circuits et appareils electroniques", MOYEN),
    "un pilote de drone professionnel": ("Realiser des prises de vue ou des mesures aeriennes", MOYEN),
    "un gestionnaire de bases de donnees": ("Organiser, securiser et optimiser le stockage des donnees", CHALLENGE),
    "un consultant en transformation digitale": ("Accompagner une organisation dans son passage au numerique", MOYEN),
    "un specialiste du support client en ligne": ("Assister les utilisateurs a distance", FACILE),
    "un designer d'experience utilisateur": ("Ameliorer le parcours et le ressenti des utilisateurs", MOYEN),
}

# outil -> (usage principal, categorie, difficulte)
OUTILS = {
    "un tableur": ("Organiser des donnees et faire des calculs", "La bureautique", FACILE),
    "un traitement de texte": ("Rediger et mettre en forme des documents", "La bureautique", FACILE),
    "un logiciel de presentation": ("Creer des diaporamas pour presenter un projet", "La bureautique", FACILE),
    "une messagerie electronique": ("Envoyer et recevoir des courriers numeriques", "La communication", FACILE),
    "une application de messagerie instantanee": ("Echanger des messages en temps reel", "La communication", FACILE),
    "un agenda partage": ("Coordonner les rendez-vous d'une equipe", "L'organisation", FACILE),
    "un outil de gestion de taches": ("Suivre l'avancement du travail d'une equipe", "L'organisation", MOYEN),
    "un espace de stockage en ligne": ("Conserver et partager des fichiers accessibles partout", "Le stockage", FACILE),
    "un logiciel de comptabilite": ("Enregistrer les operations financieres de l'entreprise", "La gestion", MOYEN),
    "un logiciel de facturation": ("Editer et suivre les factures clients", "La gestion", FACILE),
    "un logiciel de caisse": ("Enregistrer les ventes et editer les tickets", "La gestion", FACILE),
    "un outil de gestion de stock": ("Suivre les entrees et sorties de marchandises", "La gestion", MOYEN),
    "un CRM": ("Centraliser l'historique de la relation avec chaque client", "La gestion", MOYEN),
    "un outil de creation graphique en ligne": ("Realiser des visuels sans competence de designer", "La creation", FACILE),
    "un outil no-code": ("Construire un site ou une application sans programmer", "La creation", MOYEN),
    "un outil d'analyse d'audience": ("Mesurer la frequentation d'un site web", "La mesure", MOYEN),
    "un antivirus": ("Detecter et neutraliser les logiciels malveillants", "La securite", FACILE),
    "un gestionnaire de mots de passe": ("Stocker de facon securisee des identifiants complexes", "La securite", MOYEN),
    "un VPN": ("Chiffrer la connexion pour proteger les echanges en ligne", "La securite", CHALLENGE),
    "un scanner de documents sur telephone": ("Numeriser des papiers avec l'appareil photo", "La numerisation", FACILE),
    "une plateforme de visioconference": ("Organiser des reunions a distance", "La communication", FACILE),
    "une plateforme de formation en ligne": ("Diffuser des cours accessibles a distance", "La formation", FACILE),
    "un assistant IA conversationnel": ("Obtenir de l'aide pour rediger, resumer ou expliquer", "L'intelligence artificielle", FACILE),
    "un outil de traduction en ligne": ("Traduire rapidement un texte d'une langue a une autre", "L'intelligence artificielle", FACILE),
}


def build() -> list[Q]:
    qs: list[Q] = []
    missions = [v[0] for v in METIERS.values()]
    noms_metiers = list(METIERS.keys())
    for metier, (mission, diff) in METIERS.items():
        qs.append(Q(
            f"Quelle est la mission principale de {metier} ?",
            mission, others(metier, missions), diff, "innovation,metiers",
            f"{cap(metier)} : {mission.lower()}.",
        ))
        qs.append(Q(
            f"Quel professionnel du numerique a pour mission de : {mission} ?",
            metier, others(mission, noms_metiers), diff, "innovation,metiers",
            f"Il s'agit de {metier}.",
        ))
    usages = [v[0] for v in OUTILS.values()]
    categories = sorted({v[1] for v in OUTILS.values()})
    noms_outils = list(OUTILS.keys())
    for outil, (usage, categorie, diff) in OUTILS.items():
        qs.append(Q(
            f"A quoi sert principalement {outil} ?",
            usage, others(outil, usages), diff, "innovation,outils",
            f"{cap(outil)} sert a : {usage.lower()}.",
        ))
        qs.append(Q(
            f"Quel outil numerique permet de : {usage} ?",
            outil, others(usage, noms_outils), diff, "innovation,outils",
            f"Il s'agit de {outil}.",
        ))
        qs.append(Q(
            f"A quelle categorie d'outils appartient {outil} ?",
            categorie, others(outil + "c", categories), diff, "innovation,outils",
            f"{cap(outil)} appartient a cette categorie : {categorie.lower()}.",
        ))
    return qs
