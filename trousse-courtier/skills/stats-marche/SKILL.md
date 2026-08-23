---
name: stats-marche
description: "Produit les classeurs de statistiques de marché d'un secteur (gabarit OSE Coaching) à partir des données réelles de Matrix : ventes mensuelles et nouvelles inscriptions par gamme de prix sur 3 ans, un classeur imprimable par type de propriété (unifamiliale, copropriété, plex) pour les présentations de mise en vente. Utilise la formule courte officielle du programme (module Statistiques de Matrix, onglet Personnaliser). Déclenche ce skill quand un courtier demande de « mettre à jour mes statistiques de marché », « faire les stats de mon secteur », « remplir le gabarit stat de marché », « préparer mon rapport de secteur pour une présentation », ou nomme un secteur avec l'intention d'en sortir les chiffres. Outil du programme One-on-One d'OSE Coaching : requiert le gabarit Excel fourni dans le programme et un accès Matrix (Centris) avec la session du courtier ouverte dans Chrome."
---

# Les statistiques de marché de votre secteur

Tu produis pour un courtier immobilier les classeurs de statistiques de son secteur, remplis de données réelles tirées de sa propre session Matrix, selon la méthode officielle du programme One-on-One (la « formule courte » : Méthode 1 du cahier, module Statistiques de Matrix). Le résultat : un classeur par type de propriété, dans le gabarit OSE Coaching, prêt à imprimer.

**Le gabarit Excel appartient au programme One-on-One d'OSE Coaching et n'est pas dans ce skill.** Deux chemins, selon le courtier:

- **Il est dans le One-on-One:** son coach lui a remis le fichier `template stat de marché OSE Coaching.xlsm`. Demande-lui de le déposer dans son bureau, et travaille dedans. On travaille toujours sur une copie, jamais sur l'original.
- **Il n'est pas dans le coaching:** dis-le-lui simplement, sans détour et sans vendre. Puis propose-lui de monter son propre classeur avec toi: mêmes définitions, mêmes passes, même méthode, sa mise en page à lui. Le classeur qu'il bâtira lui appartiendra. La méthode ci-dessous fonctionne pareil.

Ne reproduis jamais le gabarit OSE de mémoire et ne le reconstitue pas à l'identique. Tu bâtis un classeur neuf, avec le courtier. Note du programme, à respecter : le cahier demande que ce travail soit fait par le courtier lui-même lors de son premier cycle, parce que le faire lui apprend son marché. Ce skill sert le courtier qui a déjà fait l'exercice et veut le maintenir à jour, ou celui dont le coach a convenu d'une autre approche.

## Les deux définitions qui gouvernent tout (ne jamais les confondre)

- **Propriétés Vendues** : le nombre de ventes du mois. Dans le module Statistiques : « Ventes, Nombre ».
- **Propriétés Inscrites** : les NOUVELLES inscriptions entrées en marché ce mois-là (peu importe leur sort ensuite), PAS l'inventaire en vigueur. Dans le module Statistiques : « Nouvelles inscriptions, nombre ». C'est l'offre contre la demande, la définition officielle du gabarit.
- **Plex** : catégorie « Propriété à revenus » avec genres Duplex à Quintuplex, uniquement. Jamais dans le commercial, et un immeuble à revenus de plus de 5 logements n'est pas un plex.
- Le critère de prix de chaque passe exclut naturellement les locations : toujours l'utiliser.

## Ce qu'il faut avant de commencer

1. **Le classeur** : celui de son coach s'il est dans le One-on-One, sinon celui qu'on monte ensemble. On travaille sur des copies, jamais sur l'original.
2. **La session Matrix du courtier ouverte dans Chrome.** Tu travailles dans SA session, avec SES accès. Tu ne saisis jamais d'identifiant : si la session est fermée, le courtier se connecte lui-même.
3. **Le secteur** (municipalité ou arrondissement Centris) et les 3 années à comparer.
4. Python 3 avec openpyxl, et Excel pour le test final.

## Les cinq étapes

### 1. Proposer les gammes de prix, décider avec le courtier

Le gabarit a 5 gammes par type : ni plus, ni moins. Avant de les fixer, va chercher dans le module Statistiques (Personnaliser) le **« Prix de vente, moyen »** et le **« Prix demandé, moyen »** du type sur le secteur, et au besoin « Ventes, Nombre » sur deux ou trois découpages candidats. Propose ensuite 5 gammes selon quatre critères : des bornes rondes qu'un client lit sans effort, aucune gamme vide, aucune gamme fourre-tout, et la gamme « coeur du marché » (autour des moyennes) qui ressort d'elle-même. Montre au courtier la répartition attendue de chaque gamme et fais-le décider : ses gammes, sa décision. On compare des pommes avec des pommes : les mêmes gammes servent aux deux tableaux, et le même critère de prix Matrix sert partout.

### 2. Extraire les ventes (formule courte, 15 passes)

Module STATISTIQUES > Personnaliser : Période « 5 années passées », Statistique « **Ventes, Nombre** », Regrouper par « **Mois** ». Puis pour chaque type et chaque gamme (3 x 5 = 15 passes) : poser la catégorie, la municipalité et le prix de la gamme, Générer, onglet Données, relever la table Mois x Années. À CHAQUE passe, vérifier la ligne de critères affichée sous la table avant de garder les chiffres. Procédure détaillée et extracteurs dans `references/procedure-matrix.md`.

### 3. Extraire les nouvelles inscriptions (15 passes)

Même mécanique, Statistique « **Nouvelles inscriptions, nombre** ». C'est la table « Propriétés Inscrites » du gabarit.

### 4. Générer les classeurs

Verser les 30 séries dans un JSON au format de `scripts/donnees-exemple.json`, puis `python3 scripts/generer_depuis_module.py`. Le script remplit la feuille Données par chirurgie de texte XML (les graphiques et la macro du gabarit restent intacts octet pour octet) et force le recalcul complet à l'ouverture. Un classeur par type. Aucun chiffre n'est retouché : ce que le module donne entre tel quel.

### 5. Vérifier AVANT de livrer

Règle absolue : un fichier généré se teste dans le logiciel qui va l'ouvrir. Ouvre chaque classeur dans Excel (ferme Excel d'abord s'il traîne une vieille copie), lis les totaux des feuilles Année et recoupe-les avec les séries extraites. Contre-vérification de cohérence : la somme des gammes d'une année doit recouper le total sans filtre de prix à quelques unités près (l'écart, ce sont les locations). Un écart inexpliqué = on cherche avant de livrer.

## Garde-fous permanents

- **Aucun chiffre inventé.** Tout vient de Matrix. Une passe manquée reste un trou signalé, jamais une valeur estimée.
- **Les données restent chez le courtier.** Ses extractions et ses classeurs ne servent qu'à lui.
- **Le prix reste sa décision.** Les statistiques décrivent le marché, elles ne fixent rien.
- **Marché mince, prudence affichée** : sous 20 ventes en 3 ans pour un type (les plex, souvent), le dire au courtier : chaque vente pèse lourd dans les pourcentages.
- La période du module s'arrête au mois précédent : le classeur est « à jour au [dernier mois complet] », et on le dit.
- Terminologie québécoise : inscription, promesse d'achat, courtier, rétribution, en vigueur. Jamais de tiret cadratin.
- À la fin, rappelle au courtier de vérifier ses chiffres clés avant de les présenter à un client.

## Mise à jour récurrente

La mise à jour mensuelle reprend les mêmes passes (chaque passe redonne l'historique complet, elle se corrige donc toute seule) et régénère les classeurs : une quinzaine de minutes. Propose au courtier de la caler au début de chaque mois, comme le veut le programme.
