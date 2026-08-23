#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les classeurs OSE à partir des séries du module STATISTIQUES de Matrix
(la formule courte du cahier One-on-One : Personnaliser, Ventes Nombre et
Nouvelles inscriptions nombre, regroupées par Mois).

Usage :
    python3 generer_depuis_module.py --gabarit template.xlsm --donnees donnees-module.json \
        --secteur "Ville Mont-Royal" --annees 2024 2025 2026 --dossier-sortie "…"

Entrée : le JSON à deux sections « ventes » et « inscrites », chacune
type -> b1..b5 -> année -> 12 valeurs. Les tranches viennent de la config.
Aucune retouche des chiffres : ce que le module donne entre dans le gabarit tel quel.
"""

import argparse
import json
import os
import shutil
import tempfile
import zipfile

from remplir_gabarit_ose import poser_valeurs, trouver_feuille_donnees, etiquette_gamme, COLS, L_VEN, L_INS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default=os.path.join(os.path.dirname(__file__), 'config-exemple.json'))
    ap.add_argument('--gabarit', required=True)
    ap.add_argument('--donnees', required=True)
    ap.add_argument('--secteur', required=True)
    ap.add_argument('--annees', nargs='+', type=int, required=True)
    ap.add_argument('--dossier-sortie', required=True)
    args = ap.parse_args()

    cfg = json.load(open(args.config, encoding='utf-8'))
    d = json.load(open(args.donnees, encoding='utf-8'))
    annees = sorted(args.annees, reverse=True)
    if len(annees) != 3:
        raise SystemExit('Le gabarit OSE compare exactement 3 années')

    for tcfg in cfg['types']:
        nom = tcfg['nom_feuille']
        tranches = tcfg['tranches']
        valeurs = {'D3': args.secteur, 'D15': nom}
        for g in range(5):
            valeurs[f'D{7+g}'] = etiquette_gamme(tranches[g])
        for k, a in enumerate(annees):
            valeurs[f'D{19+k}'] = a
        for k, a in enumerate(annees):
            for g in range(5):
                sv = d['ventes'][nom][f'b{g+1}'][str(a)]
                si = d['inscrites'][nom][f'b{g+1}'][str(a)]
                for m in range(12):
                    valeurs[f'{COLS[m]}{L_VEN[k]+g}'] = sv[m]
                    valeurs[f'{COLS[m]}{L_INS[k]+g}'] = si[m]

        tmp = tempfile.mkdtemp()
        with zipfile.ZipFile(args.gabarit) as z:
            z.extractall(tmp)
        poser_valeurs(trouver_feuille_donnees(tmp), valeurs)
        wb_xml_path = os.path.join(tmp, 'xl', 'workbook.xml')
        wb_xml = open(wb_xml_path, encoding='utf-8').read()
        if 'fullCalcOnLoad' not in wb_xml:
            import re
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
        tv = sum(sum(d['ventes'][nom][f'b{g+1}'][str(a)]) for g in range(5) for a in annees)
        ti = sum(sum(d['inscrites'][nom][f'b{g+1}'][str(a)]) for g in range(5) for a in annees)
        print(f'{nom}: {sortie} | ventes {tv} | inscrites {ti}')


if __name__ == '__main__':
    main()
