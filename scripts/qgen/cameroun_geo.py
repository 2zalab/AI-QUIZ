# -*- coding: utf-8 -*-
"""Banque Cameroun : geographie administrative et physique."""

from __future__ import annotations

from .common import CHALLENGE, FACILE, MOYEN, Q, others

# --------------------------------------------------------------------------
# 10 regions et leurs chefs-lieux
# --------------------------------------------------------------------------
REGIONS = {
    "Adamaoua": "Ngaoundere",
    "Centre": "Yaounde",
    "Est": "Bertoua",
    "Extreme-Nord": "Maroua",
    "Littoral": "Douala",
    "Nord": "Garoua",
    "Nord-Ouest": "Bamenda",
    "Ouest": "Bafoussam",
    "Sud": "Ebolowa",
    "Sud-Ouest": "Buea",
}

# --------------------------------------------------------------------------
# 58 departements : nom -> (chef-lieu, region)
# --------------------------------------------------------------------------
DEPARTEMENTS = {
    # Adamaoua (5)
    "Djerem": ("Tibati", "Adamaoua"),
    "Faro-et-Deo": ("Tignere", "Adamaoua"),
    "Mayo-Banyo": ("Banyo", "Adamaoua"),
    "Mbere": ("Meiganga", "Adamaoua"),
    "Vina": ("Ngaoundere", "Adamaoua"),
    # Centre (10)
    "Haute-Sanaga": ("Nanga-Eboko", "Centre"),
    "Lekie": ("Monatele", "Centre"),
    "Mbam-et-Inoubou": ("Bafia", "Centre"),
    "Mbam-et-Kim": ("Ntui", "Centre"),
    "Mefou-et-Afamba": ("Mfou", "Centre"),
    "Mefou-et-Akono": ("Ngoumou", "Centre"),
    "Mfoundi": ("Yaounde", "Centre"),
    "Nyong-et-Kelle": ("Eseka", "Centre"),
    "Nyong-et-Mfoumou": ("Akonolinga", "Centre"),
    "Nyong-et-So'o": ("Mbalmayo", "Centre"),
    # Est (4)
    "Boumba-et-Ngoko": ("Yokadouma", "Est"),
    "Haut-Nyong": ("Abong-Mbang", "Est"),
    "Kadey": ("Batouri", "Est"),
    "Lom-et-Djerem": ("Bertoua", "Est"),
    # Extreme-Nord (6)
    "Diamare": ("Maroua", "Extreme-Nord"),
    "Logone-et-Chari": ("Kousseri", "Extreme-Nord"),
    "Mayo-Danay": ("Yagoua", "Extreme-Nord"),
    "Mayo-Kani": ("Kaele", "Extreme-Nord"),
    "Mayo-Sava": ("Mora", "Extreme-Nord"),
    "Mayo-Tsanaga": ("Mokolo", "Extreme-Nord"),
    # Littoral (4)
    "Moungo": ("Nkongsamba", "Littoral"),
    "Nkam": ("Yabassi", "Littoral"),
    "Sanaga-Maritime": ("Edea", "Littoral"),
    "Wouri": ("Douala", "Littoral"),
    # Nord (4)
    "Benoue": ("Garoua", "Nord"),
    "Faro": ("Poli", "Nord"),
    "Mayo-Louti": ("Guider", "Nord"),
    "Mayo-Rey": ("Tchollire", "Nord"),
    # Nord-Ouest (7)
    "Boyo": ("Fundong", "Nord-Ouest"),
    "Bui": ("Kumbo", "Nord-Ouest"),
    "Donga-Mantung": ("Nkambe", "Nord-Ouest"),
    "Menchum": ("Wum", "Nord-Ouest"),
    "Mezam": ("Bamenda", "Nord-Ouest"),
    "Momo": ("Mbengwi", "Nord-Ouest"),
    "Ngo-Ketunjia": ("Ndop", "Nord-Ouest"),
    # Ouest (8)
    "Bamboutos": ("Mbouda", "Ouest"),
    "Haut-Nkam": ("Bafang", "Ouest"),
    "Hauts-Plateaux": ("Baham", "Ouest"),
    "Koung-Khi": ("Bandjoun", "Ouest"),
    "Menoua": ("Dschang", "Ouest"),
    "Mifi": ("Bafoussam", "Ouest"),
    "Nde": ("Bangangte", "Ouest"),
    "Noun": ("Foumban", "Ouest"),
    # Sud (4)
    "Dja-et-Lobo": ("Sangmelima", "Sud"),
    "Mvila": ("Ebolowa", "Sud"),
    "Ocean": ("Kribi", "Sud"),
    "Vallee-du-Ntem": ("Ambam", "Sud"),
    # Sud-Ouest (6)
    "Fako": ("Limbe", "Sud-Ouest"),
    "Koupe-Manengouba": ("Bangem", "Sud-Ouest"),
    "Lebialem": ("Menji", "Sud-Ouest"),
    "Manyu": ("Mamfe", "Sud-Ouest"),
    "Meme": ("Kumba", "Sud-Ouest"),
    "Ndian": ("Mundemba", "Sud-Ouest"),
}

# --------------------------------------------------------------------------
# Villes -> region (au dela des chefs-lieux de departement)
# --------------------------------------------------------------------------
VILLES = {
    "Douala": "Littoral", "Yaounde": "Centre", "Garoua": "Nord",
    "Bamenda": "Nord-Ouest", "Maroua": "Extreme-Nord", "Bafoussam": "Ouest",
    "Ngaoundere": "Adamaoua", "Bertoua": "Est", "Buea": "Sud-Ouest",
    "Ebolowa": "Sud", "Kribi": "Sud", "Limbe": "Sud-Ouest",
    "Kumba": "Sud-Ouest", "Nkongsamba": "Littoral", "Dschang": "Ouest",
    "Foumban": "Ouest", "Bafang": "Ouest", "Mbouda": "Ouest",
    "Bangangte": "Ouest", "Bandjoun": "Ouest", "Baham": "Ouest",
    "Foumbot": "Ouest", "Batcham": "Ouest", "Bafang": "Ouest",
    "Edea": "Littoral", "Yabassi": "Littoral", "Loum": "Littoral",
    "Mbanga": "Littoral", "Manjo": "Littoral", "Melong": "Littoral",
    "Penja": "Littoral", "Njombe": "Littoral", "Dizangue": "Littoral",
    "Mbalmayo": "Centre", "Eseka": "Centre", "Akonolinga": "Centre",
    "Bafia": "Centre", "Nanga-Eboko": "Centre", "Obala": "Centre",
    "Monatele": "Centre", "Mfou": "Centre", "Ntui": "Centre",
    "Soa": "Centre", "Mbandjock": "Centre", "Ngoumou": "Centre",
    "Sangmelima": "Sud", "Ambam": "Sud", "Djoum": "Sud",
    "Campo": "Sud", "Lolodorf": "Sud", "Meyomessala": "Sud",
    "Abong-Mbang": "Est", "Batouri": "Est", "Yokadouma": "Est",
    "Belabo": "Est", "Garoua-Boulai": "Est", "Moloundou": "Est",
    "Kousseri": "Extreme-Nord", "Yagoua": "Extreme-Nord", "Kaele": "Extreme-Nord",
    "Mora": "Extreme-Nord", "Mokolo": "Extreme-Nord", "Rhumsiki": "Extreme-Nord",
    "Waza": "Extreme-Nord", "Guider": "Nord", "Poli": "Nord",
    "Tchollire": "Nord", "Figuil": "Nord", "Lagdo": "Nord",
    "Tibati": "Adamaoua", "Meiganga": "Adamaoua", "Banyo": "Adamaoua",
    "Tignere": "Adamaoua", "Tibati": "Adamaoua", "Ngaoundal": "Adamaoua",
    "Kumbo": "Nord-Ouest", "Wum": "Nord-Ouest", "Ndop": "Nord-Ouest",
    "Nkambe": "Nord-Ouest", "Fundong": "Nord-Ouest", "Mbengwi": "Nord-Ouest",
    "Bafut": "Nord-Ouest", "Bali": "Nord-Ouest", "Batibo": "Nord-Ouest",
    "Mamfe": "Sud-Ouest", "Mundemba": "Sud-Ouest", "Tiko": "Sud-Ouest",
    "Muyuka": "Sud-Ouest", "Bangem": "Sud-Ouest", "Menji": "Sud-Ouest",
    "Idenau": "Sud-Ouest", "Ekondo-Titi": "Sud-Ouest",
}

CHEFS_LIEUX = list(REGIONS.values())
NOMS_REGIONS = list(REGIONS.keys())
NOMS_DEPARTEMENTS = list(DEPARTEMENTS.keys())
CHEFS_DEPT = [v[0] for v in DEPARTEMENTS.values()]


def build() -> list[Q]:
    qs: list[Q] = []

    # --- Regions et chefs-lieux -------------------------------------------
    for region, chef in REGIONS.items():
        qs.append(Q(
            f"Quel est le chef-lieu de la region de l'{region} ?"
            if region in ("Adamaoua", "Est", "Extreme-Nord", "Ouest")
            else f"Quel est le chef-lieu de la region du {region} ?",
            chef, others(chef, CHEFS_LIEUX), FACILE, "cameroun,geographie,regions",
            f"{chef} est le chef-lieu de la region de l'{region}." ,
        ))
        qs.append(Q(
            f"La ville de {chef} est le chef-lieu de quelle region du Cameroun ?",
            region, others(region, NOMS_REGIONS), FACILE, "cameroun,geographie,regions",
            f"{chef} est le chef-lieu de la region : {region}.",
        ))

    qs.append(Q("Combien de regions compte le Cameroun ?", "10",
                ["8", "12", "14"], FACILE, "cameroun,geographie,regions",
                "Le Cameroun est decoupe en 10 regions depuis 2008."))
    qs.append(Q("Combien de departements compte le Cameroun ?", "58",
                ["47", "62", "72"], MOYEN, "cameroun,geographie,regions",
                "Les 10 regions du Cameroun regroupent 58 departements."))
    qs.append(Q("Quelle est la capitale politique du Cameroun ?", "Yaounde",
                ["Douala", "Bafoussam", "Garoua"], FACILE, "cameroun,geographie",
                "Yaounde est la capitale politique, Douala la capitale economique."))
    qs.append(Q("Quelle ville est consideree comme la capitale economique du Cameroun ?",
                "Douala", ["Yaounde", "Kribi", "Bamenda"], FACILE, "cameroun,economie",
                "Douala concentre le port, les industries et les sieges d'entreprises."))
    qs.append(Q("Quelles sont les deux regions anglophones du Cameroun ?",
                "Le Nord-Ouest et le Sud-Ouest",
                ["Le Nord et l'Extreme-Nord", "L'Ouest et le Littoral",
                 "Le Centre et le Sud"], FACILE, "cameroun,geographie",
                "Le Nord-Ouest et le Sud-Ouest sont issus du Southern Cameroons britannique."))
    qs.append(Q("Quelles sont les trois regions septentrionales du Cameroun ?",
                "Adamaoua, Nord et Extreme-Nord",
                ["Nord, Ouest et Centre", "Est, Nord et Littoral",
                 "Adamaoua, Est et Sud"], MOYEN, "cameroun,geographie",
                "Le Grand Nord regroupe l'Adamaoua, le Nord et l'Extreme-Nord."))

    # --- Departements ------------------------------------------------------
    for dept, (chef, region) in DEPARTEMENTS.items():
        qs.append(Q(
            f"Quel est le chef-lieu du departement du {dept} ?",
            chef, others(chef, CHEFS_DEPT), CHALLENGE,
            "cameroun,geographie,departements",
            f"{chef} est le chef-lieu du {dept}, dans la region : {region}.",
        ))
        qs.append(Q(
            f"Le departement du {dept} appartient a quelle region ?",
            region, others(region, NOMS_REGIONS), MOYEN,
            "cameroun,geographie,departements",
            f"Le {dept} se situe dans la region : {region}.",
        ))

    # --- Villes ------------------------------------------------------------
    for ville, region in VILLES.items():
        qs.append(Q(
            f"Dans quelle region du Cameroun se trouve la ville de {ville} ?",
            region, others(region + ville, NOMS_REGIONS), MOYEN,
            "cameroun,geographie,villes",
            f"{ville} est situee dans la region : {region}.",
        ))

    # --- Frontieres, relief, hydrographie ----------------------------------
    fixes = [
        ("Combien de pays partagent une frontiere terrestre avec le Cameroun ?", "6",
         ["4", "5", "8"], MOYEN, "Nigeria, Tchad, Republique centrafricaine, Congo, Gabon et Guinee equatoriale."),
        ("Quel pays partage la plus longue frontiere terrestre avec le Cameroun ?", "Le Nigeria",
         ["Le Tchad", "Le Gabon", "Le Congo"], MOYEN, "La frontiere avec le Nigeria depasse 1 600 km."),
        ("Quel pays ne partage PAS de frontiere avec le Cameroun ?", "Le Niger",
         ["Le Tchad", "Le Gabon", "Le Congo"], MOYEN, "Le Niger n'a pas de frontiere commune avec le Cameroun."),
        ("Sur quel ocean le Cameroun possede-t-il une facade maritime ?", "L'ocean Atlantique",
         ["L'ocean Indien", "L'ocean Pacifique", "La mer Rouge"], FACILE, "Le golfe de Guinee ouvre sur l'Atlantique."),
        ("Quel est le point culminant du Cameroun ?", "Le mont Cameroun",
         ["Le mont Oku", "Les monts Mandara", "Le mont Manengouba"], FACILE, "Le mont Cameroun culmine a environ 4 095 metres."),
        ("Quelle est l'altitude approximative du mont Cameroun ?", "Environ 4 095 metres",
         ["Environ 2 100 metres", "Environ 5 800 metres", "Environ 3 000 metres"], MOYEN, "C'est le plus haut sommet d'Afrique de l'Ouest et centrale."),
        ("Le mont Cameroun est un volcan situe dans quelle region ?", "Le Sud-Ouest",
         ["Le Littoral", "L'Ouest", "Le Nord-Ouest"], FACILE, "Il domine la ville de Buea, dans le departement du Fako."),
        ("Quel surnom traditionnel donne-t-on au mont Cameroun ?", "Le Char des Dieux",
         ["La Montagne Bleue", "Le Toit du Monde", "Le Pic de la Paix"], MOYEN, "Les Grecs anciens l'appelaient deja le Char des Dieux."),
        ("Quelle course sportive celebre se dispute chaque annee sur le mont Cameroun ?", "La Course de l'Espoir",
         ["Le Marathon du Wouri", "Le Trophee des Volcans", "La Ronde de Buea"], MOYEN, "La Course de l'Espoir attire des coureurs du monde entier."),
        ("Quel est le plus long fleuve entierement camerounais ?", "La Sanaga",
         ["Le Nyong", "Le Wouri", "La Benoue"], MOYEN, "La Sanaga s'etire sur environ 918 km."),
        ("Sur quel fleuve se trouve le barrage de Song Loulou ?", "La Sanaga",
         ["Le Nyong", "Le Logone", "Le Ntem"], CHALLENGE, "Song Loulou est l'un des principaux barrages hydroelectriques du pays."),
        ("La ville de Douala est batie sur l'estuaire de quel fleuve ?", "Le Wouri",
         ["La Sanaga", "Le Nyong", "Le Mungo"], FACILE, "Le pont sur le Wouri est un symbole de Douala."),
        ("Quel fleuve marque une partie de la frontiere entre le Cameroun et la Guinee equatoriale ?", "Le Ntem",
         ["Le Nyong", "La Benoue", "Le Logone"], CHALLENGE, "Le Ntem borde le sud du pays."),
        ("Quel fleuve du Nord du Cameroun est un affluent du Niger ?", "La Benoue",
         ["La Sanaga", "Le Nyong", "Le Dja"], CHALLENGE, "La Benoue rejoint le Niger au Nigeria."),
        ("Quel lac camerounais a connu une catastrophe gazeuse meurtriere en 1986 ?", "Le lac Nyos",
         ["Le lac Monoun", "Le lac Ossa", "Le lac Barombi Mbo"], MOYEN, "L'eruption limnique du lac Nyos a fait environ 1 700 morts."),
        ("Dans quelle region se trouve le lac Nyos ?", "Le Nord-Ouest",
         ["L'Ouest", "L'Adamaoua", "Le Sud-Ouest"], CHALLENGE, "Le lac Nyos est situe dans le departement du Menchum."),
        ("Quel grand lac borde l'extreme nord du Cameroun ?", "Le lac Tchad",
         ["Le lac Victoria", "Le lac Tanganyika", "Le lac Kivu"], FACILE, "Le Cameroun est l'un des quatre pays riverains du lac Tchad."),
        ("Quel barrage hydroelectrique a ete mis en service sur la Sanaga a Nachtigal ?", "Le barrage de Nachtigal",
         ["Le barrage de Lagdo", "Le barrage de Maga", "Le barrage de Bamendjing"], MOYEN, "Nachtigal Amont est concu pour environ 420 MW."),
        ("Le barrage de Lagdo se trouve dans quelle region ?", "Le Nord",
         ["L'Extreme-Nord", "L'Adamaoua", "L'Est"], CHALLENGE, "Lagdo est situe sur la Benoue, pres de Garoua."),
        ("Quelles chutes camerounaises se jettent directement dans l'ocean ?", "Les chutes de la Lobe",
         ["Les chutes d'Ekom Nkam", "Les chutes de la Metche", "Les chutes de Menchum"], MOYEN, "Les chutes de la Lobe, pres de Kribi, sont un cas rare au monde."),
        ("Les chutes de la Lobe se trouvent pres de quelle ville ?", "Kribi",
         ["Limbe", "Edea", "Campo"], FACILE, "Elles sont l'attraction phare de la region de Kribi."),
        ("Quelles chutes de la region du Littoral ont servi de decor a un film Tarzan ?", "Les chutes d'Ekom Nkam",
         ["Les chutes de la Lobe", "Les chutes de la Metche", "Les chutes de Menchum"], CHALLENGE, "Les chutes d'Ekom Nkam, pres de Melong."),
        ("Quel parc national du Grand Nord est le plus connu pour ses safaris ?", "Le parc national de Waza",
         ["Le parc de Korup", "Le parc de Campo Ma'an", "Le parc de Lobeke"], MOYEN, "Waza, dans l'Extreme-Nord, abrite elephants, lions et girafes."),
        ("Quel parc national du Sud-Ouest est reconnu pour sa foret primaire ?", "Le parc national de Korup",
         ["Le parc de Waza", "Le parc de la Benoue", "Le parc de Bouba Ndjidah"], CHALLENGE, "Korup est l'une des plus vieilles forets tropicales d'Afrique."),
        ("Quelle reserve camerounaise est inscrite au patrimoine mondial de l'UNESCO ?", "La reserve de faune du Dja",
         ["La reserve de Douala-Edea", "Le parc de Waza", "Le parc de Campo Ma'an"], MOYEN, "La reserve du Dja est classee par l'UNESCO depuis 1987."),
        ("Quel massif montagneux de l'Extreme-Nord est celebre pour ses pics volcaniques ?", "Les monts Mandara",
         ["Les monts Bamboutos", "Le massif du Manengouba", "Les monts Alantika"], MOYEN, "Le village de Rhumsiki, dans les monts Mandara, est un site touristique majeur."),
        ("Quel village touristique des monts Mandara est celebre pour ses paysages de pitons ?", "Rhumsiki",
         ["Mokolo", "Kaele", "Mora"], MOYEN, "Rhumsiki est l'un des paysages les plus photographies du Cameroun."),
        ("Quel plateau occupe le centre de la region de l'Adamaoua ?", "Le plateau de l'Adamaoua",
         ["Le plateau Bamileke", "Le plateau du Mbam", "Le plateau de l'Ocean"], FACILE, "Le chateau d'eau du Cameroun, ou naissent plusieurs fleuves."),
        ("Pourquoi appelle-t-on l'Adamaoua le chateau d'eau du Cameroun ?", "Parce que plusieurs grands fleuves y prennent leur source",
         ["Parce qu'il pleut toute l'annee", "Parce qu'il abrite le plus grand barrage",
          "Parce qu'il borde l'ocean"], MOYEN, "La Sanaga, la Benoue et le Djerem naissent sur ce plateau."),
        ("Pourquoi surnomme-t-on le Cameroun l'Afrique en miniature ?", "Parce qu'il reunit la plupart des climats et paysages du continent",
         ["Parce qu'il est le plus petit pays d'Afrique",
          "Parce qu'il a la plus petite population du continent",
          "Parce qu'il ne possede qu'un seul climat"], FACILE, "Desert, savane, foret, montagne et littoral coexistent au Cameroun."),
        ("Quelle ville du Sud-Ouest est connue pour ses plages de sable noir volcanique ?", "Limbe",
         ["Kribi", "Douala", "Campo"], MOYEN, "Le sable noir de Limbe vient des coulees du mont Cameroun."),
        ("Quel port en eau profonde a ete inaugure dans la region du Sud ?", "Le port de Kribi",
         ["Le port de Limbe", "Le port de Tiko", "Le port de Campo"], MOYEN, "Le port en eau profonde de Kribi complete le port de Douala."),
        ("Quel est le principal port maritime historique du Cameroun ?", "Le port de Douala",
         ["Le port de Kribi", "Le port de Limbe", "Le port de Garoua"], FACILE, "Douala traite la majeure partie du trafic portuaire national."),
        ("Quelle ile camerounaise est situee face a Douala ?", "L'ile de Manoka",
         ["L'ile de Goree", "L'ile de Bioko", "L'ile de Sao Tome"], CHALLENGE, "Manoka appartient a la region du Littoral."),
        ("Quelle presqu'ile a fait l'objet d'un differend entre le Cameroun et le Nigeria ?", "La presqu'ile de Bakassi",
         ["La presqu'ile de Kribi", "L'ile de Manoka", "La plaine de Ndop"], MOYEN, "La CIJ a tranche en faveur du Cameroun en 2002."),
        ("En quelle annee la presqu'ile de Bakassi a-t-elle ete officiellement retrocedee au Cameroun ?", "2008",
         ["1998", "2002", "2012"], CHALLENGE, "La retrocession effective a eu lieu le 14 aout 2008."),
        ("Quel climat domine le sud forestier du Cameroun ?", "Un climat equatorial humide",
         ["Un climat desertique", "Un climat mediterraneen", "Un climat polaire"], FACILE, "Le sud connait de fortes pluies et une foret dense."),
        ("Quel climat caracterise l'Extreme-Nord du Cameroun ?", "Un climat sahelien, chaud et sec",
         ["Un climat equatorial humide", "Un climat oceanique", "Un climat de montagne froid"], FACILE, "La saison seche y est longue et marquee."),
        ("Quelle ville camerounaise est reputee parmi les plus pluvieuses au monde ?", "Debundscha, au pied du mont Cameroun",
         ["Maroua", "Garoua", "Ngaoundere"], CHALLENGE, "Debundscha recoit environ 10 000 mm de pluie par an."),
        ("Quelle est la superficie approximative du Cameroun ?", "Environ 475 000 km2",
         ["Environ 120 000 km2", "Environ 900 000 km2", "Environ 1 200 000 km2"], MOYEN, "Le Cameroun couvre 475 442 km2."),
        ("Quelle est la population approximative du Cameroun aujourd'hui ?", "Environ 28 millions d'habitants",
         ["Environ 8 millions", "Environ 55 millions", "Environ 90 millions"], MOYEN, "La population est estimee autour de 28 a 29 millions d'habitants."),
        ("Quelle plaine du Nord-Ouest est reputee pour sa riziculture ?", "La plaine de Ndop",
         ["La plaine de Maga", "La plaine de Mbo", "La plaine de Bakassi"], CHALLENGE, "La plaine de Ndop est un bassin rizicole important."),
        ("Quel jardin botanique historique se trouve a Limbe ?", "Le jardin botanique de Limbe",
         ["Le jardin de Mvog-Betsi", "Le jardin de Foumban", "Le jardin de Bafut"], MOYEN, "Cree en 1892 a l'epoque allemande."),
        ("Quel massif volcanique de l'Ouest abrite des lacs jumeaux tres visites ?", "Le mont Manengouba",
         ["Le mont Oku", "Les monts Bamboutos", "Le mont Kupe"], CHALLENGE, "Les lacs jumeaux du Manengouba, dits male et femelle."),
        ("Quel lac de la region de l'Ouest a connu une eruption gazeuse en 1984 ?", "Le lac Monoun",
         ["Le lac Nyos", "Le lac Ossa", "Le lac Bini"], CHALLENGE, "Le lac Monoun, pres de Foumbot, a precede la catastrophe de Nyos."),
    ]
    for question, correct, wrong, diff, expl in fixes:
        qs.append(Q(question, correct, wrong, diff, "cameroun,geographie", expl))

    return qs
