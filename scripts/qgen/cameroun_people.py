# -*- coding: utf-8 -*-
"""Banque Cameroun : personnalites (sport, musique, lettres, business, histoire)."""

from __future__ import annotations

from .common import CHALLENGE, FACILE, MOYEN, Q, others

DOMAINES = [
    "Le football", "La musique", "La litterature", "L'athletisme",
    "La politique", "Les affaires et l'entrepreneuriat", "La technologie",
    "Le cinema", "La lutte contre la colonisation", "La mode",
]

# nom -> (domaine, fait marquant, difficulte)
PERSONNALITES = {
    # Football
    "Roger Milla": ("Le football", "avoir marque quatre buts a la Coupe du monde 1990 avec sa danse au poteau de corner", FACILE),
    "Samuel Eto'o": ("Le football", "avoir remporte quatre fois le Ballon d'or africain avant de presider la FECAFOOT", FACILE),
    "Thomas N'Kono": ("Le football", "avoir ete un gardien legendaire, double Ballon d'or africain", MOYEN),
    "Rigobert Song": ("Le football", "avoir ete capitaine des Lions Indomptables puis leur selectionneur", MOYEN),
    "Marc-Vivien Foe": ("Le football", "etre un milieu de terrain decede en plein match en 2003", MOYEN),
    "Patrick Mboma": ("Le football", "avoir ete Ballon d'or africain en 2000 et champion olympique a Sydney", MOYEN),
    "Vincent Aboubakar": ("Le football", "avoir inscrit le but victorieux de la CAN 2017", MOYEN),
    "Andre Onana": ("Le football", "etre un gardien international passe par l'Ajax et l'Inter Milan", MOYEN),
    "Joseph-Antoine Bell": ("Le football", "avoir garde les buts des Lions Indomptables puis commente le football", CHALLENGE),
    "Alexandre Song": ("Le football", "avoir joue a Arsenal et au FC Barcelone", MOYEN),
    "Eric Maxim Choupo-Moting": ("Le football", "avoir joue au PSG et au Bayern Munich", MOYEN),
    "Geremi Njitap": ("Le football", "avoir joue au Real Madrid et a Chelsea", CHALLENGE),
    "Achille Emana": ("Le football", "avoir brille au Toulouse FC et au Betis Seville", CHALLENGE),
    "Nicolas Nkoulou": ("Le football", "avoir ete defenseur central des Lions Indomptables a Marseille", CHALLENGE),
    "Clinton Njie": ("Le football", "avoir joue a Lyon et Tottenham", CHALLENGE),
    "Gaelle Enganamouit": ("Le football", "avoir ete elue meilleure joueuse africaine en 2015 avec les Lionnes Indomptables", CHALLENGE),
    "Ajara Nchout": ("Le football", "avoir marque des buts decisifs avec les Lionnes Indomptables en Coupe du monde", CHALLENGE),
    "Christine Manie": ("Le football", "avoir ete capitaine des Lionnes Indomptables", CHALLENGE),
    # Athletisme et autres sports
    "Francoise Mbango Etone": ("L'athletisme", "avoir remporte deux titres olympiques au triple saut en 2004 et 2008", MOYEN),
    "Marie-Jose Ta Lou": ("L'athletisme", "etre une sprinteuse ivoirienne, et non camerounaise", CHALLENGE),
    "Joseph Kingue": ("L'athletisme", "avoir represente le Cameroun sur la scene athletique", CHALLENGE),
    "Hortense Bewouda": ("L'athletisme", "avoir represente le Cameroun en saut", CHALLENGE),
    # Musique
    "Manu Dibango": ("La musique", "avoir compose Soul Makossa, tube planetaire au saxophone", FACILE),
    "Richard Bona": ("La musique", "etre un bassiste et chanteur de jazz reconnu mondialement", MOYEN),
    "Anne-Marie Nzie": ("La musique", "etre surnommee la Reine d'or de la chanson camerounaise", MOYEN),
    "Petit-Pays": ("La musique", "etre une figure majeure du makossa moderne", MOYEN),
    "Lady Ponce": ("La musique", "etre une reine du bikutsi", MOYEN),
    "K-Tino": ("La musique", "etre surnommee la femme du peuple, figure du bikutsi", MOYEN),
    "Charlotte Dipanda": ("La musique", "chanter en douala et melanger sonorites traditionnelles et modernes", MOYEN),
    "Sam Fan Thomas": ("La musique", "avoir popularise African Typic Collection", MOYEN),
    "Ben Decca": ("La musique", "etre une grande voix du makossa", MOYEN),
    "Grace Decca": ("La musique", "etre une chanteuse de makossa de la famille Decca", CHALLENGE),
    "Longue Longue": ("La musique", "chanter un makossa engage et populaire", MOYEN),
    "Stanley Enow": ("La musique", "avoir lance le hip-hop camerounais a l'international avec Hein Pere", MOYEN),
    "Jovi": ("La musique", "etre un rappeur pionnier du mouvement Mboko", MOYEN),
    "Daphne": ("La musique", "avoir connu un grand succes avec Calee", MOYEN),
    "Locko": ("La musique", "avoir popularise la chanson Margo", MOYEN),
    "Salatiel": ("La musique", "avoir co-ecrit et produit Oyaho puis collabore avec Beyonce", MOYEN),
    "Blanche Bailly": ("La musique", "etre une chanteuse afropop connue pour Mimbayeur", MOYEN),
    "Mr Leo": ("La musique", "chanter On va gerer et melanger afropop et sonorites locales", MOYEN),
    "Tenor": ("La musique", "etre un rappeur camerounais connu pour Do le Dab", CHALLENGE),
    "Francis Bebey": ("La musique", "etre a la fois musicien, ecrivain et pionnier de la musique africaine moderne", CHALLENGE),
    "Ekambi Brillant": ("La musique", "etre une figure historique du makossa", CHALLENGE),
    "Andre-Marie Talla": ("La musique", "etre un chanteur aveugle celebre pour Hot Koki", CHALLENGE),
    "Coco Argentee": ("La musique", "etre une chanteuse de bikutsi tres populaire", CHALLENGE),
    "X-Maleya": ("La musique", "etre un groupe camerounais connu pour Elle est belle", MOYEN),
    "Lapiro de Mbanga": ("La musique", "avoir chante en camfranglais des textes sociaux engages", CHALLENGE),
    "Dina Bell": ("La musique", "etre une voix historique du makossa", CHALLENGE),
    "Tala Andre Marie": ("La musique", "avoir marque la musique camerounaise malgre sa cecite", CHALLENGE),
    # Litterature
    "Mongo Beti": ("La litterature", "avoir ecrit Le Pauvre Christ de Bomba et Ville cruelle", MOYEN),
    "Ferdinand Oyono": ("La litterature", "avoir ecrit Une vie de boy et Le Vieux Negre et la medaille", MOYEN),
    "Calixthe Beyala": ("La litterature", "avoir recu le Grand Prix du roman de l'Academie francaise", MOYEN),
    "Leonora Miano": ("La litterature", "avoir recu le prix Femina pour La Saison de l'ombre", CHALLENGE),
    "Djaili Amadou Amal": ("La litterature", "avoir recu le prix Goncourt des lyceens pour Les Impatientes", MOYEN),
    "Guillaume Oyono Mbia": ("La litterature", "avoir ecrit la piece Trois pretendants un mari", CHALLENGE),
    "Werewere Liking": ("La litterature", "etre ecrivaine, dramaturge et fondatrice du village Ki-Yi", CHALLENGE),
    "Patrice Nganang": ("La litterature", "avoir ecrit Temps de chien", CHALLENGE),
    "Rene Philombe": ("La litterature", "avoir ecrit le poeme L'homme qui te ressemble", CHALLENGE),
    "Bernard Nanga": ("La litterature", "avoir ecrit Les Chauves-souris", CHALLENGE),
    "Jean-Pierre Bekolo": ("Le cinema", "avoir realise Quartier Mozart et Les Saignantes", CHALLENGE),
    "Jean-Marie Teno": ("Le cinema", "etre un documentariste camerounais reconnu", CHALLENGE),
    "Francoise Ellong": ("Le cinema", "avoir realise le film W.A.K.A.", CHALLENGE),
    # Histoire et politique
    "Ahmadou Ahidjo": ("La politique", "avoir ete le premier president de la Republique du Cameroun", FACILE),
    "Paul Biya": ("La politique", "etre devenu president du Cameroun le 6 novembre 1982", FACILE),
    "John Ngu Foncha": ("La politique", "avoir conduit le Southern Cameroons vers la reunification de 1961", CHALLENGE),
    "Solomon Tandeng Muna": ("La politique", "avoir ete vice-president puis president de l'Assemblee nationale", CHALLENGE),
    "Ni John Fru Ndi": ("La politique", "avoir fonde le Social Democratic Front a Bamenda en 1990", MOYEN),
    "Ruben Um Nyobe": ("La lutte contre la colonisation", "avoir dirige l'UPC dans le combat pour l'independance", MOYEN),
    "Felix-Roland Moumie": ("La lutte contre la colonisation", "avoir dirige l'UPC en exil avant d'etre empoisonne a Geneve", CHALLENGE),
    "Ernest Ouandie": ("La lutte contre la colonisation", "avoir ete un dirigeant de l'UPC execute en 1971", CHALLENGE),
    "Martin-Paul Samba": ("La lutte contre la colonisation", "avoir ete fusille par les Allemands en 1914", CHALLENGE),
    "Rudolf Douala Manga Bell": ("La lutte contre la colonisation", "avoir ete pendu par les Allemands en 1914 pour avoir defendu les terres douala", MOYEN),
    "Le sultan Njoya": ("La politique", "avoir invente l'ecriture shu-mom et regne sur le royaume Bamoun", MOYEN),
    "Charles Atangana": ("La politique", "avoir ete un chef superieur ewondo influent a l'epoque coloniale", CHALLENGE),
    # Affaires, sciences et technologie
    "Baba Danpullo": ("Les affaires et l'entrepreneuriat", "etre l'un des hommes d'affaires les plus riches du Cameroun", MOYEN),
    "Kate Fotso": ("Les affaires et l'entrepreneuriat", "diriger une entreprise majeure de negoce du cacao", CHALLENGE),
    "Victor Fotso": ("Les affaires et l'entrepreneuriat", "avoir bati un grand groupe industriel et bancaire camerounais", CHALLENGE),
    "Paul Kammogne Fokam": ("Les affaires et l'entrepreneuriat", "avoir fonde Afriland First Bank", CHALLENGE),
    "James Onobiono": ("Les affaires et l'entrepreneuriat", "avoir dirige un grand groupe industriel camerounais", CHALLENGE),
    "Rebecca Enonchong": ("La technologie", "avoir fonde AppsTech et defendre l'ecosysteme tech africain", MOYEN),
    "Arthur Zang": ("La technologie", "avoir invente le Cardiopad, tablette medicale pour le coeur", MOYEN),
    "William Elong": ("La technologie", "avoir cree une startup camerounaise de drones civils", MOYEN),
    "Alain Nteff": ("La technologie", "avoir cofonde Gifted Mom pour la sante maternelle", CHALLENGE),
    "Olivier Madiba": ("La technologie", "avoir cree le studio Kiro'o Games et le jeu Aurion", MOYEN),
    "Churchill Mambe": ("La technologie", "avoir cree le moteur de recherche d'emploi Njorku", CHALLENGE),
}


def build() -> list[Q]:
    qs: list[Q] = []
    noms = list(PERSONNALITES.keys())

    for nom, (domaine, fait, diff) in PERSONNALITES.items():
        qs.append(Q(
            f"Dans quel domaine {nom} s'est-il ou s'est-elle illustre(e) ?",
            domaine, others(nom, DOMAINES), diff, "cameroun,personnalites",
            f"{nom} est connu(e) pour {fait}.",
        ))
        qs.append(Q(
            f"Quelle personnalite camerounaise est connue pour {fait} ?",
            nom, others(fait, noms), diff, "cameroun,personnalites",
            f"Il s'agit de {nom}.",
        ))

    extra = [
        ("Combien de fois Samuel Eto'o a-t-il remporte le Ballon d'or africain ?", "Quatre fois",
         ["Une fois", "Deux fois", "Six fois"], MOYEN, "Samuel Eto'o a ete sacre en 2003, 2004, 2005 et 2010."),
        ("En quelle annee Samuel Eto'o est-il devenu president de la Federation camerounaise de football ?", "2021",
         ["2015", "2018", "2023"], CHALLENGE, "Il a ete elu a la tete de la FECAFOOT en decembre 2021."),
        ("Quel age avait Roger Milla lorsqu'il a marque a la Coupe du monde 1994 ?", "42 ans",
         ["32 ans", "36 ans", "48 ans"], CHALLENGE, "Il reste le plus vieux buteur de l'histoire de la Coupe du monde."),
        ("Quelle celebration Roger Milla a-t-il rendue celebre en 1990 ?", "Sa danse au poteau de corner",
         ["Le salut militaire", "Le saut perilleux", "Le baiser au ballon"], FACILE, "Sa danse est devenue un symbole mondial."),
        ("Quel surnom porte l'equipe nationale masculine de football du Cameroun ?", "Les Lions Indomptables",
         ["Les Elephants", "Les Aigles", "Les Etalons"], FACILE, "Les Lions Indomptables sont l'un des symboles du pays."),
        ("Quel surnom porte l'equipe nationale feminine de football du Cameroun ?", "Les Lionnes Indomptables",
         ["Les Panthers", "Les Gazelles", "Les Etoiles"], MOYEN, "Les Lionnes Indomptables ont dispute plusieurs Coupes du monde."),
        ("Combien de Coupes d'Afrique des Nations le Cameroun a-t-il remportees ?", "Cinq",
         ["Deux", "Trois", "Sept"], MOYEN, "Titres en 1984, 1988, 2000, 2002 et 2017."),
        ("En quelle annee le Cameroun a-t-il remporte sa premiere CAN ?", "1984",
         ["1972", "1988", "1990"], CHALLENGE, "Le premier sacre continental date de 1984."),
        ("En quelle annee le Cameroun a-t-il remporte la CAN a domicile la plus recente ?", "2017",
         ["2002", "2010", "2021"], MOYEN, "Le titre de 2017 a ete conquis au Gabon."),
        ("Quel pays a organise la Coupe d'Afrique des Nations 2021 disputee en 2022 ?", "Le Cameroun",
         ["Le Nigeria", "La Cote d'Ivoire", "Le Senegal"], FACILE, "Le Cameroun a accueilli la CAN en janvier-fevrier 2022."),
        ("A quels Jeux olympiques les Lions Indomptables ont-ils remporte la medaille d'or ?", "Sydney 2000",
         ["Atlanta 1996", "Athenes 2004", "Pekin 2008"], MOYEN, "Le Cameroun a battu l'Espagne en finale a Sydney."),
        ("En 1990, jusqu'ou le Cameroun est-il alle en Coupe du monde ?", "En quart de finale",
         ["En huitieme de finale", "En demi-finale", "En finale"], MOYEN, "Premiere equipe africaine a atteindre les quarts."),
        ("Quel stade de Yaounde a accueilli des matchs de la CAN 2021 ?", "Le stade Olembe",
         ["Le stade Reunification de Douala", "Le stade de Bafoussam uniquement", "Le stade de Limbe uniquement"], MOYEN, "Le stade Olembe, aussi appele stade Paul Biya."),
        ("Dans quelle ville se trouve le stade de la Reunification ?", "Douala",
         ["Yaounde", "Garoua", "Bafoussam"], MOYEN, "Le stade de la Reunification est situe a Douala."),
        ("Quel genre musical est originaire du pays Beti, dans le Centre ?", "Le bikutsi",
         ["Le makossa", "Le mbalax", "Le coupe-decale"], MOYEN, "Le bikutsi est emblematique de la region du Centre."),
        ("De quelle region le makossa est-il originaire ?", "Le Littoral",
         ["Le Centre", "L'Ouest", "Le Nord"], MOYEN, "Le makossa est ne chez les Sawa, autour de Douala."),
        ("Quel rythme musical est associe a la region de l'Ouest ?", "Le bend-skin",
         ["Le bikutsi", "Le makossa", "L'assiko"], CHALLENGE, "Le bend-skin est ne dans les Grassfields de l'Ouest."),
        ("Quel genre musical camerounais est joue principalement a la guitare et associe aux Bassa ?", "L'assiko",
         ["Le bikutsi", "Le mangambeu", "Le njang"], CHALLENGE, "L'assiko est un style guitare-percussions du pays Bassa."),
        ("Quel morceau de Manu Dibango a inspire des artistes internationaux comme Michael Jackson ?", "Soul Makossa",
         ["Sweet Mother", "Yaounde Blues", "African Queen"], MOYEN, "Soul Makossa est sorti en 1972."),
        ("Quel instrument Manu Dibango jouait-il principalement ?", "Le saxophone",
         ["La guitare", "Le piano", "La trompette"], FACILE, "Manu Dibango etait saxophoniste et vibraphoniste."),
        ("Quel roman de Ferdinand Oyono raconte la vie d'un jeune domestique sous la colonisation ?", "Une vie de boy",
         ["Ville cruelle", "Les Impatientes", "Trois pretendants un mari"], MOYEN, "Une vie de boy est un classique de la litterature africaine."),
        ("Sous quel pseudonyme Mongo Beti a-t-il publie Ville cruelle ?", "Eza Boto",
         ["Oyono Mbia", "Nganang", "Philombe"], CHALLENGE, "Mongo Beti a signe Ville cruelle sous le nom d'Eza Boto."),
        ("De quoi parle principalement le roman Les Impatientes de Djaili Amadou Amal ?", "De la condition des femmes dans le Nord du Cameroun",
         ["De la vie des pecheurs de Kribi", "De la colonisation allemande", "De l'histoire du football camerounais"], MOYEN, "Le roman denonce les mariages forces et la patience imposee aux femmes."),
        ("Quel jeu video camerounais developpe par Kiro'o Games s'inspire des mythologies africaines ?", "Aurion",
         ["Mboa Quest", "Sawa Legends", "Kamer Fighter"], MOYEN, "Aurion : L'Heritage des Kori-Odan est sorti en 2016."),
        ("A quoi sert le Cardiopad invente par Arthur Zang ?", "A realiser des examens cardiaques a distance",
         ["A recharger les telephones", "A purifier l'eau", "A traduire les langues locales"], MOYEN, "Le Cardiopad permet des electrocardiogrammes en zone rurale."),
    ]
    for question, correct, wrong, diff, expl in extra:
        qs.append(Q(question, correct, wrong, diff, "cameroun,personnalites,sport,culture", expl))

    return qs
