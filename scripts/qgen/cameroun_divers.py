# -*- coding: utf-8 -*-
"""Banque Cameroun : vie quotidienne, expressions, marques, sport et divers."""

from __future__ import annotations

from .common import cap, CHALLENGE, FACILE, MOYEN, Q, others

# club -> (ville, region)
CLUBS = {
    "Coton Sport": ("Garoua", "Le Nord"),
    "Canon Sportif": ("Yaounde", "Le Centre"),
    "Tonnerre Kalara Club": ("Yaounde", "Le Centre"),
    "Union Sportive": ("Douala", "Le Littoral"),
    "Dynamo": ("Douala", "Le Littoral"),
    "Aigle Royal": ("Dschang", "L'Ouest"),
    "PWD": ("Bamenda", "Le Nord-Ouest"),
    "Fovu Club": ("Baham", "L'Ouest"),
    "Bamboutos FC": ("Mbouda", "L'Ouest"),
    "Victoria United": ("Limbe", "Le Sud-Ouest"),
    "UMS": ("Loum", "Le Littoral"),
    "Astres FC": ("Douala", "Le Littoral"),
    "Renaissance FC": ("Ngoumou", "Le Centre"),
    "Stade Renard": ("Melong", "Le Littoral"),
}
VILLES_CLUBS = sorted({v[0] for v in CLUBS.values()})

# expression -> (sens, difficulte)
EXPRESSIONS = {
    "un mbindi": ("Un petit, un cadet ou un jeune", FACILE),
    "le njoh": ("Quelque chose d'obtenu gratuitement", FACILE),
    "un tara": ("Un ami, un pote", FACILE),
    "ashia": ("Une formule de compassion ou d'encouragement", FACILE),
    "un kombi": ("Un ami proche, un complice", FACILE),
    "le gombo": ("Un petit contrat ou un revenu d'appoint", MOYEN),
    "un call box": ("Un point de vente de credit telephonique dans la rue", FACILE),
    "un sauveteur": ("Un petit commercant qui vend au bord de la route", FACILE),
    "un bendskin": ("Un moto-taxi", FACILE),
    "un clando": ("Un taxi ou vehicule de transport non officiel", MOYEN),
    "une opep": ("Un vehicule de transport en commun surcharge", MOYEN),
    "le ndem": ("La malchance, la poisse", MOYEN),
    "la sissia": ("L'intimidation, le fait de faire peur", MOYEN),
    "tchouker": ("Payer ou glisser discretement de l'argent", MOYEN),
    "un mola": ("Un ami, un frere (langage de la rue)", MOYEN),
    "un bosso": ("Un patron ou un homme respecte", MOYEN),
    "le tchop": ("La nourriture, le fait de manger", FACILE),
    "un ngata": ("La prison", CHALLENGE),
    "un mbenguiste": ("Un Camerounais vivant a l'etranger", MOYEN),
    "le mbeng": ("L'Europe ou l'etranger", MOYEN),
    "un bayam-sellam": ("Un revendeur, souvent une commercante de vivres", MOYEN),
    "le tchakala": ("Ce qui est de mauvaise qualite ou bricole", CHALLENGE),
    "faire le wandah": ("S'etonner, etre surpris", CHALLENGE),
    "un pia": ("De l'argent", MOYEN),
    "la demarche": ("Une combine ou un arrangement pour obtenir quelque chose", MOYEN),
}

# marque -> (secteur, entreprise/precision, difficulte)
MARQUES = {
    "33 Export": ("Une biere", "elle est produite par les Brasseries du Cameroun", FACILE),
    "Mutzig": ("Une biere", "elle est brassee au Cameroun sous licence", MOYEN),
    "Beaufort": ("Une biere", "elle appartient au portefeuille des Brasseries du Cameroun", MOYEN),
    "Kadji Beer": ("Une biere", "elle est produite par le groupe Kadji", MOYEN),
    "Tangui": ("Une eau minerale", "elle est produite par la SEMC", FACILE),
    "Supermont": ("Une eau minerale", "elle est embouteillee au Cameroun", FACILE),
    "Top": ("Une boisson gazeuse", "elle est declinee en plusieurs parfums fruites", FACILE),
    "Djino": ("Une boisson gazeuse", "elle est tres populaire dans les fetes", MOYEN),
    "Malta Guinness": ("Une boisson maltee sans alcool", "elle est produite par Guinness Cameroun", MOYEN),
    "Mambo": ("Un chocolat a tartiner", "il est produit par Chococam", FACILE),
    "Tartina": ("Une pate a tartiner", "elle est produite par Chococam", MOYEN),
    "Orange Money": ("Un service de mobile money", "il permet de payer et transferer de l'argent", FACILE),
    "MTN MoMo": ("Un service de mobile money", "il permet de payer et transferer de l'argent", FACILE),
    "Camtel Blue": ("Un service de telecommunication", "il est propose par l'operateur historique CAMTEL", CHALLENGE),
}
SECTEURS_MARQUES = sorted({v[0] for v in MARQUES.values()})

DIVERS = [
    ("Comment surnomme-t-on la ville de Yaounde ?", "La ville aux sept collines",
     ["La perle du Sud", "La cite des arts", "La capitale du Nord"], MOYEN, "Yaounde est batie sur plusieurs collines."),
    ("Comment surnomme-t-on la ville de Kribi ?", "La perle du Sud",
     ["La ville aux sept collines", "Abakwa", "La cite des arts"], MOYEN, "Kribi est reputee pour ses plages."),
    ("Comment surnomme-t-on la ville de Foumban ?", "La cite des arts",
     ["La perle du Sud", "La ville climatique", "Abakwa"], MOYEN, "Foumban est le berceau de l'artisanat bamoun."),
    ("Quel surnom populaire designe la ville de Bamenda ?", "Abakwa",
     ["Ngola", "La perle du Sud", "La cite des arts"], CHALLENGE, "Abakwa est le surnom familier de Bamenda."),
    ("Quelle ville de l'Ouest est surnommee la ville climatique en raison de sa fraicheur ?", "Dschang",
     ["Bafoussam", "Bandjoun", "Foumbot"], MOYEN, "Dschang est reputee pour son climat frais."),
    ("Comment s'appelait la ville de Limbe avant 1982 ?", "Victoria",
     ["Tiko", "Buea", "Bota"], CHALLENGE, "Limbe s'appelait Victoria a l'epoque britannique."),
    ("Comment s'appelait la ville de Kousseri pendant la periode coloniale francaise ?", "Fort-Foureau",
     ["Fort-Lamy", "Fort-Archambault", "Fort-Sibut"], CHALLENGE, "Kousseri portait le nom de Fort-Foureau."),
    ("Quelle est la ville la plus peuplee du Cameroun ?", "Douala",
     ["Yaounde", "Bafoussam", "Garoua"], FACILE, "Douala est la ville la plus peuplee du pays."),
    ("Quelles sont les deux plus grandes villes du Cameroun ?", "Douala et Yaounde",
     ["Yaounde et Bafoussam", "Douala et Garoua", "Bamenda et Maroua"], FACILE,
     "Douala et Yaounde depassent chacune deux millions d'habitants."),
    ("Quel pont emblematique relie les deux rives de Douala ?", "Le pont sur le Wouri",
     ["Le pont de la Sanaga", "Le pont du Nyong", "Le pont de Bakassi"], FACILE, "Le pont sur le Wouri est un symbole de Douala."),
    ("Quel quartier de Douala est connu pour ses activites nocturnes et sa vie animee ?", "Akwa",
     ["Nsimalen", "Melen", "Mvog-Ada"], MOYEN, "Akwa concentre hotels, bars et commerces."),
    ("Quel quartier administratif de Yaounde regroupe de nombreux ministeres ?", "Le quartier du Lac / centre administratif",
     ["Akwa", "Bonaberi", "Deido"], CHALLENGE, "Le centre administratif de Yaounde accueille les ministeres."),
    ("Quel moyen de transport urbain populaire est appele moto-taxi au Cameroun ?", "Le bendskin",
     ["Le clando", "L'opep", "Le pousse-pousse"], FACILE, "Le bendskin est le moto-taxi camerounais."),
    ("Quelle est la couleur traditionnelle des taxis a Douala et Yaounde ?", "Le jaune",
     ["Le bleu", "Le vert", "Le rouge"], FACILE, "Les taxis urbains camerounais sont jaunes."),
    ("Quelle grande religion est majoritaire dans le Grand Nord du Cameroun ?", "L'islam",
     ["Le bouddhisme", "L'hindouisme", "Le shintoisme"], FACILE, "Le Nord est majoritairement musulman."),
    ("Quelles sont les deux grandes religions les plus pratiquees au Cameroun ?",
     "Le christianisme et l'islam", ["Le bouddhisme et l'hindouisme", "Le judaisme et le shintoisme",
      "Le taoisme et le sikhisme"], FACILE, "Christianisme et islam coexistent avec les religions traditionnelles."),
    ("Quelle langue est enseignee comme seconde langue officielle dans les ecoles francophones ?", "L'anglais",
     ["L'espagnol", "L'allemand", "Le chinois"], FACILE, "Le bilinguisme est encourage dans le systeme educatif."),
    ("Quel document d'identite national les Camerounais majeurs doivent-ils posseder ?",
     "La carte nationale d'identite", ["Le passeport diplomatique", "La carte de sejour", "Le livret de famille"], FACILE,
     "La CNI est le document d'identite de base."),
    ("Quel indicatif telephonique international correspond au Cameroun ?", "+237",
     ["+225", "+229", "+241"], MOYEN, "L'indicatif du Cameroun est le +237."),
    ("Quel est le nom du domaine internet national du Cameroun ?", ".cm",
     [".cd", ".ca", ".cr"], MOYEN, "Le domaine de premier niveau camerounais est le .cm."),
    ("Quel fuseau horaire s'applique au Cameroun ?", "UTC+1",
     ["UTC-2", "UTC+3", "UTC+0"], MOYEN, "Le Cameroun est a UTC+1 toute l'annee."),
    ("Quelle saison domine de novembre a fevrier dans le Nord du Cameroun ?", "La saison seche",
     ["La saison des pluies", "L'hiver neigeux", "La mousson"], FACILE, "Le Nord connait une longue saison seche."),
    ("Quel evenement religieux annuel rassemble de nombreux fideles a Marienberg, au Cameroun ?",
     "Le pelerinage marial", ["Le Nguon", "Le Ngondo", "Le Festival Ecrans Noirs"], CHALLENGE,
     "Marienberg, dans la Sanaga-Maritime, est un lieu de pelerinage."),
    ("Quel festival de cinema se tient chaque annee a Yaounde ?", "Ecrans Noirs",
     ["Le FESPACO", "Le Ngondo", "Le FEMUA"], MOYEN, "Ecrans Noirs valorise le cinema africain."),
    ("Quel journal quotidien public parait au Cameroun ?", "Cameroon Tribune",
     ["Le Monde", "Jeune Afrique", "The Guardian"], FACILE, "Cameroon Tribune est le quotidien national bilingue."),
    ("Quel service national assure la distribution du courrier au Cameroun ?", "CAMPOST",
     ["CAMTEL", "CAMRAIL", "CAMWATER"], MOYEN, "La Cameroon Postal Services gere le courrier."),
    ("Quel numero appelle-t-on pour joindre la police au Cameroun ?", "Le 117",
     ["Le 15", "Le 911", "Le 100"], MOYEN, "Le 117 est le numero de la police."),
    ("Quel numero appelle-t-on pour joindre les sapeurs-pompiers au Cameroun ?", "Le 118",
     ["Le 18", "Le 112", "Le 911"], CHALLENGE, "Le 118 correspond aux sapeurs-pompiers."),
    ("Quelle plante sert a fabriquer les paniers et nattes artisanales dans plusieurs regions ?", "Le raphia",
     ["Le cactus", "Le sapin", "Le ble"], MOYEN, "Le raphia est tres utilise dans l'artisanat camerounais."),
    ("Quel tissu traditionnel est associe aux chefferies de l'Ouest du Cameroun ?", "Le ndop",
     ["Le bogolan", "Le kente", "Le wax hollandais"], MOYEN, "Le tissu ndop, indigo et blanc, orne les ceremonies."),
    ("Quel vetement traditionnel masculin est courant dans le Nord du Cameroun ?", "Le gandoura (boubou)",
     ["Le kilt", "Le kimono", "Le poncho"], MOYEN, "Le gandoura est porte dans les regions septentrionales."),
    ("Comment appelle-t-on le pagne porte par les femmes lors des ceremonies au Cameroun ?", "Le kaba ngondo ou pagne",
     ["Le sari", "Le sarong", "Le hanbok"], MOYEN, "Le kaba est une robe traditionnelle camerounaise."),
    ("Quelle activite economique domine autour du lac Tchad cote camerounais ?", "La peche et l'elevage",
     ["L'industrie automobile", "L'extraction de diamants", "La production de vin"], MOYEN,
     "Les riverains vivent de la peche, de l'elevage et du commerce."),
    ("Quel animal emblematique peut-on observer au parc de Waza ?", "L'elephant",
     ["Le pingouin", "Le kangourou", "L'ours polaire"], FACILE, "Waza abrite elephants, lions et antilopes."),
    ("Quel primate rare vit dans les forets du Sud-Ouest camerounais ?", "Le gorille de la Cross River",
     ["Le panda", "Le lemurien", "L'orang-outan"], CHALLENGE, "Le gorille de la Cross River est menace d'extinction."),
    ("Quel arbre est a l'origine du fruit appele safou au Cameroun ?", "Le safoutier",
     ["Le manguier", "Le cacaoyer", "Le palmier dattier"], MOYEN, "Le safou est le fruit du safoutier."),
    ("Quel produit forestier non ligneux est tres commercialise dans le Sud du Cameroun ?", "L'okok (gnetum)",
     ["Le coton", "Le ble", "Le riz"], CHALLENGE, "L'okok est recolte et exporte dans la sous-region."),
    ("Quel evenement sportif universitaire national rassemble les etudiants camerounais ?", "Les Jeux universitaires",
     ["Les Jeux du Commonwealth", "Les Jeux de la Francophonie", "Les Jeux olympiques"], MOYEN,
     "Les Jeux universitaires reunissent les universites d'Etat."),
    ("Quelle competition scolaire de football porte le nom d'un tournoi national des lycees et colleges ?",
     "Les Jeux FENASSCO", ["La Champions League", "La Coupe Davis", "Le Tournoi des Six Nations"], CHALLENGE,
     "La FENASSCO organise les competitions scolaires."),
    ("Quel est le nom de la coupe nationale de football au Cameroun ?", "La Coupe du Cameroun",
     ["La Coupe de la Ligue anglaise", "La Coupe du Congo", "La Coupe Amilcar Cabral"], FACILE,
     "La Coupe du Cameroun est la competition a elimination directe nationale."),
    ("Comment s'appelle le championnat de football professionnel camerounais ?", "L'Elite One",
     ["La Ligue 1 Orange", "La Premier League", "La Serie A"], MOYEN, "L'Elite One est la premiere division camerounaise."),
    ("Quelle federation gere le football au Cameroun ?", "La FECAFOOT",
     ["La FIFA nationale", "La CAF Cameroun", "La LFP"], FACILE, "La Federation Camerounaise de Football."),
]


def build() -> list[Q]:
    qs: list[Q] = []
    for club, (ville, region) in CLUBS.items():
        qs.append(Q(
            f"De quelle ville camerounaise le club de football {club} est-il originaire ?",
            ville, others(club, VILLES_CLUBS), MOYEN, "cameroun,sport",
            f"{club} est base a {ville}, dans la region : {region}.",
        ))
    for expr, (sens, diff) in EXPRESSIONS.items():
        qs.append(Q(
            f"Dans le langage populaire camerounais, que designe {expr} ?",
            sens, others(expr, [v[0] for v in EXPRESSIONS.values()]), diff,
            "cameroun,culture,expressions", f"{cap(expr)} : {sens.lower()}.",
        ))
    for marque, (secteur, precision, diff) in MARQUES.items():
        qs.append(Q(
            f"Que designe la marque camerounaise {marque} ?",
            secteur, others(marque, SECTEURS_MARQUES), diff, "cameroun,marques",
            f"{marque} : {precision}.",
        ))
    for question, correct, wrong, diff, expl in DIVERS:
        qs.append(Q(question, correct, wrong, diff, "cameroun,divers", expl))
    return qs
