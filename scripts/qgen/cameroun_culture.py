# -*- coding: utf-8 -*-
"""Banque Cameroun : gastronomie, peuples, langues, tourisme et traditions."""

from __future__ import annotations

from .common import cap, CHALLENGE, FACILE, MOYEN, Q, others

REGIONS_LIST = ["Le Littoral", "Le Centre", "L'Ouest", "Le Nord-Ouest", "Le Sud-Ouest",
                "Le Sud", "L'Est", "Le Nord", "L'Extreme-Nord", "L'Adamaoua"]

# plat -> (region d'origine, ingredient principal, difficulte)
PLATS = {
    "le ndole": ("Le Littoral", "les feuilles de ndole et l'arachide", FACILE),
    "le poulet DG": ("Le Littoral", "le poulet et la banane plantain", FACILE),
    "l'eru": ("Le Sud-Ouest", "les feuilles d'eru et le waterleaf", MOYEN),
    "l'achu": ("Le Nord-Ouest", "le taro pile et la soupe jaune", MOYEN),
    "le koki": ("Le Centre", "les haricots ecrases", MOYEN),
    "le kondre": ("L'Ouest", "la banane plantain et la viande", MOYEN),
    "le mbongo tchobi": ("Le Littoral", "les epices noires grillees et le poisson", MOYEN),
    "le nkui": ("L'Ouest", "des ecorces et racines qui rendent la sauce visqueuse", CHALLENGE),
    "l'okok": ("Le Sud", "les feuilles de gnetum", MOYEN),
    "le nnam owondo": ("Le Sud", "la pate d'arachide cuite en feuilles", CHALLENGE),
    "le bobolo": ("Le Centre", "le manioc fermente", FACILE),
    "le miondo": ("Le Littoral", "le manioc fermente en petits batons", MOYEN),
    "le water fufu": ("Le Sud-Ouest", "le manioc trempe", MOYEN),
    "le njama njama": ("Le Nord-Ouest", "la morelle noire, un legume-feuille", MOYEN),
    "le kwacoco": ("Le Sud-Ouest", "le macabo rape", CHALLENGE),
    "le soya": ("Le Nord", "la viande de boeuf grillee et epicee en brochettes", FACILE),
    "le bil-bil": ("Le Nord", "le mil fermente", MOYEN),
    "la bouillie de mil": ("L'Extreme-Nord", "le mil", MOYEN),
    "le couscous de mais": ("Le Nord", "la farine de mais", MOYEN),
    "le taro sauce jaune": ("Le Nord-Ouest", "le taro et l'huile de palme aux epices", MOYEN),
    "le sanga": ("Le Centre", "le mais frais et les feuilles de manioc", CHALLENGE),
    "le mets de pistache": ("Le Centre", "les graines de courge (pistaches)", MOYEN),
    "le corn chaff": ("Le Sud-Ouest", "le mais et les haricots", CHALLENGE),
    "le katikati": ("Le Nord-Ouest", "le poulet grille a l'huile de palme", CHALLENGE),
    "le mbanga soup": ("Le Littoral", "la noix de palme", MOYEN),
    "le folong": ("Le Centre", "les feuilles d'amarante", MOYEN),
    "le kpwem": ("Le Sud", "les feuilles de manioc pilees", CHALLENGE),
    "le gari": ("Le Sud-Ouest", "la semoule de manioc", MOYEN),
    "les beignets haricots bouillie": ("Le Centre", "la farine de ble, les haricots et le mais", FACILE),
    "le pain charge": ("Le Littoral", "le pain garni de spaghetti et d'omelette", MOYEN),
    "le poisson braise": ("Le Littoral", "le poisson grille au feu de bois", FACILE),
    "le nkondre de chevre": ("L'Ouest", "la chevre et la banane plantain", CHALLENGE),
    "le matango": ("Le Littoral", "la seve du palmier", MOYEN),
    "le jus de foleré": ("L'Extreme-Nord", "les fleurs d'hibiscus", MOYEN),
    "le safou": ("Le Centre", "le fruit du safoutier", MOYEN),
    "le bongo chobi": ("Le Littoral", "les epices noires et le poisson", CHALLENGE),
}

# entreprise -> (secteur, description, difficulte)
ENTREPRISES = {
    "la SONARA": ("Le raffinage petrolier", "la raffinerie nationale installee a Limbe", MOYEN),
    "la SNH": ("Les hydrocarbures", "la societe nationale qui gere les interets petroliers de l'Etat", MOYEN),
    "CAMTEL": ("Les telecommunications", "l'operateur historique de telecommunications", FACILE),
    "CAMWATER": ("L'eau potable", "la societe publique de production et distribution d'eau", FACILE),
    "ENEO": ("L'electricite", "le principal distributeur d'electricite du pays", FACILE),
    "CAMRAIL": ("Le transport ferroviaire", "l'exploitant du reseau ferre camerounais", FACILE),
    "la CDC": ("L'agro-industrie", "un grand employeur agricole du Sud-Ouest (banane, hevea, palmier)", MOYEN),
    "la SODECOTON": ("Le coton", "la societe de developpement du coton dans le Nord", MOYEN),
    "la SOSUCAM": ("Le sucre", "la societe sucriere implantee a Mbandjock et Nkoteng", MOYEN),
    "ALUCAM": ("L'aluminium", "l'usine d'aluminium d'Edea", MOYEN),
    "la CICAM": ("Le textile", "l'industrie cotonniere textile du Cameroun", CHALLENGE),
    "Chococam": ("L'agroalimentaire", "le fabricant de chocolats et confiseries", MOYEN),
    "les Brasseries du Cameroun": ("Les boissons", "le principal brasseur du pays", FACILE),
    "Camair-Co": ("Le transport aerien", "la compagnie aerienne nationale", FACILE),
    "Afriland First Bank": ("La banque", "une banque camerounaise fondee par Paul Kammogne Fokam", MOYEN),
    "la BICEC": ("La banque", "une banque commerciale historique du Cameroun", MOYEN),
    "Express Union": ("Le transfert d'argent", "un reseau camerounais de transfert d'argent", MOYEN),
    "la SIC": ("L'immobilier", "la Societe Immobiliere du Cameroun", CHALLENGE),
    "la MAGZI": ("Les zones industrielles", "la mission d'amenagement des zones industrielles", CHALLENGE),
    "le PAD": ("La logistique portuaire", "le Port Autonome de Douala", MOYEN),
    "le PAK": ("La logistique portuaire", "le Port Autonome de Kribi", MOYEN),
    "Kiro'o Games": ("Le jeu video", "le studio camerounais createur d'Aurion", MOYEN),
    "Jumia Cameroun": ("Le commerce en ligne", "une plateforme de vente en ligne", FACILE),
    "la SNI": ("L'investissement public", "la Societe Nationale d'Investissement", CHALLENGE),
    "la CNPS": ("La protection sociale", "la caisse de prevoyance sociale des travailleurs", MOYEN),
    "Nexttel": ("La telephonie mobile", "le troisieme operateur mobile du pays", MOYEN),
    "Orange Cameroun": ("La telephonie mobile", "un operateur mobile et de mobile money", FACILE),
    "MTN Cameroon": ("La telephonie mobile", "un operateur mobile et de mobile money", FACILE),
    "la SABC": ("Les boissons", "le groupe des Brasseries du Cameroun", MOYEN),
    "Guinness Cameroun": ("Les boissons", "un brasseur installe a Douala", MOYEN),
    "la SEMC": ("Les eaux minerales", "le producteur de l'eau minerale Tangui", CHALLENGE),
    "Fokou": ("La distribution et la quincaillerie", "un grand groupe de distribution camerounais", CHALLENGE),
    "Cimencam": ("Le ciment", "un producteur historique de ciment au Cameroun", MOYEN),
    "Dangote Cement Cameroun": ("Le ciment", "une cimenterie du groupe nigerian Dangote a Douala", MOYEN),
    "Bocom": ("La distribution de carburants", "un groupe petrolier camerounais", CHALLENGE),
    "Tradex": ("La distribution de carburants", "un distributeur de produits petroliers", CHALLENGE),
}

SECTEURS = list({v[0] for v in ENTREPRISES.values()})

# peuple/langue -> region principale
PEUPLES = {
    "les Bamileke": "L'Ouest",
    "les Bamoun": "L'Ouest",
    "les Douala": "Le Littoral",
    "les Bassa": "Le Littoral",
    "les Ewondo": "Le Centre",
    "les Eton": "Le Centre",
    "les Bulu": "Le Sud",
    "les Fang": "Le Sud",
    "les Bakweri": "Le Sud-Ouest",
    "les Bakossi": "Le Sud-Ouest",
    "les Nso": "Le Nord-Ouest",
    "les Kom": "Le Nord-Ouest",
    "les Bafut": "Le Nord-Ouest",
    "les Peuls (Foulbe)": "Le Nord",
    "les Toupouri": "L'Extreme-Nord",
    "les Massa": "L'Extreme-Nord",
    "les Kotoko": "L'Extreme-Nord",
    "les Mafa": "L'Extreme-Nord",
    "les Moundang": "L'Extreme-Nord",
    "les Arabes Choa": "L'Extreme-Nord",
    "les Gbaya": "L'Est",
    "les Maka": "L'Est",
    "les Baka": "L'Est",
    "les Mbororo": "L'Adamaoua",
    "les Tikar": "L'Adamaoua",
    "les Bakoko": "Le Littoral",
    "les Yambassa": "Le Centre",
    "les Mbo": "Le Littoral",
}

CULTURE = [
    ("Combien de langues nationales estime-t-on parler au Cameroun ?", "Plus de 250",
     ["Environ 12", "Environ 40", "Plus de 900"], MOYEN, "On denombre entre 250 et 280 langues au Cameroun."),
    ("Comment appelle-t-on l'argot urbain melangeant francais, anglais et langues locales au Cameroun ?",
     "Le camfranglais", ["Le wolof", "Le pidgin latin", "Le nouchi"], MOYEN,
     "Le camfranglais est tres present chez les jeunes urbains."),
    ("Quelle langue vehiculaire anglophone est tres parlee dans le Sud-Ouest et le Nord-Ouest ?",
     "Le pidgin english", ["Le swahili", "Le haoussa", "Le lingala"], MOYEN,
     "Le pidgin english sert de langue de communication courante."),
    ("Quelle langue vehiculaire est largement parlee dans le Grand Nord du Cameroun ?", "Le fulfulde",
     ["Le douala", "L'ewondo", "Le bassa"], MOYEN, "Le fulfulde est la langue des Peuls et sert de langue d'echange."),
    ("Quelle ecriture originale le sultan Njoya a-t-il inventee ?", "Le shu-mom",
     ["Le tifinagh", "Le geez", "Le nsibidi"], CHALLENGE, "L'ecriture bamoun shu-mom date de la fin du XIXe siecle."),
    ("Dans quelle ville se trouve le palais des sultans Bamoun ?", "Foumban",
     ["Bafoussam", "Dschang", "Bandjoun"], MOYEN, "Le palais royal de Foumban abrite un musee reconnu."),
    ("Quelle ville de l'Ouest est reputee pour son artisanat et ses sculptures sur bois ?", "Foumban",
     ["Kribi", "Limbe", "Maroua"], MOYEN, "Le village des artisans de Foumban est celebre."),
    ("Quelle chefferie traditionnelle de l'Ouest est celebre pour son musee et sa case a poteaux sculptes ?",
     "La chefferie de Bandjoun", ["La chefferie de Bafut", "Le palais de Foumban", "La chefferie de Rey Bouba"], CHALLENGE,
     "La chefferie Bandjoun est un joyau du patrimoine Bamileke."),
    ("Comment appelle-t-on la fete traditionnelle des Bamoun celebree a Foumban ?", "Le Nguon",
     ["Le Ngondo", "Le Medumba", "Le Fete du Mbaya"], MOYEN, "Le Nguon est inscrit au patrimoine immateriel de l'UNESCO."),
    ("Comment s'appelle la grande fete traditionnelle du peuple Sawa a Douala ?", "Le Ngondo",
     ["Le Nguon", "Le Fet'Afrik", "Le Medumba"], MOYEN, "Le Ngondo se tient chaque annee au bord du Wouri."),
    ("Quelle course de pirogues est associee au festival Ngondo ?", "La course de pirogues sur le Wouri",
     ["La course sur la Sanaga", "La regate de Kribi", "La traversee du lac Nyos"], CHALLENGE,
     "Les courses de pirogues sont un temps fort du Ngondo."),
    ("Quel festival culturel camerounais est dedie aux arts et cultures du Grand Nord a Maroua ?", "Le FESTAM",
     ["Le Ngondo", "Le Nguon", "Le FEMUA"], CHALLENGE, "Le Festival des Arts de Maroua valorise les cultures septentrionales."),
    ("Quel musee national se trouve dans l'ancien palais presidentiel a Yaounde ?", "Le Musee national du Cameroun",
     ["Le Musee maritime de Douala", "Le Musee royal de Foumban", "Le Musee de Limbe"], MOYEN,
     "Le Musee national occupe l'ancien palais presidentiel."),
    ("Quel monument de Yaounde symbolise l'union entre les deux Cameroun ?", "Le monument de la Reunification",
     ["La cathedrale Notre-Dame des Victoires", "Le rond-point Deido", "Le monument Nachtigal"], MOYEN,
     "Le monument de la Reunification a ete erige a Yaounde."),
    ("Quelle colline de Yaounde offre une vue panoramique et abrite un palais ?", "Le mont Febe",
     ["Le mont Oku", "La colline de Deido", "Le mont Kupe"], CHALLENGE, "Le mont Febe domine la capitale."),
    ("Quel rocher emblematique se trouve sur la cote de Kribi ?", "Le Rocher du Loup",
     ["Le Rocher du Lion", "La Pierre de Buea", "Le Rocher de Manoka"], CHALLENGE,
     "Le Rocher du Loup est un site touristique de Kribi."),
    ("Quel centre camerounais, pres de Belabo, accueille des chimpanzes orphelins ?", "Le centre de Sanaga-Yong",
     ["Le zoo de Mvog-Betsi", "Le parc de Waza", "Le jardin botanique de Limbe"], CHALLENGE,
     "Le centre Sanaga-Yong, dans la region de l'Est, recueille des chimpanzes orphelins."),
    ("Quel jeu de societe traditionnel se joue avec des graines dans des cavites au Cameroun ?", "Le songo",
     ["Le mancala europeen", "Le senet", "Le go"], CHALLENGE, "Le songo est une variante camerounaise de l'awale."),
    ("Quelle danse traditionnelle est associee aux Grassfields du Nord-Ouest ?", "Le njang",
     ["Le makossa", "Le bikutsi", "L'assiko"], CHALLENGE, "Le njang accompagne les ceremonies dans le Nord-Ouest."),
    ("Que designe une chefferie traditionnelle au Cameroun ?",
     "Une institution coutumiere dirigee par un chef reconnu par sa communaute",
     ["Une entreprise publique", "Une cooperative agricole", "Une prefecture administrative"], FACILE,
     "Les chefferies sont reconnues comme auxiliaires de l'administration."),
    ("Comment appelle-t-on le chef traditionnel chez les Bamileke ?", "Le Fon ou le Chef superieur",
     ["Le Lamido", "L'Emir", "Le Cheikh"], MOYEN, "Les Grassfields parlent de Fon, les Bamileke de chef superieur."),
    ("Comment appelle-t-on le chef traditionnel peul dans le Nord du Cameroun ?", "Le Lamido",
     ["Le Fon", "Le Sultan de Douala", "Le Mfon Sawa"], MOYEN, "Le lamidat est l'institution traditionnelle peule."),
    ("Quel lamidat du Nord est reste celebre pour son autonomie historique ?", "Le lamidat de Rey Bouba",
     ["Le lamidat de Kribi", "Le lamidat de Bafang", "Le lamidat de Buea"], CHALLENGE,
     "Rey Bouba, dans le Mayo-Rey, est un lamidat puissant."),
    ("Quelle association de solidarite financiere informelle est tres repandue au Cameroun ?", "La tontine",
     ["La bourse", "La mutuelle europeenne", "Le fonds souverain"], FACILE,
     "La tontine est un pilier de l'epargne communautaire camerounaise."),
    ("A quoi sert principalement une tontine au Cameroun ?",
     "A epargner en groupe et financer les projets des membres a tour de role",
     ["A payer les impots de l'Etat", "A organiser des competitions sportives", "A distribuer des diplomes"], FACILE,
     "La tontine mobilise l'epargne collective et finance des projets."),
    ("Quelle boisson traditionnelle est tiree de la seve du palmier ?", "Le vin de palme (matango)",
     ["Le bil-bil", "Le foleré", "L'odontol"], MOYEN, "Le matango est recolte directement sur le palmier."),
    ("Quelle boisson traditionnelle du Nord est brassee a partir du mil ?", "Le bil-bil",
     ["Le matango", "Le safou", "Le gari"], MOYEN, "Le bil-bil est une biere de mil."),
    ("Quel marche de Douala est l'un des plus grands marches populaires du pays ?", "Le marche de Mboppi",
     ["Le marche Mokolo de Yaounde", "Le marche de Foumban", "Le marche central de Garoua"], MOYEN,
     "Mboppi est un immense marche de Douala."),
    ("Quel grand marche populaire se trouve a Yaounde ?", "Le marche Mokolo",
     ["Le marche Mboppi", "Le marche de Limbe", "Le marche de Kumba"], MOYEN, "Mokolo est un marche majeur de Yaounde."),
    ("Quelle chaine de television publique diffuse au Cameroun ?", "La CRTV",
     ["La RTI", "L'ORTB", "La RTS"], FACILE, "Cameroon Radio Television est le media public national."),
    ("Quel evenement sportif populaire relie Douala a d'autres villes par la route ?", "Le Tour du Cameroun cycliste",
     ["Le Rallye du Wouri", "Le Marathon de Waza", "La Traversee du Ntem"], CHALLENGE,
     "Le Tour cycliste international du Cameroun est une competition annuelle."),
    ("Quelle universite camerounaise est situee dans la ville de Buea ?", "L'Universite de Buea",
     ["L'Universite de Douala", "L'Universite de Dschang", "L'Universite de Ngaoundere"], FACILE,
     "L'Universite de Buea est la premiere universite anglophone du pays."),
    ("Quelle grande ecole camerounaise forme les ingenieurs a Yaounde ?", "L'Ecole Nationale Superieure Polytechnique",
     ["L'ENAM", "L'ESSEC", "L'IRIC"], MOYEN, "L'ENSP forme les ingenieurs a Yaounde."),
    ("Que forme l'ENAM au Cameroun ?", "Les cadres de l'administration et de la magistrature",
     ["Les pilotes de ligne", "Les medecins specialistes", "Les journalistes sportifs"], MOYEN,
     "L'Ecole Nationale d'Administration et de Magistrature."),
    ("Quelle ecole de commerce publique est rattachee a l'Universite de Douala ?", "L'ESSEC de Douala",
     ["L'ENSP", "L'IRIC", "L'ENAM"], CHALLENGE, "L'ESSEC de Douala forme aux metiers de la gestion."),
    ("Combien d'universites d'Etat le Cameroun compte-t-il aujourd'hui ?", "Onze",
     ["Trois", "Six", "Vingt"], CHALLENGE,
     "Aux huit universites historiques se sont ajoutees Bertoua, Ebolowa et Garoua."),
    ("Quelle est la premiere universite creee au Cameroun ?", "L'Universite de Yaounde",
     ["L'Universite de Douala", "L'Universite de Buea", "L'Universite de Dschang"], MOYEN,
     "L'Universite federale de Yaounde a ete creee en 1962."),
    ("Quel examen sanctionne la fin du cycle secondaire francophone au Cameroun ?", "Le baccalaureat",
     ["Le GCE A Level uniquement", "Le CAP uniquement", "Le brevet des colleges"], FACILE,
     "Le sous-systeme francophone delivre le baccalaureat."),
    ("Quel diplome sanctionne le cycle secondaire anglophone au Cameroun ?", "Le GCE Advanced Level",
     ["Le baccalaureat", "Le BEPC", "Le CEP"], MOYEN, "Le General Certificate of Education est delivre par le GCE Board."),
]


def build() -> list[Q]:
    qs: list[Q] = []
    noms_plats = list(PLATS.keys())

    for plat, (region, ingredient, diff) in PLATS.items():
        qs.append(Q(
            f"De quelle region du Cameroun {plat} est-il originaire ou le plus consomme ?",
            region, others(plat, REGIONS_LIST), diff, "cameroun,gastronomie",
            f"{cap(plat)} est surtout associe a cette region.",
        ))
        qs.append(Q(
            f"Quel est l'ingredient principal utilise pour preparer {plat} ?",
            ingredient, others(plat + "ing", [v[1] for v in PLATS.values()]), diff,
            "cameroun,gastronomie", f"{cap(plat)} se prepare avec {ingredient}.",
        ))

    qs.append(Q("Quel plat est souvent presente comme le plat national du Cameroun ?", "Le ndole",
                ["Le couscous royal", "Le thieboudienne", "Le foutou"], FACILE, "cameroun,gastronomie",
                "Le ndole est le plat emblematique du Cameroun."))
    qs.append(Q("Que veut dire DG dans l'expression poulet DG ?", "Directeur General",
                ["Douala Grille", "Dinde Grillee", "Delice Gourmand"], MOYEN, "cameroun,gastronomie",
                "Le poulet DG etait juge digne d'un directeur general."))

    for entreprise, (secteur, description, diff) in ENTREPRISES.items():
        qs.append(Q(
            f"Dans quel secteur d'activite intervient {entreprise} ?",
            secteur, others(entreprise, SECTEURS), diff, "cameroun,economie,entreprises",
            f"{cap(entreprise)} est {description}.",
        ))
        qs.append(Q(
            f"Quelle entreprise camerounaise correspond a cette description : {description} ?",
            entreprise, others(description, list(ENTREPRISES.keys())), diff,
            "cameroun,economie,entreprises", f"Il s'agit de {entreprise}.",
        ))

    for peuple, region in PEUPLES.items():
        qs.append(Q(
            f"Dans quelle region du Cameroun {peuple} sont-ils principalement etablis ?",
            region, others(peuple, REGIONS_LIST), MOYEN, "cameroun,peuples,langues",
            f"{cap(peuple)} vivent principalement dans cette region.",
        ))

    for question, correct, wrong, diff, expl in CULTURE:
        qs.append(Q(question, correct, wrong, diff, "cameroun,culture", expl))

    return qs
