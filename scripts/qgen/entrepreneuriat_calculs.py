# -*- coding: utf-8 -*-
"""Banque Entrepreneuriat : cas pratiques chiffres (gestion, marge, rentabilite).

Les enonces sont generes a partir de jeux de donnees realistes en FCFA. Les
distracteurs correspondent a des erreurs de raisonnement classiques (oubli d'une
charge, mauvaise base de calcul, confusion marge / prix de vente).
"""

from __future__ import annotations

from .common import CHALLENGE, FACILE, MOYEN, Q


def fcfa(value: float) -> str:
    """Formate un montant en FCFA avec des espaces comme separateurs."""
    rounded = round(value)
    return f"{rounded:,}".replace(",", " ") + " FCFA"


def pct(value: float) -> str:
    return f"{value:.1f} %".replace(".0 %", " %")


def uniq(correct: str, candidates: list[str]) -> list[str]:
    out: list[str] = []
    for c in candidates:
        if c != correct and c not in out:
            out.append(c)
    return out


def build() -> list[Q]:
    qs: list[Q] = []

    # 1. Marge unitaire ------------------------------------------------------
    for achat, vente in [(1200, 2000), (350, 500), (4500, 6000), (700, 1000),
                         (2500, 4000), (15000, 21000), (800, 1250), (60000, 85000),
                         (250, 400), (3200, 4500), (12000, 15500), (900, 1500)]:
        marge = vente - achat
        qs.append(Q(
            f"Une commercante achete un article a {fcfa(achat)} et le revend a {fcfa(vente)}. "
            "Quelle est sa marge sur une unite vendue ?",
            fcfa(marge),
            uniq(fcfa(marge), [fcfa(vente), fcfa(achat), fcfa(vente + achat), fcfa(marge / 2)]),
            FACILE, "entrepreneuriat,calcul,marge",
            f"Marge = prix de vente - prix d'achat = {fcfa(vente)} - {fcfa(achat)} = {fcfa(marge)}.",
        ))

    # 2. Marge totale sur un volume ----------------------------------------
    for achat, vente, qte in [(1200, 2000, 50), (350, 500, 200), (4500, 6000, 30),
                              (700, 1000, 120), (2500, 4000, 25), (900, 1500, 80),
                              (250, 400, 300), (15000, 21000, 12), (3200, 4500, 40),
                              (600, 950, 150), (1800, 2600, 60), (5000, 7500, 20)]:
        marge = (vente - achat) * qte
        qs.append(Q(
            f"Un vendeur achete des articles a {fcfa(achat)} l'unite et les revend a {fcfa(vente)}. "
            f"Il en vend {qte} dans le mois. Quelle est sa marge totale ?",
            fcfa(marge),
            uniq(fcfa(marge), [fcfa(vente * qte), fcfa(achat * qte),
                               fcfa((vente + achat) * qte), fcfa(vente - achat)]),
            MOYEN, "entrepreneuriat,calcul,marge",
            f"Marge totale = ({fcfa(vente)} - {fcfa(achat)}) x {qte} = {fcfa(marge)}.",
        ))

    # 3. Taux de marge ------------------------------------------------------
    for achat, vente in [(1500, 2000), (600, 1000), (7500, 10000), (2400, 3000),
                         (900, 1200), (4000, 5000), (1750, 2500), (12000, 16000),
                         (450, 600), (8000, 10000)]:
        taux = (vente - achat) / vente * 100
        taux_faux = (vente - achat) / achat * 100
        qs.append(Q(
            f"Un produit est achete {fcfa(achat)} et vendu {fcfa(vente)}. "
            "Quel est le taux de marge, calcule sur le prix de vente ?",
            pct(taux),
            uniq(pct(taux), [pct(taux_faux), pct(taux / 2), pct(100 - taux), pct(taux + 10)]),
            CHALLENGE, "entrepreneuriat,calcul,marge",
            f"Taux de marge = (PV - PA) / PV x 100 = {pct(taux)}.",
        ))

    # 4. Chiffre d'affaires -------------------------------------------------
    for prix, qte in [(1500, 40), (2500, 60), (500, 250), (12000, 15), (800, 175),
                      (3500, 48), (250, 400), (9000, 22), (1750, 90), (600, 320),
                      (4500, 36), (2000, 125)]:
        ca = prix * qte
        qs.append(Q(
            f"Une entreprise vend {qte} produits a {fcfa(prix)} l'unite. "
            "Quel est son chiffre d'affaires ?",
            fcfa(ca),
            uniq(fcfa(ca), [fcfa(ca / 2), fcfa(prix + qte), fcfa(ca * 2), fcfa(ca / 10)]),
            FACILE, "entrepreneuriat,calcul,chiffre-affaires",
            f"Chiffre d'affaires = prix x quantite = {fcfa(prix)} x {qte} = {fcfa(ca)}.",
        ))

    # 5. Benefice apres charges --------------------------------------------
    for ca, charges in [(1200000, 850000), (450000, 300000), (2500000, 1900000),
                        (780000, 640000), (3200000, 2450000), (150000, 95000),
                        (5600000, 4700000), (920000, 815000), (2050000, 1380000),
                        (640000, 590000), (7500000, 6200000), (330000, 215000)]:
        benef = ca - charges
        qs.append(Q(
            f"Une entreprise realise {fcfa(ca)} de chiffre d'affaires et supporte {fcfa(charges)} de charges. "
            "Quel est son benefice ?",
            fcfa(benef),
            uniq(fcfa(benef), [fcfa(ca), fcfa(charges), fcfa(ca + charges), fcfa(benef / 2)]),
            FACILE, "entrepreneuriat,calcul,resultat",
            f"Benefice = CA - charges = {fcfa(ca)} - {fcfa(charges)} = {fcfa(benef)}.",
        ))

    # 6. Seuil de rentabilite en quantite -----------------------------------
    for fixes, prix, cvu in [(300000, 2000, 1200), (150000, 1500, 900),
                             (600000, 5000, 3000), (240000, 1200, 800),
                             (450000, 3000, 1500), (900000, 6000, 3000),
                             (120000, 800, 500), (750000, 4000, 2500),
                             (360000, 2400, 1200), (200000, 1000, 600)]:
        seuil = fixes / (prix - cvu)
        qs.append(Q(
            f"Une activite supporte {fcfa(fixes)} de charges fixes par mois. Chaque produit se vend "
            f"{fcfa(prix)} et coute {fcfa(cvu)} a produire. Combien faut-il en vendre pour atteindre le seuil de rentabilite ?",
            f"{round(seuil)} unites",
            uniq(f"{round(seuil)} unites",
                 [f"{round(fixes / prix)} unites", f"{round(fixes / cvu)} unites",
                  f"{round(seuil * 2)} unites", f"{round(seuil / 2)} unites",
                  f"{round(seuil * 1.5)} unites", f"{round(seuil + 25)} unites"]),
            CHALLENGE, "entrepreneuriat,calcul,seuil-rentabilite",
            f"Seuil = charges fixes / marge sur cout variable = {fcfa(fixes)} / {fcfa(prix - cvu)} = {round(seuil)} unites.",
        ))

    # 7. Remise commerciale -------------------------------------------------
    for prix, remise in [(25000, 10), (12000, 25), (80000, 15), (5000, 20),
                         (150000, 5), (36000, 50), (7500, 10), (240000, 30),
                         (18000, 15), (60000, 20)]:
        net = prix * (1 - remise / 100)
        qs.append(Q(
            f"Un article coute {fcfa(prix)}. Le vendeur accorde une remise de {remise} %. "
            "Quel est le prix a payer ?",
            fcfa(net),
            uniq(fcfa(net), [fcfa(prix * remise / 100), fcfa(prix), fcfa(prix * (1 + remise / 100)),
                             fcfa(prix - remise)]),
            MOYEN, "entrepreneuriat,calcul,prix",
            f"Prix remise = {fcfa(prix)} x (1 - {remise}/100) = {fcfa(net)}.",
        ))

    # 8. TVA camerounaise ---------------------------------------------------
    for ht in [100000, 250000, 40000, 1500000, 75000, 320000, 60000, 850000]:
        ttc = ht * 1.1925
        qs.append(Q(
            f"Une prestation est facturee {fcfa(ht)} hors taxes. Avec une TVA de 19,25 %, "
            "quel est le montant toutes taxes comprises ?",
            fcfa(ttc),
            uniq(fcfa(ttc), [fcfa(ht * 1.1925 - ht), fcfa(ht), fcfa(ht * 1.18), fcfa(ht * 1.5)]),
            CHALLENGE, "entrepreneuriat,calcul,fiscalite",
            f"TTC = HT x 1,1925 = {fcfa(ht)} x 1,1925 = {fcfa(ttc)}.",
        ))

    # 9. Prix de revient ----------------------------------------------------
    for matieres, mo, autres in [(1200, 500, 300), (3500, 1500, 800), (600, 250, 150),
                                 (8000, 4000, 2500), (2200, 900, 400), (450, 200, 100),
                                 (15000, 6000, 3500), (1800, 700, 500)]:
        revient = matieres + mo + autres
        qs.append(Q(
            f"Pour fabriquer un produit, un artisan depense {fcfa(matieres)} de matieres, "
            f"{fcfa(mo)} de main-d'oeuvre et {fcfa(autres)} d'autres charges. Quel est son prix de revient ?",
            fcfa(revient),
            uniq(fcfa(revient), [fcfa(matieres + mo), fcfa(matieres), fcfa(revient * 2), fcfa(mo + autres)]),
            MOYEN, "entrepreneuriat,calcul,couts",
            f"Prix de revient = {fcfa(matieres)} + {fcfa(mo)} + {fcfa(autres)} = {fcfa(revient)}.",
        ))

    # 10. Panier moyen ------------------------------------------------------
    for ca, clients in [(450000, 150), (1200000, 300), (96000, 48), (750000, 250),
                        (330000, 110), (2400000, 480), (180000, 90), (560000, 140)]:
        panier = ca / clients
        qs.append(Q(
            f"Une boutique realise {fcfa(ca)} de ventes aupres de {clients} clients dans la semaine. "
            "Quel est le panier moyen ?",
            fcfa(panier),
            uniq(fcfa(panier), [fcfa(ca / (clients * 2)), fcfa(ca), fcfa(panier * 2), fcfa(clients)]),
            MOYEN, "entrepreneuriat,calcul,indicateurs",
            f"Panier moyen = CA / nombre de clients = {fcfa(ca)} / {clients} = {fcfa(panier)}.",
        ))

    # 11. Taux de croissance ------------------------------------------------
    for avant, apres in [(400000, 500000), (1200000, 1500000), (250000, 300000),
                         (800000, 1000000), (600000, 750000), (2000000, 2600000),
                         (150000, 195000), (900000, 1080000)]:
        croissance = (apres - avant) / avant * 100
        qs.append(Q(
            f"Le chiffre d'affaires est passe de {fcfa(avant)} a {fcfa(apres)} en un an. "
            "Quel est le taux de croissance ?",
            pct(croissance),
            uniq(pct(croissance), [pct((apres - avant) / apres * 100), pct(croissance * 2),
                                   pct(croissance / 2), pct(100 - croissance)]),
            CHALLENGE, "entrepreneuriat,calcul,indicateurs",
            f"Croissance = (nouveau - ancien) / ancien x 100 = {pct(croissance)}.",
        ))

    # 12. Rentabilite / marge nette ----------------------------------------
    for ca, benef in [(1000000, 150000), (2500000, 500000), (400000, 40000),
                      (750000, 60000), (3000000, 750000), (180000, 27000),
                      (5000000, 400000), (620000, 93000)]:
        taux = benef / ca * 100
        qs.append(Q(
            f"Une entreprise realise {fcfa(ca)} de chiffre d'affaires et {fcfa(benef)} de benefice. "
            "Quelle est sa rentabilite nette ?",
            pct(taux),
            uniq(pct(taux), [pct(benef / (ca - benef) * 100), pct(taux * 2), pct(taux / 2), pct(100 - taux)]),
            CHALLENGE, "entrepreneuriat,calcul,rentabilite",
            f"Rentabilite = benefice / CA x 100 = {pct(taux)}.",
        ))

    # 13. Retour sur investissement ----------------------------------------
    for invest, gain in [(500000, 150000), (1200000, 300000), (250000, 100000),
                         (2000000, 400000), (750000, 225000), (100000, 45000),
                         (3000000, 900000), (600000, 90000)]:
        roi = gain / invest * 100
        qs.append(Q(
            f"Un entrepreneur investit {fcfa(invest)} et obtient un gain net de {fcfa(gain)}. "
            "Quel est le retour sur investissement ?",
            pct(roi),
            uniq(pct(roi), [pct(invest / gain * 100), pct(roi * 2), pct(roi / 2), pct(100 + roi)]),
            CHALLENGE, "entrepreneuriat,calcul,investissement",
            f"ROI = gain / investissement x 100 = {pct(roi)}.",
        ))

    # 14. Mensualite d'un credit simple ------------------------------------
    for montant, taux_annuel, mois in [(1000000, 10, 12), (500000, 12, 10),
                                       (2000000, 8, 24), (300000, 15, 6),
                                       (1500000, 10, 18), (800000, 12, 12),
                                       (2500000, 9, 20), (600000, 14, 8)]:
        interets = montant * (taux_annuel / 100) * (mois / 12)
        mensualite = (montant + interets) / mois
        qs.append(Q(
            f"Un entrepreneur emprunte {fcfa(montant)} sur {mois} mois, avec un interet simple de "
            f"{taux_annuel} % par an. Quelle est approximativement la mensualite a rembourser ?",
            fcfa(mensualite),
            uniq(fcfa(mensualite), [fcfa(montant / mois), fcfa(montant + interets),
                                    fcfa(interets / mois), fcfa(mensualite * 2)]),
            CHALLENGE, "entrepreneuriat,calcul,financement",
            f"Total du = {fcfa(montant)} + {fcfa(interets)} d'interets, soit {fcfa(mensualite)} par mois.",
        ))

    # 15. Part de marche ----------------------------------------------------
    for ventes, marche in [(150000, 1000000), (400000, 2000000), (75000, 500000),
                           (1200000, 8000000), (90000, 450000), (250000, 1250000)]:
        part = ventes / marche * 100
        qs.append(Q(
            f"Une entreprise vend pour {fcfa(ventes)} sur un marche total estime a {fcfa(marche)}. "
            "Quelle est sa part de marche ?",
            pct(part),
            uniq(pct(part), [pct(part * 2), pct(part / 2), pct(100 - part), pct(marche / ventes)]),
            CHALLENGE, "entrepreneuriat,calcul,marche",
            f"Part de marche = ventes / marche total x 100 = {pct(part)}.",
        ))

    # 16. Prix de vente a partir d'une marge visee -------------------------
    for revient, marge_pct in [(1500, 40), (800, 25), (12000, 30), (2500, 50),
                               (400, 20), (6000, 35), (900, 60), (18000, 25)]:
        prix = revient * (1 + marge_pct / 100)
        qs.append(Q(
            f"Un produit coute {fcfa(revient)} a produire. L'entrepreneur veut une marge de {marge_pct} % "
            "sur ce cout. A quel prix doit-il le vendre ?",
            fcfa(prix),
            uniq(fcfa(prix), [fcfa(revient), fcfa(revient * marge_pct / 100),
                              fcfa(revient * (1 - marge_pct / 100)), fcfa(prix * 2)]),
            MOYEN, "entrepreneuriat,calcul,prix",
            f"Prix = cout x (1 + marge) = {fcfa(revient)} x {1 + marge_pct/100:.2f} = {fcfa(prix)}.",
        ))

    return qs
