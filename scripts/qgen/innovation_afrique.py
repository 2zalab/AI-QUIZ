# -*- coding: utf-8 -*-
"""Banque Innovation & IA : le numerique en Afrique et au Cameroun."""

from __future__ import annotations

from .common import CHALLENGE, FACILE, MOYEN, Q, others

# service / startup -> (activite, pays d'origine, difficulte)
ACTEURS = {
    "M-Pesa": ("Le transfert d'argent par telephone", "le Kenya", MOYEN),
    "Flutterwave": ("Les paiements en ligne pour entreprises", "le Nigeria", MOYEN),
    "Paystack": ("Les paiements en ligne pour commercants", "le Nigeria", CHALLENGE),
    "Jumia": ("La vente en ligne de produits varies", "le Nigeria", FACILE),
    "Andela": ("La formation et le placement de developpeurs", "le Nigeria", CHALLENGE),
    "Yoco": ("Les terminaux de paiement pour petits commerces", "l'Afrique du Sud", CHALLENGE),
    "Wave": ("Le transfert d'argent mobile a bas cout", "le Senegal", MOYEN),
    "InstaDeep": ("L'intelligence artificielle appliquee aux entreprises", "la Tunisie", CHALLENGE),
    "Kiro'o Games": ("Le developpement de jeux video", "le Cameroun", MOYEN),
    "Njorku": ("La recherche d'emploi en ligne", "le Cameroun", CHALLENGE),
    "Gifted Mom": ("Le suivi de la sante maternelle par mobile", "le Cameroun", CHALLENGE),
    "Will and Brothers": ("La conception de drones civils", "le Cameroun", CHALLENGE),
    "Healthlane": ("Les services de sante numeriques", "le Cameroun", CHALLENGE),
    "Waspito": ("La teleconsultation medicale", "le Cameroun", CHALLENGE),
    "Diool": ("Les paiements marchands et le mobile money", "le Cameroun", CHALLENGE),
    "Orange Money": ("Le paiement et le transfert par telephone", "le Cameroun", FACILE),
    "MTN MoMo": ("Le paiement et le transfert par telephone", "le Cameroun", FACILE),
    "Glotelho": ("La vente en ligne d'appareils et d'electromenager", "le Cameroun", MOYEN),
    "Yassir": ("Le transport a la demande et la livraison", "l'Algerie", CHALLENGE),
    "Twiga Foods": ("La distribution de produits agricoles", "le Kenya", CHALLENGE),
    "SafeMotos": ("Le transport a moto securise", "le Rwanda", CHALLENGE),
    "Zipline": ("La livraison medicale par drone", "le Rwanda", MOYEN),
}

CONTEXTE = [
    ("Quel service a fait de l'Afrique de l'Est un pionnier mondial du paiement mobile ?", "M-Pesa",
     ["Le minitel", "Le fax", "Le telegramme"], MOYEN, "M-Pesa a ete lance au Kenya en 2007."),
    ("Pourquoi le mobile money s'est-il developpe si vite en Afrique ?",
     "Parce qu'une grande partie de la population n'avait pas de compte bancaire mais possedait un telephone",
     ["Parce que les banques etaient interdites", "Parce que l'argent liquide n'existait pas",
      "Parce que les telephones etaient gratuits"], MOYEN, "Le mobile a comble le manque d'acces bancaire."),
    ("Quel avantage le mobile money apporte-t-il a un commercant de quartier ?",
     "Encaisser sans especes et garder une trace de ses ventes",
     ["Supprimer ses fournisseurs", "Garantir un benefice",
      "Eviter de servir les clients"], FACILE, "Il securise et trace les encaissements."),
    ("Quel obstacle freine encore le e-commerce dans plusieurs pays africains ?",
     "L'adressage imprecis et le cout de la livraison",
     ["L'absence totale de clients", "L'interdiction du commerce",
      "Le manque de telephones"], MOYEN, "Le dernier kilometre reste un defi logistique."),
    ("Quel mode de paiement rassure encore beaucoup d'acheteurs en ligne en Afrique ?",
     "Le paiement a la livraison", ["Le paiement par cheque uniquement",
      "Le virement international uniquement", "Le paiement en lingots d'or"],
     MOYEN, "Le paiement a reception limite le risque percu."),
    ("Que designe une fintech ?", "Une entreprise qui utilise la technologie pour proposer des services financiers",
     ["Une usine de textile", "Une exploitation agricole", "Une compagnie aerienne"],
     MOYEN, "Financial technology."),
    ("Quel secteur du numerique africain attire le plus de financements ces dernieres annees ?", "La fintech",
     ["L'industrie du charbon", "La construction navale", "L'aeronautique lourde"],
     MOYEN, "Les paiements et services financiers dominent les levees de fonds."),
    ("Comment appelle-t-on les pays africains les plus actifs dans les levees de fonds technologiques ?",
     "Le Big Four : Nigeria, Kenya, Egypte et Afrique du Sud",
     ["Le Big Two : Cameroun et Tchad", "Le Big Five europeen",
      "Le G7 africain"], CHALLENGE, "Ces quatre pays concentrent l'essentiel des financements tech."),
    ("Quel est le principal atout demographique de l'Afrique pour le numerique ?",
     "Une population tres jeune et connectee",
     ["Une population majoritairement agee", "Une population tres reduite",
      "Une population sans telephone"], FACILE, "La jeunesse africaine est un moteur d'adoption."),
    ("Quel type de connexion domine l'acces a internet en Afrique ?", "L'internet mobile",
     ["La fibre a domicile pour tous", "Le cable telephonique fixe",
      "La connexion satellite domestique generalisee"], FACILE, "L'acces se fait majoritairement par le mobile."),
    ("Quel projet camerounais vise a etendre la fibre optique dans le pays ?",
     "Le deploiement de la dorsale nationale a fibre optique",
     ["La construction d'un aeroport", "Le barrage de Lagdo",
      "La ligne ferroviaire de Ngaoundere"], MOYEN, "La fibre nationale ameliore le debit et la couverture."),
    ("Quelle est la principale difficulte des startups camerounaises pour se financer ?",
     "L'acces limite au capital-risque local",
     ["Le trop grand nombre d'investisseurs", "L'interdiction de creer des entreprises",
      "L'absence de talents"], MOYEN, "Le financement en amorçage reste rare localement."),
    ("Que propose un incubateur a une startup camerounaise ?",
     "Un accompagnement, un espace de travail et l'acces a un reseau",
     ["Un chiffre d'affaires garanti", "Une exoneration totale d'impots",
      "Des clients obligatoires"], MOYEN, "L'incubateur structure le projet et ouvre des portes."),
    ("Quel evenement rassemble regulierement les acteurs du numerique africain autour de projets courts ?",
     "Un hackathon", ["Un conseil des ministres", "Un match de football",
      "Une assemblee generale d'actionnaires"], MOYEN, "Le hackathon fait emerger des prototypes en quelques jours."),
    ("Quel usage de l'IA est particulierement utile pour l'agriculture africaine ?",
     "L'analyse d'images pour detecter les maladies des cultures",
     ["La production de neige", "Le pilotage de trains a grande vitesse",
      "La fabrication de satellites"], MOYEN, "La detection precoce des maladies protege les rendements."),
    ("Quel service numerique facilite l'acces aux soins dans les zones eloignees ?", "La teleconsultation",
     ["Le cinema en ligne", "Le jeu video", "Le streaming musical"],
     FACILE, "La telemedecine reduit la contrainte de distance."),
    ("Quel usage du drone est deja operationnel en Afrique de l'Est pour la sante ?",
     "La livraison de sang et de medicaments",
     ["Le transport de passagers", "La distribution de repas chauds partout",
      "Le remplacement des ambulances routieres"], MOYEN, "Zipline livre des produits sanguins au Rwanda et au Ghana."),
    ("Quelle langue est un atout pour un entrepreneur numerique camerounais sur le marche africain ?",
     "Le bilinguisme francais-anglais", ["Le latin", "Le grec ancien", "Le japonais"],
     FACILE, "Le bilinguisme ouvre les marches francophones et anglophones."),
    ("Quel avantage la ZLECAf offre-t-elle aux entreprises numeriques africaines ?",
     "Un acces facilite a un marche continental",
     ["Une interdiction d'exporter", "Une taxe supplementaire garantie",
      "Une obligation de fermer"], MOYEN, "La zone de libre-echange elargit le marche adressable."),
    ("Quel frein energetique limite l'activite numerique dans plusieurs zones camerounaises ?",
     "Les coupures d'electricite", ["L'exces d'energie solaire", "L'interdiction des ordinateurs",
      "Le manque de cables sous-marins uniquement"], FACILE, "La stabilite electrique conditionne les usages numeriques."),
    ("Quelle solution permet de travailler malgre les coupures de courant ?",
     "Un onduleur ou une batterie de secours",
     ["Un ordinateur sans alimentation", "Un modem eteint",
      "Un ecran plus grand"], FACILE, "L'alimentation de secours assure la continuite."),
    ("Quel usage du code QR se developpe fortement dans le commerce africain ?",
     "Le paiement et l'acces rapide a une information produit",
     ["Le remplacement des routes", "La production d'electricite",
      "Le stockage d'eau"], FACILE, "Le QR code sert au paiement et a l'information."),
]


def build() -> list[Q]:
    qs: list[Q] = []
    activites = sorted({v[0] for v in ACTEURS.values()})
    pays = sorted({v[1] for v in ACTEURS.values()})
    noms = list(ACTEURS.keys())
    for nom, (activite, origine, diff) in ACTEURS.items():
        qs.append(Q(
            f"Quelle est l'activite principale de {nom} ?",
            activite, others(nom, activites), diff, "innovation,afrique",
            f"{nom} : {activite.lower()} ({origine}).",
        ))
        qs.append(Q(
            f"De quel pays {nom} est-il ou est-elle originaire ?",
            origine, others(nom + "p", pays), diff, "innovation,afrique",
            f"{nom} vient de ce pays : {origine}.",
        ))
        qs.append(Q(
            f"Quel service correspond a cette activite : {activite} ?",
            nom, others(activite, noms), diff, "innovation,afrique",
            f"{nom} correspond a cette activite.",
        ))
    for question, correct, wrong, diff, expl in CONTEXTE:
        qs.append(Q(question, correct, wrong, diff, "innovation,afrique", expl))
    return qs
