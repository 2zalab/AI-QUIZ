# -*- coding: utf-8 -*-
"""Banque Innovation & IA : usages concrets pour les petites entreprises."""

from __future__ import annotations

from .common import cap, CHALLENGE, FACILE, MOYEN, Q, others

# besoin -> (solution, benefice principal, difficulte)
USAGES = {
    "repondre automatiquement aux questions frequentes des clients": (
        "Un chatbot ou agent conversationnel", "Repondre plus vite et a toute heure", FACILE),
    "traduire une fiche produit en anglais pour la vendre au Nigeria": (
        "Un outil de traduction automatique", "Gagner du temps et toucher un nouveau marche", FACILE),
    "rediger une premiere version d'annonce publicitaire": (
        "Une IA generative de texte", "Produire rapidement un brouillon a corriger ensuite", FACILE),
    "trier automatiquement les commandes recues par messagerie": (
        "Un outil d'automatisation des taches", "Reduire les erreurs et le temps de saisie", MOYEN),
    "savoir quels produits se vendent le mieux chaque semaine": (
        "Un tableau de bord de suivi des ventes", "Decider a partir de chiffres reels", MOYEN),
    "encaisser un client qui n'a pas d'argent liquide": (
        "Le paiement par mobile money", "Ne pas perdre la vente et garder une trace", FACILE),
    "permettre a un client de retrouver une fiche produit en magasin": (
        "Un code QR imprime sur l'etiquette", "Donner acces a l'information sans vendeur disponible", FACILE),
    "suivre la position d'une livraison en cours": (
        "La geolocalisation via une application", "Rassurer le client et optimiser les tournees", MOYEN),
    "sauvegarder le fichier client contre la perte d'un telephone": (
        "Une sauvegarde dans le cloud", "Retrouver ses donnees en cas d'incident", FACILE),
    "verifier l'identite d'un utilisateur avant un paiement": (
        "L'authentification a deux facteurs", "Reduire fortement le risque de fraude", MOYEN),
    "former ses employes sans les deplacer": (
        "Une plateforme de formation en ligne", "Reduire les couts et le temps de formation", MOYEN),
    "organiser une reunion avec un partenaire base a l'etranger": (
        "Une visioconference", "Echanger sans frais de deplacement", FACILE),
    "faire connaitre une boutique aupres des habitants du quartier": (
        "Une presence sur les reseaux sociaux locaux", "Toucher des clients proches a faible cout", FACILE),
    "montrer un meuble dans le salon du client avant l'achat": (
        "La realite augmentee", "Aider le client a se projeter et reduire les retours", CHALLENGE),
    "fabriquer une piece de rechange unique rapidement": (
        "Une imprimante 3D", "Produire a l'unite sans outillage industriel", MOYEN),
    "surveiller l'humidite d'un champ pour declencher l'irrigation": (
        "Des capteurs connectes", "Economiser l'eau et ameliorer les rendements", CHALLENGE),
    "photographier de grandes parcelles agricoles rapidement": (
        "Un drone", "Observer l'etat des cultures sans se deplacer partout", MOYEN),
    "identifier les clients qui n'ont pas commande depuis trois mois": (
        "Un logiciel de gestion de la relation client", "Relancer les clients endormis au bon moment", MOYEN),
    "eviter de ressaisir les factures a la main": (
        "La reconnaissance automatique de documents", "Gagner du temps et limiter les erreurs", MOYEN),
    "recommander des produits complementaires a un acheteur en ligne": (
        "Un systeme de recommandation", "Augmenter le panier moyen", MOYEN),
    "verifier qu'une information vue en ligne est vraie": (
        "La verification des sources", "Eviter de relayer une fausse information", FACILE),
    "proteger les acces des employes aux outils de l'entreprise": (
        "Une politique de mots de passe forts", "Reduire le risque de piratage", FACILE),
    "vendre a des clients situes dans une autre ville": (
        "Une boutique en ligne", "Elargir la zone de chalandise sans nouveau local", FACILE),
    "envoyer une information a tous ses clients d'un coup": (
        "Une newsletter ou une liste de diffusion", "Communiquer a grande echelle a faible cout", FACILE),
    "comprendre pourquoi les visiteurs quittent un site sans acheter": (
        "L'analyse du parcours utilisateur", "Corriger les points de blocage du tunnel de vente", CHALLENGE),
    "consulter un medecin depuis un village eloigne": (
        "La telemedecine", "Acceder aux soins sans long deplacement", MOYEN),
    "apprendre un metier depuis chez soi": (
        "Un cours en ligne (MOOC)", "Se former a son rythme et a moindre cout", FACILE),
    "faire signer un contrat a distance": (
        "La signature electronique", "Conclure plus vite sans deplacement", MOYEN),
    "eviter de perdre du temps a compter le stock a la main": (
        "Un logiciel de gestion de stock avec code-barres", "Suivre le stock en temps reel", MOYEN),
    "resumer un long document en quelques points": (
        "Une IA generative de texte", "Gagner du temps de lecture", MOYEN),
    "creer un visuel de communication sans graphiste": (
        "Un outil de creation graphique en ligne", "Produire des visuels corrects a faible cout", FACILE),
    "creer un site vitrine sans savoir programmer": (
        "Un outil no-code", "Etre visible en ligne rapidement", MOYEN),
    "reduire les erreurs de calcul dans les devis": (
        "Un tableur avec formules automatiques", "Fiabiliser les chiffres transmis aux clients", FACILE),
    "connaitre l'avis des clients apres un achat": (
        "Un questionnaire de satisfaction en ligne", "Ameliorer l'offre grace aux retours", FACILE),
    "gerer les plannings d'une equipe dispersee": (
        "Un agenda partage en ligne", "Coordonner sans reunions inutiles", FACILE),
    "travailler a plusieurs sur le meme document": (
        "Un document partage en ligne", "Eviter les versions multiples et les pertes", FACILE),
    "detecter une transaction bancaire anormale": (
        "Un systeme de detection automatique de fraude", "Limiter les pertes financieres", CHALLENGE),
    "identifier un client sans carte grace a son empreinte": (
        "La biometrie", "Securiser l'acces tout en simplifiant l'identification", MOYEN),
    "transcrire automatiquement une reunion en compte rendu": (
        "La reconnaissance vocale", "Gagner du temps de redaction", MOYEN),
    "repondre a un client anglophone quand on ne parle pas anglais": (
        "Un outil de traduction automatique", "Servir une clientele plus large", FACILE),
    "eviter que la caisse ne soit fausse en fin de journee": (
        "Un logiciel de caisse", "Suivre chaque vente et fiabiliser les comptes", FACILE),
    "prevoir les ventes de la saison prochaine": (
        "L'analyse des donnees historiques de vente", "Mieux dimensionner les achats et les stocks", CHALLENGE),
    "faire decouvrir un hotel avant la reservation": (
        "Une visite virtuelle", "Rassurer le client et augmenter les reservations", MOYEN),
    "reduire la consommation d'electricite d'un atelier": (
        "Des compteurs connectes et un suivi des consommations", "Identifier les gaspillages et economiser", CHALLENGE),
    "envoyer un rappel de rendez-vous aux clients": (
        "Un envoi automatique de SMS ou de notifications", "Reduire les rendez-vous manques", FACILE),
    "classer automatiquement des milliers de photos de produits": (
        "La reconnaissance d'images", "Traiter un grand volume sans travail manuel", CHALLENGE),
    "verifier la disponibilite d'un produit avant de se deplacer": (
        "Un catalogue en ligne mis a jour", "Eviter des deplacements inutiles au client", FACILE),
    "accepter des paiements depuis l'etranger": (
        "Une solution de paiement en ligne", "Servir la diaspora et les clients internationaux", MOYEN),
    "garder une trace ecrite de tous les echanges avec un client": (
        "Un logiciel CRM", "Assurer la continuite du suivi commercial", MOYEN),
    "reduire le temps d'attente au guichet": (
        "Un systeme de prise de rendez-vous en ligne", "Ameliorer l'experience client", MOYEN),
}


def build() -> list[Q]:
    qs: list[Q] = []
    solutions = sorted({v[0] for v in USAGES.values()})
    benefices = sorted({v[1] for v in USAGES.values()})
    besoins = list(USAGES.keys())
    for besoin, (solution, benefice, diff) in USAGES.items():
        qs.append(Q(
            f"Une petite entreprise veut {besoin}. Quelle solution numerique est la plus adaptee ?",
            solution, others(besoin, solutions), diff, "innovation,usages",
            f"Pour {besoin}, {solution.lower()} est la reponse la plus directe.",
        ))
        qs.append(Q(
            f"Quel est le principal benefice de cette demarche : {besoin} ?",
            benefice, others(besoin + "b", benefices), diff, "innovation,usages",
            f"Le gain principal : {benefice.lower()}.",
        ))
        qs.append(Q(
            f"A quel besoin repond principalement cette solution : {solution} ?",
            cap(besoin), others(solution, [cap(b) for b in besoins]), diff,
            "innovation,usages", f"{solution} sert notamment a {besoin}.",
        ))
    return qs
