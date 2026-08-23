#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remplit le gabarit OSE Coaching (template stat de marché OSE Coaching.xlsm) sans casser
ses graphiques ni ses macros : le fichier est modifié au niveau XML (zip), seule la feuille
Données est touchée, tout le reste reste octet pour octet identique.

Le gabarit est mono-type : un classeur par type de propriété.

Usage :
    python3 remplir_gabarit_ose.py --gabarit template.xlsm --vendus moisson-vendus.txt \
        --envigueur moisson-envigueur.txt --secteur "Ville Mont-Royal" \
        --annees 2024 2025 2026 --mois-photo 8 --dossier-sortie "…/Statistiques de marché"

Structure de la feuille Données (gabarit OSE) :
    D3 secteur, D7:D11 gammes (texte), D15 type, D19:D21 années (décroissant),
    Vendues E24:P28 (année 1), E31:P35 (année 2), E38:P42 (année 3),
    Inscrites E45:P49 (année 1), E52:P56 (année 2), E59:P63 (année 3).
La table « Propriétés Inscrites » est traitée comme l'inventaire en vigueur (même sens que
le fichier 2019 : la feuille Année affiche « Total en vigueur ») : photo du mois-photo,
année la plus récente seulement.
"""

import argparse
import json
import os
import re
import shutil
import tempfile
import zipfile
import xml.etree.ElementTree as ET

NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
ET.register_namespace('', NS)

COLS = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
L_VEN = {0: 24, 1: 31, 2: 38}   # index d'année (0 = plus récente) -> première ligne du bloc Vendues
L_INS = {0: 45, 1: 52, 2: 59}


def parse(fichier):
    rows = []
    for ligne in open(fichier, encoding='utf-8'):
        seg = [s.strip() for s in ligne.strip().strip('|').split('|') if s.strip() != '']
        if not seg or not re.match(r'^\d{7,8}$', seg[0]):
            continue
        while len(seg) > 1 and seg[1] not in ('VE', 'EV'):
            seg.pop(1)
        if len(seg) < 5:
            continue
        reste = seg[4:]
        if '$/m' in reste[0]:
            continue
        m = re.match(r'^([\d\s  ]+)\$', reste[0])
        if not m:
            continue
        prix = int(re.sub(r'\D', '', m.group(1)))
        cats = [s for s in reste if s in ('UNI', 'COP', 'PPR', 'PCI', 'TER', 'FER')]
        gps = [s for s in reste if s in ('4X', '3X', '2X', '5X', 'APP', 'ME', 'PP', 'MPM', 'AUT', 'LS', 'MA', 'M15', 'MM', 'IND', 'QDX')]
        dm = [s for s in reste if re.match(r'^\d{4}-\d{2}-\d{2}$', s)]
        rows.append((cats[0] if cats else None, gps[0] if gps else None, prix, dm[0] if dm else None))
    return rows


def type_grille(cp, gp):
    if cp == 'UNI':
        return 'Unifamiliale'
    if cp == 'COP':
        return 'Copropriété'
    if cp == 'PPR' and gp in ('2X', '3X', '4X', '5X'):
        return 'Plex'
    return None


def idx_tranche(prix, tranches):
    for i, t in enumerate(tranches):
        hi = t['max'] if t['max'] is not None else float('inf')
        if t['min'] <= prix <= hi:
            return i
    return None


def etiquette_gamme(t):
    f = lambda x: f"{x:,}".replace(',', ' ')
    if t['max'] is None:
        return f"{f(t['min'])}$ et plus"
    if t['min'] == 0:
        return f"0 à {f(t['max'])}$"
    return f"{f(t['min'])}$ à {f(t['max'])}$"


def trouver_feuille_donnees(tmp):
    wbx = ET.parse(os.path.join(tmp, 'xl', 'workbook.xml'))
    rels = ET.parse(os.path.join(tmp, 'xl', '_rels', 'workbook.xml.rels'))
    rns = '{http://schemas.openxmlformats.org/package/2006/relationships}'
    rid = None
    for s in wbx.getroot().iter(f'{{{NS}}}sheet'):
        if s.get('name') == 'Données':
            rid = s.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
    cible = None
    for r in rels.getroot().iter(f'{rns}Relationship'):
        if r.get('Id') == rid:
            cible = r.get('Target')
    if not cible:
        raise SystemExit("Feuille Données introuvable dans le gabarit")
    return os.path.join(tmp, 'xl', cible.lstrip('/'))


def poser_valeurs(chemin_xml, valeurs):
    """valeurs : dict 'D3' -> texte (str) ou nombre (int).

    Chirurgie par texte : on ne remplace que le fragment <c r="REF" ...>...</c> de chaque
    cellule visée, le reste du document (espaces de noms, attributs mc:Ignorable, styles)
    reste strictement intact. Une réécriture par ElementTree casse les prefixes déclarés
    dans l'en-tête de la feuille et Excel refuse alors le fichier (constaté le 8 août 2026).
    """
    xml = open(chemin_xml, encoding='utf-8').read()
    for ref, v in valeurs.items():
        motif = re.compile(r'<c r="' + ref + r'"([^>]*?)(/>|>.*?</c>)', re.DOTALL)
        m = motif.search(xml)
        if not m:
            raise SystemExit(f"Cellule {ref} absente du gabarit, rien d'écrit")
        attrs = m.group(1)
        ms = re.search(r'\ss="(\d+)"', attrs)
        s_attr = f' s="{ms.group(1)}"' if ms else ''
        if isinstance(v, str):
            texte = v.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            neuf = f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{texte}</t></is></c>'
        else:
            neuf = f'<c r="{ref}"{s_attr}><v>{v}</v></c>'
        xml = xml[:m.start()] + neuf + xml[m.end():]
    open(chemin_xml, 'w', encoding='utf-8').write(xml)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default=os.path.join(os.path.dirname(__file__), 'config-exemple.json'))
    ap.add_argument('--gabarit', required=True)
    ap.add_argument('--vendus', required=True)
    ap.add_argument('--envigueur', required=True)
    ap.add_argument('--secteur', required=True)
    ap.add_argument('--annees', nargs='+', type=int, required=True)
    ap.add_argument('--mois-photo', type=int, required=True)
    ap.add_argument('--inscrites', default=None, help='JSON des séries mensuelles d\'inscriptions en vigueur (module Statistiques de Matrix)')
    ap.add_argument('--dossier-sortie', required=True)
    args = ap.parse_args()

    cfg = json.load(open(args.config, encoding='utf-8'))
    series_inscrites = None
    if args.inscrites:
        series_inscrites = json.load(open(args.inscrites, encoding='utf-8'))['series']
    annees = sorted(args.annees, reverse=True)   # ordre décroissant, comme le gabarit
    if len(annees) != 3:
        raise SystemExit('Le gabarit OSE compare exactement 3 années')

    vendus = parse(args.vendus)
    actifs = parse(args.envigueur)

    for tcfg in cfg['types']:
        nom = tcfg['nom_feuille']
        tranches = tcfg['tranches']
        ventes = {a: [[0] * 12 for _ in tranches] for a in annees}
        for cp, gp, prix, date in vendus:
            if not date or type_grille(cp, gp) != nom:
                continue
            a, m = int(date[:4]), int(date[5:7])
            i = idx_tranche(prix, tranches)
            if a in ventes and i is not None:
                ventes[a][i][m - 1] += 1
        inv = [0] * len(tranches)
        for cp, gp, prix, _ in actifs:
            if type_grille(cp, gp) != nom:
                continue
            i = idx_tranche(prix, tranches)
            if i is not None:
                inv[i] += 1

        valeurs = {'D3': args.secteur, 'D15': nom}
        for g in range(5):
            valeurs[f'D{7+g}'] = etiquette_gamme(tranches[g])
        for k, a in enumerate(annees):
            valeurs[f'D{19+k}'] = a
        for k, a in enumerate(annees):
            for g in range(5):
                for m in range(12):
                    valeurs[f'{COLS[m]}{L_VEN[k]+g}'] = ventes[a][g][m]
                    if k == 0 and m == args.mois_photo - 1:
                        v_ins = inv[g]
                    elif series_inscrites is not None:
                        v_ins = series_inscrites[nom][f'b{g+1}'][str(a)][m]
                    else:
                        v_ins = 0
                    valeurs[f'{COLS[m]}{L_INS[k]+g}'] = v_ins

        tmp = tempfile.mkdtemp()
        with zipfile.ZipFile(args.gabarit) as z:
            z.extractall(tmp)
        poser_valeurs(trouver_feuille_donnees(tmp), valeurs)

        # Recalcul complet à l'ouverture : les valeurs posées au niveau XML ne marquent pas
        # les formules dépendantes comme périmées, Excel afficherait les caches du gabarit
        # (des zéros). fullCalcOnLoad force Excel à tout recalculer en ouvrant.
        wb_xml_path = os.path.join(tmp, 'xl', 'workbook.xml')
        wb_xml = open(wb_xml_path, encoding='utf-8').read()
        if 'fullCalcOnLoad' not in wb_xml:
            if '<calcPr' in wb_xml:
                wb_xml = re.sub(r'<calcPr ', '<calcPr fullCalcOnLoad="1" ', wb_xml, count=1)
            else:
                wb_xml = wb_xml.replace('</workbook>', '<calcPr calcId="191029" fullCalcOnLoad="1"/></workbook>')
            open(wb_xml_path, 'w', encoding='utf-8').write(wb_xml)

        slug = nom.lower().replace('é', 'e').replace('É', 'e')
        sortie = os.path.join(args.dossier_sortie, f'stats-{args.secteur.lower().replace(" ", "-")}-{slug}-{annees[-1]}-{annees[0]}.xlsm')
        if os.path.exists(sortie):
            os.remove(sortie)
        with zipfile.ZipFile(sortie, 'w', zipfile.ZIP_DEFLATED) as z:
            for base, _, fichiers in os.walk(tmp):
                for f in fichiers:
                    plein = os.path.join(base, f)
                    z.write(plein, os.path.relpath(plein, tmp))
        shutil.rmtree(tmp)
        total = sum(sum(sum(mois) for mois in ventes[a]) for a in annees)
        print(f'{nom}: {sortie} | ventes {total} | inventaire {sum(inv)}')


if __name__ == '__main__':
    main()
