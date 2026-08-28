# Procédure Matrix pas à pas : la formule courte (module STATISTIQUES)

Méthode officielle du cahier One-on-One (Méthode 1), validée de bout en bout les 8 et 9 août 2026 sur un secteur réel : 30 passes (ventes et nouvelles inscriptions, 3 types x 5 gammes), critères vérifiés à chaque passe, résultats recoupés contre un décompte indépendant inscription par inscription. Matrix v12.6 (Cotality), interface française de Centris.

Tout se fait dans la session Matrix du courtier, déjà connectée dans Chrome. Aucun identifiant n'est saisi par l'assistant.

## A. Réglage du module (une fois par session de travail)

1. Menu **STATISTIQUES > Statistiques**, onglet **Personnaliser**.
2. Période : **5 années passées** (la période se termine au mois précédent).
3. Statistique : **« Ventes, Nombre »** pour la table des vendues, **« Nouvelles inscriptions, nombre »** pour la table des inscrites.
4. Regrouper par : **Mois**.

Le menu Statistique offre aussi « Prix de vente, moyen », « Prix demandé, moyen », les médians et les ratios vente/demandé : c'est là qu'on va chercher les moyennes pour proposer les gammes de prix (étape 1 du skill).

## B. Les critères, par passe

- **Localisation** : Région, puis Municipalité/Arrondissement.
- **Catégorie** : Unifamiliale; ou Copropriété/Appartement résidentiel; ou **Propriété à revenus AVEC Genre de propriété = Duplex, Triplex, Quadruplex, Quintuplex** pour les plex (les plex ne sont QUE là, jamais dans le commercial).
- **Prix Demandé/Vendu = la gamme** (formats : `0-1199999`, `1200000-1599999`, `2500000+`). Ce critère est ce qui exclut les locations, parce qu'une location n'a pas de prix de vente. Une passe sans critère de prix compte les baux loués avec les ventes.
- Générer, puis onglet **Données** : la table Mois x Années.

**Vérification obligatoire à chaque passe** : la ligne de critères affichée sous la table (catégorie, municipalité, prix, statistique) doit correspondre exactement à la passe demandée. On ne garde jamais des chiffres sans cette vérification.

## C. Extracteur de la table Données (console JavaScript)

```js
const tables = Array.from(document.querySelectorAll('table')).filter(t => /Mois/.test(t.innerText) && !/Préréglages/.test(t.innerText));
const t = tables[tables.length-1];
const rows = Array.from(t.querySelectorAll('tr')).map(r => Array.from(r.querySelectorAll('td,th')).map(c=>c.innerText.trim())).filter(r=>r.length>=4);
JSON.stringify(rows);
```

Entre les passes : onglet Recherche (`__doPostBack('m_btnCriteria','')`), changer le prix ou la catégorie, Générer (`m_btnGenerate`), Données (`m_btnData`). Laisser 2 à 3 secondes entre chaque action, le module est un formulaire à allers-retours serveur.

## D. Contrôles de cohérence avant de générer

1. **Le test des bornes.** La somme des 5 gammes d'une année doit recouper, au chiffre près, le total du même type obtenu avec UN critère de prix qui couvre tout (« 0 $ et plus »). Un écart ici veut dire un trou ou un chevauchement entre les gammes.
2. **Jamais contre le total sans critère de prix.** Le statut Vendu de Matrix inclut les baux loués : ce total compte les ventes ET les locations. L'écart n'est pas de quelques unités, il est énorme. Mesuré : Mont-Royal, 430 locations pour 509 ventes sur 3 ans (8 août 2026); LaSalle, 339 locations pour 255 ventes de copropriété en 2023 (28 août 2026). En unifamiliale l'écart est plus petit, autour de 15 %, mais bien réel. Un courtier qui recoupe contre ce total conclura à tort qu'il perd la moitié de ses ventes.
3. Les totaux annuels doivent être plausibles pour le secteur (un total qui double d'une passe à l'autre = un critère resté collé, refaire la passe).
4. Sur un marché mince (moins de 20 ventes en 3 ans), chaque chiffre se relit deux fois.

## E. Comparatif des méthodes (fait le 9 août 2026, pour ne pas refaire le débat)

| Méthode | Verdict |
|---|---|
| **Module Statistiques, Personnaliser** (formule courte, Méthode 1 du cahier) | **LA méthode.** Côté serveur, 30 petites passes, aucune manipulation d'affichage, critères vérifiables, mêmes définitions pour tous les courtiers du programme. |
| Recherches manuelles mois par gamme (formule longue, Méthode 2 du cahier) | Même résultat, environ 2 heures à la main. Reste la référence pédagogique du premier cycle et la voie de secours si le module est indisponible. |
| Moisson des résultats de recherche inscription par inscription | Abandonnée pour la production : elle exige d'insérer des colonnes d'affichage (manipulation instable) et découpe les mois par date d'acceptation plutôt que par changement de statut, ce qui décale légèrement les chiffres par rapport aux deux méthodes officielles. Utile seulement pour une analyse fine ponctuelle (distribution des prix vendus réels). |

Écart-type observé entre la moisson et le module sur un même secteur : 1 à 2 unités par gamme-année (bases de date et de prix différentes). Les deux méthodes officielles concordent entre elles.
