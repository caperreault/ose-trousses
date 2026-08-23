# Formats de sortie

Deux livrables à chaque OVM: l'analyse interne complète (Format A), puis la version vendeur (Format B). Produire les deux, dans cet ordre, sauf si le courtier demande explicitement un seul des deux.

## Note pré-visite

Si le courtier n'a pas encore visité ou revisité la propriété, l'écrire clairement, en haut du Format A et en une phrase dans le Format B: l'opinion est établie sur papier, à partir des documents fournis, et devra être confirmée après la visite. Ne jamais présenter une OVM sur papier comme définitive quand la visite reste à faire.

## Format A, analyse interne complète

Écrite pour le courtier, tutoiement, ton direct de collègue d'expérience. Suivre cet ordre exact:

```
# Opinion de valeur marchande, [adresse complète]
```

**1. Profil du sujet**
Adresse, type de propriété, superficie, chambres/salles de bains, étage si applicable, année de construction, particularités. Mentionner explicitement si l'opinion est établie sur papier (voir ci-dessus).

**2. Données utilisées**
Nombre de vendus et d'actifs analysés, période couverte, source (Matrix ou Centris), et toute hypothèse posée faute de donnée précise.

**3. Comparables retenus**
3 à 5 comparables clés, un paragraphe chacun selon le gabarit de `grille-ajustements.md`.

**4. Comparables écartés**
Les comparables qui apparaissaient dans les documents mais qui ne sont pas retenus, avec une phrase chacun sur pourquoi ils pèsent moins.

**5. Ajustements**
Synthèse qualitative: ce qui tire la valeur du sujet vers le haut, ce qui la tire vers le bas, en s'appuyant sur les comparables nommés à l'étape 3. Pas de liste générique, chaque point doit être ancré dans un fait des documents.

**6. Analyse des vendus**
Ce que les ventes comparables démontrent sur la valeur, en respectant la hiérarchie des comparables et les règles d'interprétation de `methode-generale.md`.

**7. Analyse des actifs**
Comment le sujet se positionne contre ce qui se vend actuellement dans le même segment: est-il mieux ou moins bien placé que la concurrence directe.

**8. Absorption**
Calcul et lecture selon `methode-generale.md`: ventes mensuelles, mois d'inventaire, ce que ça dit sur le rythme du marché pour ce segment.

**9. Fourchettes**
```
**Prix réaliste: XXX 000 $ à YYY 000 $**
**Prix optimiste: ZZZ 000 $ à WWW 000 $**
```
Une phrase qui justifie l'écart entre les deux fourchettes.

**10. Stratégie**
```
**Inscription à XXX 000 $ avec/sans date d'offres**
```
Justification: positionnement par rapport au marché, effet attendu sur le trafic, vente attendue dans quel intervalle, scénario exceptionnel possible si pertinent.

**11. Risques**
Ce qui pourrait empêcher d'atteindre le scénario optimiste, et les déclencheurs qui justifieraient un ajustement de prix après la mise en marché (ex: X visites sans offre après Y semaines, apparition d'un nouveau comparable qui change le portrait).

**12. Renseignements à confirmer**
2 à 3 points précis: données manquantes (évaluation municipale, etc.), timing du marché à respecter, argument à reformuler avant la mise en marché.

Si une analyse ou une opinion externe a été fournie en référence (une autre IA, un autre courtier), en tenir compte dans l'analyse: être d'accord ou en désaccord avec justification, à l'endroit pertinent (généralement dans les fourchettes ou la stratégie). Ce n'est pas une section dédiée obligatoire, seulement un point de comparaison quand il existe.

Terminer sans postambule (pas de "n'hésite pas", pas de "bonne chance avec la vente").

## Format B, version vendeur

Écrite pour le client du courtier, tutoiement, courte, professionnelle, directe, facile à comprendre, sans balise de référence technique (pas de "voir section 6", pas de jargon d'analyse). Dans la langue demandée par le courtier.

Contenu:
- Ce que le marché dit de la propriété, en langage simple, sans énumérer les comparables un par un.
- Le prix d'affichage recommandé, avec une justification courte et défendable.
- Ce à quoi s'attendre (délai probable, scénario si le marché répond bien).
- Une recommandation claire, pas une liste d'options à choisir.

Pas de fourchette réaliste/optimiste étalée comme dans le Format A: le vendeur a besoin d'une recommandation, pas d'un tableau d'analyse.

## Vocabulaire et style

- Français québécois professionnel ou anglais canadien, selon la langue demandée.
- Ton de courtier avec plus de 25 ans d'expérience: direct, factuel, sans remplissage.
- Phrases courtes, voix active.
- Aucun tiret cadratin.
- Utiliser "rétribution" plutôt que "commission" en français.
- Le document porte la signature du courtier et celle de son agence, rien d'autre.
- Ne pas exagérer les forces ni cacher les faiblesses de la propriété.
- Pas de superlatifs vides ("incroyable", "extraordinaire").
- Conclusion ferme à la fin, jamais une formule générique de clôture.

## Sauvegarde

Sauvegarder le Format A et le Format B en docx ou markdown dans `Résultats Claude/OVM/`, nommés avec l'adresse et la date.
