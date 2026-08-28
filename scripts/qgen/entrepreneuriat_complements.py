# -*- coding: utf-8 -*-
"""Banque Entrepreneuriat : sigles, classification des couts, vente et digital."""

from __future__ import annotations

from .common import cap, CHALLENGE, FACILE, MOYEN, Q, others

# sigle -> (signification, difficulte)
SIGLES = {
    "PME": ("Petite et Moyenne Entreprise", FACILE),
    "TPE": ("Tres Petite Entreprise", FACILE),
    "CA": ("Chiffre d'Affaires", FACILE),
    "BFR": ("Besoin en Fonds de Roulement", CHALLENGE),
    "ROI": ("Retour sur Investissement", MOYEN),
    "KPI": ("Indicateur Cle de Performance", MOYEN),
    "RSE": ("Responsabilite Societale des Entreprises", MOYEN),
    "MVP": ("Produit Minimum Viable", MOYEN),
    "B2B": ("Vente d'entreprise a entreprise", MOYEN),
    "B2C": ("Vente d'entreprise a particulier", MOYEN),
    "SARL": ("Societe a Responsabilite Limitee", FACILE),
    "SA": ("Societe Anonyme", FACILE),
    "GIE": ("Groupement d'Interet Economique", MOYEN),
    "RCCM": ("Registre du Commerce et du Credit Mobilier", MOYEN),
    "OHADA": ("Organisation pour l'Harmonisation en Afrique du Droit des Affaires", MOYEN),
    "OAPI": ("Organisation Africaine de la Propriete Intellectuelle", CHALLENGE),
    "CFCE": ("Centre de Formalites de Creation des Entreprises", MOYEN),
    "NIU": ("Numero d'Identifiant Unique", MOYEN),
    "TVA": ("Taxe sur la Valeur Ajoutee", FACILE),
    "CNPS": ("Caisse Nationale de Prevoyance Sociale", MOYEN),
    "SMIG": ("Salaire Minimum Interprofessionnel Garanti", MOYEN),
    "PIB": ("Produit Interieur Brut", FACILE),
    "ZLECAf": ("Zone de Libre-Echange Continentale Africaine", MOYEN),
    "CEMAC": ("Communaute Economique et Monetaire de l'Afrique Centrale", MOYEN),
    "BEAC": ("Banque des Etats de l'Afrique Centrale", MOYEN),
    "EMF": ("Etablissement de Microfinance", MOYEN),
    "CRM": ("Gestion de la Relation Client", MOYEN),
    "ERP": ("Progiciel de Gestion Integre", CHALLENGE),
    "SEO": ("Optimisation pour les moteurs de recherche", MOYEN),
    "CAC": ("Cout d'Acquisition Client", CHALLENGE),
    "SaaS": ("Logiciel fourni comme un service en ligne", CHALLENGE),
    "R&D": ("Recherche et Developpement", FACILE),
    "APME": ("Agence de Promotion des Petites et Moyennes Entreprises", MOYEN),
    "FNE": ("Fonds National de l'Emploi", MOYEN),
    "GICAM": ("Groupement Inter-patronal du Cameroun", MOYEN),
    "CCIMA": ("Chambre de Commerce, d'Industrie, des Mines et de l'Artisanat", CHALLENGE),
    "IGP": ("Indication Geographique Protegee", CHALLENGE),
    "BVMAC": ("Bourse des Valeurs Mobilieres de l'Afrique Centrale", CHALLENGE),
}

# charge -> "fixe" ou "variable"
CHARGES = {
    "le loyer mensuel du local": "fixe",
    "le salaire fixe du gerant": "fixe",
    "l'abonnement internet du bureau": "fixe",
    "l'assurance annuelle de l'entreprise": "fixe",
    "l'amortissement d'une machine": "fixe",
    "la matiere premiere consommee par produit": "variable",
    "l'emballage de chaque article vendu": "variable",
    "la commission versee au vendeur par vente": "variable",
    "le carburant utilise pour chaque livraison": "variable",
    "les frais de transport par commande": "variable",
    "l'electricite d'un atelier proportionnelle a la production": "variable",
    "la taxe fonciere annuelle": "fixe",
}

VENTE = [
    ("Quelle est la premiere etape d'un entretien de vente reussi ?", "Comprendre le besoin du client en posant des questions",
     ["Reciter tout le catalogue", "Annoncer le prix immediatement", "Parler de soi pendant dix minutes"],
     FACILE, "La decouverte du besoin precede l'argumentaire."),
    ("Que faire face a l'objection c'est trop cher ?", "Reformuler, comprendre la reference du client et rappeler la valeur apportee",
     ["Baisser le prix immediatement", "Mettre fin a la discussion", "Dire au client qu'il a tort"],
     MOYEN, "Une objection prix se traite par la valeur, pas par la remise reflexe."),
    ("Que designe une objection en vente ?", "Un frein exprime par le client, souvent signe d'interet",
     ["Un refus definitif et sans appel", "Une insulte", "Une commande ferme"],
     MOYEN, "L'objection ouvre le dialogue."),
    ("Quel est le meilleur moment pour conclure une vente ?", "Quand le client a exprime son accord sur la valeur et n'a plus d'objection majeure",
     ["Des les premieres secondes", "Apres avoir epuise le client",
      "Uniquement par ecrit trois mois plus tard"], MOYEN, "La conclusion suit la levee des objections."),
    ("Que signifie negocier gagnant-gagnant ?", "Trouver un accord ou chaque partie tire un benefice reel",
     ["Imposer ses conditions", "Ceder sur tout", "Rompre la discussion"],
     FACILE, "L'accord equilibre construit une relation durable."),
    ("Quelle preparation est indispensable avant une negociation importante ?",
     "Connaitre son prix plancher et ses marges de manoeuvre",
     ["Improviser totalement", "Ignorer ses couts", "Fixer un prix au hasard"],
     MOYEN, "Sans prix plancher, on cede trop."),
    ("Que faire lorsqu'un prospect ne repond plus apres un devis ?",
     "Relancer poliment une ou deux fois en apportant une information utile",
     ["Le harceler tous les jours", "L'ignorer definitivement", "Lui envoyer une facture"],
     MOYEN, "Une relance de valeur reste professionnelle."),
    ("Quel est l'interet d'un argumentaire structure ?", "Presenter les benefices clients de facon claire et convaincante",
     ["Reciter les caracteristiques techniques uniquement", "Parler le plus longtemps possible",
      "Eviter de repondre aux questions"], MOYEN, "On vend des benefices, pas des caracteristiques."),
    ("Quelle difference entre une caracteristique et un benefice produit ?",
     "La caracteristique decrit le produit, le benefice decrit ce que le client y gagne",
     ["Il n'y a aucune difference", "Le benefice est le prix",
      "La caracteristique est la marge"], MOYEN, "Le client achete un resultat, pas une fiche technique."),
    ("Pourquoi qualifier un prospect avant de lui consacrer du temps ?",
     "Pour verifier qu'il a le besoin, le budget et le pouvoir de decision",
     ["Pour le faire attendre", "Pour augmenter le prix", "Pour eviter de vendre"],
     CHALLENGE, "La qualification evite de perdre du temps commercial."),
    ("Quel comportement renforce la confiance lors d'une vente ?", "Tenir ses engagements de delai et de qualite",
     ["Promettre l'impossible", "Eviter les questions du client", "Changer de prix sans explication"],
     FACILE, "La confiance se construit par la fiabilite."),
    ("Comment traiter un client mecontent ?", "Ecouter, reconnaitre le probleme, proposer une solution et suivre son application",
     ["Nier le probleme", "Rejeter la faute sur le client", "Ne pas repondre"],
     FACILE, "Un litige bien traite peut renforcer la relation."),
]

DIGITAL = [
    ("Pourquoi une petite entreprise a-t-elle interet a etre visible en ligne ?",
     "Parce que ses clients cherchent des produits et services sur internet",
     ["Parce que la loi l'impose", "Pour eviter de servir les clients",
      "Pour supprimer la concurrence"], FACILE, "La presence en ligne elargit la visibilite."),
    ("Quel outil gratuit permet a un commerce d'apparaitre sur une carte en ligne ?",
     "Une fiche d'etablissement sur un service de cartographie",
     ["Un logiciel de comptabilite", "Un tableur", "Une imprimante connectee"],
     MOYEN, "La fiche etablissement ameliore la visibilite locale."),
    ("Que designe le SEO ?", "L'optimisation d'un site pour apparaitre dans les resultats de recherche",
     ["Un statut juridique", "Un mode de financement", "Un impot local"],
     MOYEN, "Search Engine Optimization."),
    ("Quel est l'avantage d'un catalogue produit en ligne ?", "Presenter l'offre en permanence sans local supplementaire",
     ["Supprimer les couts de production", "Garantir les ventes",
      "Eviter de payer les fournisseurs"], FACILE, "Le catalogue en ligne travaille 24 h/24."),
    ("Que faut-il eviter sur une page de vente en ligne ?", "Des informations floues sur le prix et la livraison",
     ["Des photos claires du produit", "Des avis clients", "Un moyen de contact visible"],
     MOYEN, "L'ambiguite fait fuir l'acheteur."),
    ("Quel indicateur suivre en priorite pour une boutique en ligne debutante ?", "Le nombre de commandes reelles",
     ["Le nombre de couleurs du site", "Le nombre de polices utilisees",
      "Le nombre de pages creees"], MOYEN, "Les commandes mesurent la performance reelle."),
    ("Pourquoi repondre rapidement aux messages des clients sur les reseaux ?",
     "Parce que la reactivite influence directement la decision d'achat",
     ["Parce que c'est obligatoire", "Pour eviter de vendre",
      "Pour augmenter les frais"], FACILE, "En ligne, la reactivite fait la difference."),
    ("Quel risque une entreprise court-elle en publiant sans strategie sur les reseaux ?",
     "Perdre du temps sans generer de clients",
     ["Devenir automatiquement leader", "Reduire ses couts fixes",
      "Obtenir un financement"], MOYEN, "La publication doit servir un objectif commercial."),
    ("Qu'est-ce qu'un outil no-code apporte a un entrepreneur ?", "Creer un site ou une application sans savoir programmer",
     ["Remplacer la comptabilite", "Supprimer les impots", "Garantir des clients"],
     MOYEN, "Le no-code accelere le prototypage."),
    ("Pourquoi sauvegarder regulierement ses donnees commerciales ?", "Pour ne pas perdre son fichier client et son historique en cas d'incident",
     ["Pour occuper de l'espace", "Pour ralentir l'ordinateur",
      "Parce que la banque l'exige"], FACILE, "Le fichier client est un actif strategique."),
    ("Quelle precaution prendre avec les mots de passe professionnels ?",
     "Utiliser des mots de passe forts et differents pour chaque service",
     ["Utiliser le meme partout", "Les ecrire sur la vitrine",
      "Les partager publiquement"], FACILE, "La securite des acces protege l'activite."),
    ("Que designe un paiement securise en ligne ?", "Un paiement realise via un service qui protege les donnees et confirme la transaction",
     ["Un paiement en especes dans la rue", "Un virement sans trace",
      "Un paiement promis oralement"], MOYEN, "La securisation rassure l'acheteur."),
]


def build() -> list[Q]:
    qs: list[Q] = []
    significations = [v[0] for v in SIGLES.values()]
    for sigle, (sens, diff) in SIGLES.items():
        qs.append(Q(
            f"Que signifie le sigle {sigle} dans le monde de l'entreprise ?",
            sens, others(sigle, significations), diff, "entrepreneuriat,sigles",
            f"{sigle} : {sens}.",
        ))
    fixes = [c for c, t in CHARGES.items() if t == "fixe"]
    variables = [c for c, t in CHARGES.items() if t == "variable"]
    for charge, type_charge in CHARGES.items():
        autres = variables if type_charge == "fixe" else fixes
        qs.append(Q(
            f"Comment qualifie-t-on cette charge : {charge} ?",
            f"Une charge {type_charge}",
            [f"Une charge {'variable' if type_charge == 'fixe' else 'fixe'}",
             "Un produit d'exploitation", "Un actif immobilise"],
            MOYEN, "entrepreneuriat,couts",
            f"{cap(charge)} est une charge {type_charge}.",
        ))
        qs.append(Q(
            f"Parmi ces elements, lequel est une charge {type_charge} ?",
            charge, others(charge + type_charge, autres), MOYEN, "entrepreneuriat,couts",
            f"{cap(charge)} est une charge {type_charge}.",
        ))
    for question, correct, wrong, diff, expl in VENTE:
        qs.append(Q(question, correct, wrong, diff, "entrepreneuriat,vente", expl))
    for question, correct, wrong, diff, expl in DIGITAL:
        qs.append(Q(question, correct, wrong, diff, "entrepreneuriat,digital", expl))
    return qs
