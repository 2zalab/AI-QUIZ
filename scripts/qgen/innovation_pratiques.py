# -*- coding: utf-8 -*-
"""Banque Innovation & IA : cybersecurite, bonnes pratiques et mises en situation."""

from __future__ import annotations

from .common import cap, CHALLENGE, FACILE, MOYEN, Q, others

# situation a risque -> (bonne reaction, difficulte)
CYBER = {
    "vous recevez un SMS annoncant que vous avez gagne un prix et demandant votre code secret": (
        "Ne jamais communiquer son code et supprimer le message", FACILE),
    "un e-mail imite votre banque et demande de confirmer votre mot de passe": (
        "Ne pas cliquer et contacter la banque par un canal officiel", FACILE),
    "un inconnu vous appelle en se disant technicien et demande un code recu par SMS": (
        "Refuser de communiquer le code et raccrocher", FACILE),
    "vous utilisez le meme mot de passe pour tous vos comptes": (
        "Creer un mot de passe different pour chaque service", FACILE),
    "vous notez vos mots de passe sur un papier colle a l'ecran": (
        "Utiliser un gestionnaire de mots de passe securise", MOYEN),
    "un employe part de l'entreprise en gardant ses acces informatiques": (
        "Desactiver immediatement ses comptes et acces", MOYEN),
    "votre telephone professionnel n'a aucun code de verrouillage": (
        "Activer un code ou un verrouillage biometrique", FACILE),
    "vous vous connectez au wifi public d'un hotel pour consulter vos comptes": (
        "Eviter les operations sensibles sur un reseau public non securise", MOYEN),
    "un fichier joint inattendu arrive d'un expediteur inconnu": (
        "Ne pas l'ouvrir et verifier l'expediteur", FACILE),
    "votre logiciel affiche depuis des mois un message de mise a jour": (
        "Installer les mises a jour de securite sans tarder", FACILE),
    "vous n'avez aucune copie de votre fichier client": (
        "Mettre en place une sauvegarde reguliere et automatique", FACILE),
    "un site vous demande de payer sans afficher aucune mention legale": (
        "Ne pas payer et verifier l'identite du vendeur", MOYEN),
    "une application demande l'acces a tous vos contacts sans raison": (
        "Refuser l'autorisation inutile", MOYEN),
    "vous partagez publiquement une photo de votre carte bancaire": (
        "Ne jamais publier ses coordonnees bancaires en ligne", FACILE),
    "un collaborateur telecharge des logiciels piratés sur l'ordinateur de l'entreprise": (
        "Interdire cette pratique et n'installer que des logiciels legitimes", MOYEN),
    "votre boutique en ligne stocke les mots de passe clients en clair": (
        "Chiffrer les mots de passe et securiser la base de donnees", CHALLENGE),
    "un message urgent du dirigeant demande un virement immediat sans verification": (
        "Verifier la demande par un autre canal avant tout paiement", MOYEN),
    "vous jetez un ancien ordinateur sans effacer son disque": (
        "Effacer securise le disque avant de vous en separer", CHALLENGE),
}

SCENARIOS = [
    ("Une PME veut se lancer dans le numerique mais dispose d'un tres petit budget. Par quoi commencer ?",
     "Par un outil gratuit ou peu couteux qui resout son probleme le plus urgent",
     ["Par l'achat d'un logiciel sur mesure a plusieurs millions",
      "Par le recrutement d'une equipe informatique complete",
      "Par la construction d'un centre de donnees"], FACILE,
     "On commence par le besoin le plus douloureux, avec un outil simple."),
    ("Un commercant veut utiliser l'IA pour repondre a ses clients la nuit. Quelle solution simple ?",
     "Mettre en place un agent conversationnel repondant aux questions frequentes",
     ["Recruter cinq employes de nuit immediatement", "Fermer le service client",
      "Supprimer les questions des clients"], FACILE, "Le chatbot couvre les questions repetitives 24 h/24."),
    ("Une entreprise utilise une IA pour rediger ses contrats. Quelle precaution est indispensable ?",
     "Faire relire le contrat par une personne competente avant signature",
     ["Signer immediatement sans relecture", "Publier le contrat sans le lire",
      "Supprimer toute relecture pour gagner du temps"], MOYEN,
     "La supervision humaine reste obligatoire sur les documents engageants."),
    ("Un restaurant recoit beaucoup d'avis negatifs en ligne. Quelle demarche adopter ?",
     "Repondre publiquement, corriger les problemes reels et suivre l'evolution",
     ["Supprimer son compte", "Acheter de faux avis positifs",
      "Insulter les clients mecontents"], MOYEN, "La e-reputation se travaille par des actions reelles."),
    ("Une cooperative agricole veut mieux prevoir ses recoltes. Quel usage numerique est pertinent ?",
     "Suivre les donnees meteo et les rendements passes pour planifier",
     ["Publier des photos sur les reseaux uniquement", "Acheter un drone de loisir sans usage defini",
      "Ignorer completement les donnees"], MOYEN, "Le pilotage par la donnee ameliore la planification."),
    ("Un artisan veut vendre au-dela de son quartier sans site web complexe. Quelle option realiste ?",
     "Utiliser une page professionnelle sur un reseau social et le mobile money",
     ["Developper une application mobile complete d'emblee",
      "Ouvrir dix boutiques physiques", "Attendre d'avoir un million de FCFA"], FACILE,
     "Les canaux existants permettent de demarrer sans developpement."),
    ("Une entreprise veut automatiser ses relances de factures impayees. Quelle approche ?",
     "Programmer des rappels automatiques a partir de son outil de gestion",
     ["Attendre que les clients paient spontanement", "Appeler chaque client au hasard",
      "Renoncer aux creances"], MOYEN, "L'automatisation des relances ameliore la tresorerie."),
    ("Un centre de formation veut toucher des apprenants eloignes. Quelle solution ?",
     "Proposer des cours en ligne accessibles depuis un telephone",
     ["Construire dix nouveaux batiments", "Limiter les inscriptions",
      "Supprimer les supports pedagogiques"], FACILE, "Le e-learning reduit la contrainte de distance."),
    ("Une entreprise hesite a adopter un nouvel outil numerique. Quel test raisonnable ?",
     "Le tester sur une equipe pilote avant de le generaliser",
     ["L'imposer immediatement a tout le monde", "L'acheter sans essai",
      "Ne jamais rien changer"], MOYEN, "Le pilote limite le risque de rejet et de perte financiere."),
    ("Un service client recoit toujours les memes questions. Que faire en priorite ?",
     "Publier une foire aux questions et automatiser les reponses courantes",
     ["Ignorer les clients", "Repondre plus lentement",
      "Supprimer le service client"], FACILE, "La FAQ libere du temps pour les demandes complexes."),
    ("Une entreprise veut utiliser l'IA pour trier des candidatures. Quel risque doit-elle anticiper ?",
     "Le risque de biais reproduisant des discriminations passees",
     ["Le risque de recruter trop vite", "Le risque d'avoir trop de candidats",
      "Aucun risque particulier"], CHALLENGE, "Les biais algorithmiques sont un enjeu majeur en recrutement."),
    ("Un dirigeant veut mesurer l'effet de sa page en ligne sur ses ventes. Que met-il en place ?",
     "Un suivi des demandes et commandes provenant de cette page",
     ["Un comptage des couleurs utilisees", "Un sondage aupres de sa famille",
      "Rien, l'intuition suffit"], MOYEN, "Le lien entre canal et vente doit etre mesure."),
    ("Une boutique en ligne perd des clients au moment du paiement. Quelle piste explorer ?",
     "Simplifier le processus et proposer des moyens de paiement locaux",
     ["Augmenter le prix", "Ajouter cinq etapes supplementaires",
      "Supprimer le paiement en ligne"], MOYEN, "L'abandon de panier vient souvent d'un paiement complique."),
    ("Une PME veut proteger ses donnees contre la perte. Quelle mesure de base ?",
     "Sauvegarder regulierement, avec au moins une copie hors du local",
     ["Garder une seule copie sur un ordinateur", "Imprimer toutes les donnees",
      "Ne rien sauvegarder"], FACILE, "La regle de base : plusieurs copies, dont une externalisee."),
    ("Un employe utilise une IA pour rediger des e-mails clients. Quelle regle poser ?",
     "Verifier le contenu et ne jamais y saisir d'informations confidentielles sensibles",
     ["Envoyer sans relire", "Y saisir tous les mots de passe de l'entreprise",
      "Interdire toute relecture"], MOYEN, "Verification et confidentialite sont les deux regles cles."),
    ("Une entreprise veut savoir si un investissement numerique a ete rentable. Que compare-t-elle ?",
     "Le cout total de la solution et les gains mesures qu'elle a apportes",
     ["Le nombre d'ecrans installes", "Le nombre de logiciels achetes",
      "L'avis du fournisseur uniquement"], MOYEN, "Le retour sur investissement se mesure en gains reels."),
    ("Une equipe refuse d'utiliser un nouvel outil impose. Quelle est la cause la plus probable ?",
     "Un manque d'explication, de formation ou d'utilite percue",
     ["Une trop grande facilite d'usage", "Un outil trop bien documente",
      "Une formation trop complete"], MOYEN, "L'adoption depend du sens et de l'accompagnement."),
    ("Une entreprise veut lancer une application mobile. Quelle question poser en premier ?",
     "Les clients ont-ils vraiment besoin d'une application plutot que d'un site simple ?",
     ["Quelle couleur choisir pour l'icone ?", "Combien de developpeurs recruter ?",
      "Quel nom de serveur utiliser ?"], MOYEN, "Le besoin reel precede le choix technique."),
    ("Un entrepreneur veut proteger une invention technique. Quelle demarche ?",
     "Deposer un brevet aupres de l'organisme competent",
     ["Publier tous les details en ligne", "Ne rien faire",
      "Vendre l'idee sans contrat"], MOYEN, "Le brevet protege l'invention pour une duree limitee."),
    ("Une entreprise stocke les donnees de ses clients. Quelle obligation morale et legale ?",
     "Les proteger, ne collecter que le necessaire et informer les personnes",
     ["Les revendre au plus offrant", "Les publier en ligne",
      "Les partager avec les concurrents"], MOYEN, "La protection des donnees personnelles est une responsabilite."),
]


def build() -> list[Q]:
    qs: list[Q] = []
    reactions = sorted({v[0] for v in CYBER.values()})
    for situation, (reaction, diff) in CYBER.items():
        qs.append(Q(
            f"Que faut-il faire dans cette situation : {situation} ?",
            reaction, others(situation, reactions), diff, "innovation,cybersecurite",
            f"Bonne pratique : {reaction.lower()}.",
        ))
        qs.append(Q(
            f"Quelle situation justifie cette bonne pratique : {reaction} ?",
            cap(situation), others(reaction, [cap(s) for s in CYBER]), diff,
            "innovation,cybersecurite", f"Cette pratique repond au cas suivant : {situation}.",
        ))
    for question, correct, wrong, diff, expl in SCENARIOS:
        qs.append(Q(question, correct, wrong, diff, "innovation,mise-en-situation", expl))
    return qs
