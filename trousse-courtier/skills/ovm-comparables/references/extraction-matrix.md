# Sortir les comparables de Matrix

Le courtier demande souvent « fais-moi les comparables » sans avoir sorti les données. Ce fichier dit comment les obtenir, selon la méthode OSE. L'analyse, elle, est dans `methode-generale.md`.

Contexte vérifié : Matrix v12.6 (Cotality), interface française de Centris, dans la session du courtier ouverte dans Chrome. **Aucun identifiant n'est saisi par l'assistant, jamais.**

## Les deux chemins, et lequel proposer

| Le chemin | Quand | Ce qu'il donne |
|---|---|---|
| **Le courtier exporte en PDF** | Toujours possible, même si rien n'est branché | Les trois niveaux ci-dessous, avec photos et remarques |
| **L'assistant travaille dans sa session ouverte** | Chrome ouvert, session Matrix ouverte, il vous dit d'y aller | La même chose, sans les allers-retours |

Proposez les deux en une phrase, laissez-le choisir :

> Deux chemins. Vous sortez vos vendus et vos en vigueur en PDF et vous me les glissez, ou vous ouvrez votre session Matrix dans Chrome et je vais les chercher avec vous. Lequel?

**Ne dites jamais que vous n'avez pas accès à Matrix.** Le deuxième chemin existe, et le premier fonctionne toujours.

## La méthode OSE : trois niveaux, toujours en prix croissant

| Niveau | Format Matrix | Recherche | Ce qu'il montre |
|---|---|---|---|
| **1. La liste partielle** | Une propriété par ligne, environ 100 lignes par page | Le secteur précis et le type, assez large | Combien de propriétés se sont vendues et combien sont à vendre : l'offre et la demande d'un coup d'œil. C'est la base du calcul d'absorption. |
| **2. Le 4 par page courtier** | « 4 par page courtier » | Plus cadrée : ce qui ressemble au sujet (type, gamme de prix, superficie, caractéristiques) | Les vrais candidats. 20, 30 ou 40 propriétés, c'est correct. |
| **3. Les fiches détaillées** | « Détaillé courtier (Impérial) » avec photos | De 2 à 4 propriétés très semblables | La comparaison photo contre photo avec le sujet. Obligatoire pour une propriété du même immeuble ou presque identique. |

**Chaque niveau se sort deux fois : les vendus, puis les en vigueur** (la compétition).

**Toujours en prix croissant**, du moins cher au plus cher, vendus comme en vigueur. Le tri par défaut de Matrix (municipalité, rue, numéro) oblige à chercher. Le tri par prix donne une échelle où le vendeur voit tout de suite où sa propriété se situe. Triez par la colonne Prix avant d'imprimer, puis vérifiez dans le PDF que la suite des prix monte.

**Nommez les PDF par leur contenu** : « 18 vendus depuis 1er janvier 2026 - 400 à 500 k$ », « 24 en vigueur - compétition nov. 2026 », « Même immeuble ». Le nom dit déjà le décompte.

Ajoutez au besoin :
- **les expirés et les retirés** du secteur, surtout pour une réévaluation : ce sont les prix que le marché a refusés ;
- **l'historique du sujet** (tous statuts) : une propriété déjà expirée une ou plusieurs fois arrive stigmatisée, et il faut le savoir avant le rendez-vous ;
- **les vendus de la même rue**, même s'ils ne ressemblent pas au sujet, et les ventes de duProprio s'il y en a. Le vendeur les connaît. Ils vont sur une feuille à part, pas dans l'analyse.

## Ce qu'il faut décider avant de chercher

Cinq critères, décidés avec le courtier. Ne les devinez pas, ce sont ses choix de professionnel.

1. **Le secteur.** Municipalité ou arrondissement, et s'il le faut, le quadrilatère. Un rayon trop large fabrique des comparables qui n'en sont pas.
2. **La catégorie.** Unifamiliale, Copropriété/Appartement résidentiel, ou Propriété à revenus avec le genre (duplex à quintuplex). Un plex n'est jamais dans le commercial. En copropriété, gardez les divises ET les indivises : le type de copropriété est un facteur à analyser, pas un filtre (voir `methode-generale.md`).
3. **La période.** Par défaut, depuis le 1er janvier de l'année en cours : c'est le marché d'aujourd'hui. Puis réglez-la sur le volume. Beaucoup de ventes : quelques mois suffisent. Peu de ventes : remontez, jusqu'à deux ou trois ans pour un produit rare ou de luxe, en le disant. Un bon échantillon passe avant une période fixe. Cinq ans, c'est trop loin, le marché a trop changé.
4. **La fourchette de prix.** Autour du sujet, assez large pour ne rien manquer.
5. **Les caractéristiques qui comptent** pour ce sujet : superficie, chambres, étage, garage (simple ou double), maison à étages ou à paliers, année.

## Le piège du statut Vendu

**Le statut Vendu de Matrix inclut les baux loués.** Sans critère de prix, une recherche compte les ventes et les locations ensemble. En copropriété, l'écart est énorme : mesuré à Mont-Royal, 430 locations pour 509 ventes sur trois ans. En unifamiliale, autour de 15 %, mais bien réel.

**Chaque recherche porte donc un critère de prix, sans exception.** Une location n'a pas de prix de vente : dès qu'un critère de prix existe, elle sort du décompte.

Un courtier qui voit passer des « ventes » à 1 800 $ vient de compter des baux.

## Le piège des jours sur le marché

**Le délai affiché par Matrix part de la signature du contrat de courtage, pas de la mise en marché.** Avant de citer un délai, lisez la note du courtier inscripteur (« mise sur le marché le », « les visites débuteront le »). Un « 161 jours » peut en valoir 6. Un vendeur qui trouve l'erreur ne croit plus le reste du dossier.

## Ce qu'il faut relever pour chaque comparable

Une fiche incomplète est un comparable écarté, pas un comparable moyen.

- Adresse
- Prix demandé initial (champ « Prix original »), prix demandé final, prix vendu
- Date d'inscription, date de mise en marché réelle, date de vente
- Superficie habitable, et sa source
- Terrain, chambres, salles de bains, étage, garage
- Année de construction
- Taxes, évaluation municipale
- Copropriété : divise ou indivise, frais mensuels et ce qu'ils incluent
- Plex : loyers, qui paie le chauffage, logement libre ou non
- Les remarques de la fiche, où se cachent les rénovations et les défauts

**L'écart entre le prix demandé initial et le prix vendu**, croisé avec le délai réel, vaut autant que le prix lui-même. C'est ce qui dit si le marché a couru ou négocié.

## Travailler dans sa session

Quand le courtier a ouvert Matrix et vous a dit d'y aller :

- **Lisez la page avant d'agir.** Les critères affichés font foi, pas votre souvenir.
- **Vérifiez la ligne de critères** avant de garder des chiffres : catégorie, secteur, période, prix. Une passe dont les critères ne correspondent pas est une passe à refaire.
- **Laissez respirer entre les actions.** Le module est un formulaire à allers-retours serveur, deux ou trois secondes.
- **Si la session tombe**, arrêtez et dites-le. Ne recommencez pas à l'aveugle.
- **Ne modifiez rien** dans son compte : aucune recherche enregistrée effacée, aucun réglage changé, aucun envoi à un client.

## Ce que vous rendez au courtier

1. Les PDF des trois niveaux, vendus et en vigueur, triés par prix et nommés par leur contenu.
2. Un tableau des comparables, avec pour chacun sa source et la date de l'extraction.
3. Ceux que vous auriez retenus mais dont il manque une donnée.
4. Ce que vous n'avez pas pu sortir, et ce qu'il faut pour l'obtenir.

**Les PDF restent au dossier du courtier**, dans le dossier de la propriété. Ils prouvent sur quoi le prix a été conseillé si une question arrive plus tard (voir `strategie-prix.md`).

Ensuite seulement, l'analyse de `methode-generale.md`.

## L'avertissement qui ne saute jamais

**Le choix final des comparables appartient au courtier.** Vous ne voyez que des fiches. Vous ne savez pas que la maison donne sur l'autoroute, que le sous-sol a pris l'eau, ni ce qui s'est passé dans la négociation. Lui le sait.

Vous sortez les données et vous montez l'argumentaire. Le chiffre reste à lui.
