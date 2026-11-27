# Formats de sortie

Deux livrables à chaque OVM : l'analyse interne complète (Format A), puis le document vendeur (Format B). Produire les deux, dans cet ordre, sauf si le courtier en demande un seul.

## Note pré-visite

Si le courtier n'a pas encore visité ou revisité la propriété, l'écrire clairement, en haut du Format A et en une phrase dans le Format B : l'opinion est établie sur papier, à partir des documents fournis, et sera confirmée après la visite. L'état de la propriété est alors présumé, et il faut le dire.

## Format A, analyse interne complète

Écrite pour le courtier, tutoiement, ton direct de collègue d'expérience. Dans cet ordre :

```
# Opinion de valeur marchande, [adresse complète]
```

**1. Profil du sujet**
Adresse, type, superficie, chambres et salles de bains, étage si applicable, année de construction, particularités, historique (inscriptions passées, expirations). Objectif du vendeur et sa date, s'ils sont connus. Mention « sur papier » si la visite reste à faire.

**2. Données utilisées**
Les PDF sortis (les trois niveaux, avec leurs critères), le nombre de vendus et d'actifs, la période couverte, la source, la date de l'extraction, et toute hypothèse posée faute de donnée.

**3. Comparables retenus**
3 à 5 comparables clés, un paragraphe chacun selon le gabarit de `grille-ajustements.md`.

**4. Comparables écartés**
Une phrase chacun sur pourquoi il pèse moins. Inclure les ventes que le vendeur connaît probablement (même rue, voisin, duProprio) et ce qu'il faudra lui répondre.

**5. Ajustements**
Ce qui tire la valeur du sujet vers le haut, ce qui la tire vers le bas, chaque point ancré dans un fait des documents. Aucun montant en dollars inventé.

**6. Analyse des vendus**
Ce que les ventes démontrent sur la valeur, selon la hiérarchie et les règles de `methode-generale.md`. L'écart entre le prix demandé initial et le prix vendu, et les délais réels.

**7. Analyse des actifs**
Où le sujet se classe contre sa compétition directe, au prix recommandé : parmi les trois meilleures de sa course, ou non.

**8. Absorption et marché**
Ventes par mois, mois d'inventaire, lecture selon les repères québécois. Par gamme de prix et par période quand l'échantillon le permet. La saison.

**9. Prix**
```
**Prix réaliste : XXX 000 $**
**Prix optimiste : YYY 000 $**
**Prix d'affichage recommandé : ZZZ 000 $**
```
La base de chaque prix, et une phrase qui justifie l'écart entre le réaliste et l'optimiste. Au besoin, la zone de vente probable et le point central.

**10. Stratégie et plan de baisse**
Le positionnement, l'effet attendu sur les visites, le délai de vente attendu. La date de la première réévaluation, les déclencheurs, le plancher. Jamais de date d'offres par défaut, jamais de prix d'appel sous la valeur (`strategie-prix.md`).

**11. Mise en marché**
Qui va acheter, pourquoi, et ce que la fiche doit dire. Les points du plan d'action qui comptent pour ce produit (`mise-en-marche.md`).

**12. La rencontre**
Ce que le vendeur a en tête, les objections probables et le fait du dossier qui répond à chacune, l'ordre de présentation (`presenter-au-vendeur.md`).

**13. Risques et renseignements à confirmer**
Ce qui pourrait empêcher le prix optimiste. Deux ou trois points précis à confirmer : état à la visite, données manquantes, calendrier.

Si une autre opinion a été fournie en référence (une autre IA, un autre courtier), en tenir compte à l'endroit pertinent, d'accord ou en désaccord, avec la raison.

Terminer sans formule de politesse. La dernière phrase est une conclusion.

## Format B, document vendeur

**Le document vendeur est factuel.** Des tableaux, des faits, une conclusion chiffrée dont chaque chiffre porte sa base (une vente ou une statistique citée). Il doit pouvoir être relu par un autre courtier, ou par l'OACIQ, sans qu'une seule phrase ait à être défendue.

Ce qu'il contient, avec des titres simples :
- **La propriété** : une ligne de description, sur le même modèle que les comparables.
- **Ventes comparables** : le tableau des vendus retenus, du moins cher au plus cher (prix vendu, délai, superficie, caractéristiques). Sans adresse complète.
- **Inscriptions en vigueur** : la compétition, sur le même modèle.
- **Le marché** : ventes par mois, mois d'inventaire, et au besoin le marché par période.
- **Conclusion** : le prix réaliste, le prix optimiste et le prix d'affichage recommandé, chacun avec sa base. Puis ce à quoi s'attendre : le délai probable et la date de la première réévaluation.

Ce qu'il ne contient jamais :
- aucune phrase de commentaire, aucune formule, aucun marché qui « dit », « voit », « attend » ou « répond » ;
- pas de paragraphe d'atouts et de limites raconté : la propriété entre dans le tableau comme les autres ;
- aucun conseil sur la fiche ou sur le travail d'un autre courtier ;
- aucun jargon d'analyse, aucun renvoi du genre « voir section 6 ».

Le courriel ou la conversation qui accompagne le document peut garder la voix du courtier. Le document, non.

Les PDF de comparables (`extraction-matrix.md`) se joignent au document ou se remettent à la rencontre, dans le format courtier. Le courtier n'a rien à cacher dans ce format, et le vendeur lit l'échelle des prix lui-même.

**Vouvoiement par défaut.** Le tutoiement seulement si le courtier tutoie déjà ce client. Dans la langue du client.

## Vocabulaire et style

- Français québécois professionnel ou anglais canadien, selon le client.
- Phrases courtes, voix active, aucun tiret cadratin.
- « Rétribution » plutôt que « commission » en français.
- Le document porte la signature du courtier et celle de son agence, rien d'autre.
- Pas de superlatifs vides.
- N'exagérez pas les forces, ne cachez pas les faiblesses.

## Sauvegarde

Sauvegarder le Format A et le Format B en docx ou markdown dans `Résultats/OVM/` du bureau IA du courtier, nommés avec l'adresse et la date. Les PDF de comparables et l'analyse vont aussi dans le dossier de la propriété : ils documentent le conseil donné (`strategie-prix.md`).
