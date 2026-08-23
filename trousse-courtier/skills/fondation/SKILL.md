---
name: fondation
description: >-
  Vérifie, répare et complète le bureau IA d'un courtier immobilier: le fichier CLAUDE.md à la racine, les quatre sous-dossiers, la liste de lecture de son assistant, son calendrier IA neutre et sa routine du matin. À utiliser quand le courtier dit « vérifie ma fondation », « est-ce que mon bureau est bien monté », « répare mon bureau IA », « mon assistant ne se souvient de rien », « on commence le Jour 2 », « je viens d'installer la trousse », ou au tout premier passage après l'installation de la trousse OSE. À utiliser aussi quand un assistant semble ignorer le contexte du courtier alors que les fichiers existent.
---

# La fondation

Vous vérifiez le bureau IA d'un courtier immobilier du Québec et vous réparez ce qui manque. C'est la première compétence qui tourne après l'installation de la trousse.

**Ce courtier sort d'une formation. Il n'a pas envie d'un diagnostic technique.** Il veut savoir que son affaire est solide. Travaillez en silence, réparez, et livrez un rapport court à la fin.

Trois cas se présentent, souvent dans la même salle: le bureau est complet, le bureau est à moitié monté, le bureau a des fichiers vides. Vous gérez les trois sans jamais faire sentir au courtier qu'il est en retard sur son voisin.

## Étape 1: le bon dossier

Regardez le dossier ouvert dans la conversation.

- Il s'appelle « Mon bureau IA » ou l'équivalent chez ce courtier: continuez.
- Il porte un autre nom et ne contient ni `CLAUDE.md` ni « À propos de moi »: **arrêtez tout de suite.** Dites au courtier que la conversation n'est pas ouverte sur son bureau, et expliquez le geste: cliquer le sélecteur de dossier en haut, choisir « Mon bureau IA » dans les dossiers récents. Ne créez jamais un deuxième bureau par-dessus le premier.

## Étape 2: l'inventaire, en silence

Sans rien dire encore, faites le tour:

| Ce que vous cherchez | Ce que vous notez |
|---|---|
| `CLAUDE.md` à la racine | Absent, vide, ou rempli |
| `À propos de moi/` | Quels fichiers existent, lesquels sont vides |
| `Exemples/`, `Projets/`, `Résultats/` | Présents ou non |
| `Mes agents/` | Quels agents existent |
| Le `CLAUDE.md` de chaque agent | Sa liste de lecture pointe-t-elle vers des fichiers réels |

Un fichier de moins de 200 caractères compte comme vide. C'est le cas le plus fréquent: le fichier a été créé au Jour 1 et jamais rempli.

## Étape 3: écrire le CLAUDE.md de la racine

C'est le coeur du travail. Ce fichier est le premier que vous lirez chaque fois que ce courtier ouvre son bureau. Sans lui, chaque conversation repart de zéro.

Écrivez-le à partir de ce qui existe VRAIMENT dans le dossier, jamais à partir d'un modèle. Structure:

1. **Qui est ce courtier**, en trois lignes maximum. Tirez-les de son fichier à propos de moi s'il est rempli. S'il est vide, écrivez trois lignes provisoires et dites-le-lui à la fin.
2. **Ses fichiers et à quoi chacun sert**, avec le chemin exact. Une ligne par fichier. Ne listez que ce qui existe.
3. **Ses agents**, s'il en a: le nom, le mandat en une ligne, le chemin.
4. **Ses règles permanentes**: aucun envoi, aucune donnée inventée, aucun avis juridique ou fiscal.

**Vous écrivez où aller lire, jamais quoi lire.** Ne recopiez jamais le contenu d'un fichier dans le CLAUDE.md. Deux copies de la même information finissent toujours par se contredire, et c'est le courtier qui paie la facture six mois plus tard.

Si le fichier existe déjà et qu'il est rempli: ne l'écrasez pas. Ajoutez ce qui manque, corrigez les chemins morts, laissez le reste intact.

## Étape 4: réparer la liste de lecture des agents

Ouvrez le `CLAUDE.md` de chaque agent dans `Mes agents/`. Sa liste de lecture doit pointer vers des fichiers qui existent.

Le défaut classique: la liste nomme `../../À propos de moi/ma-voix.md` alors que le fichier n'a jamais été créé. L'agent ne plante pas. Il lit dans le vide, en silence, à chaque conversation. C'est le pire genre de bris parce que personne ne le voit.

Pour chaque chemin mort: soit le fichier existe sous un autre nom et vous corrigez le chemin, soit il n'existe pas et vous retirez la ligne en la notant pour le rapport.

## Étape 5: le calendrier IA

Demandez au courtier s'il a un calendrier séparé pour son assistant. La plupart n'en ont pas.

Expliquez-lui pourquoi en une phrase: **votre assistant n'écrit jamais dans votre vrai agenda.** Il dépose ce qu'il trouve dans un calendrier à part, que vous regardez quand ça vous convient, et vous glissez vous-même dans le vôtre ce qui est bon. Un rendez-vous ajouté par erreur dans le calendrier partagé avec la famille, ça arrive une fois et ça se paie longtemps.

Donnez-lui le geste selon son outil. Une seule fois, sans faire un cours:

- **Calendrier Apple:** menu Fichier, Nouveau calendrier, nommez-le `IA`.
- **Google Agenda:** dans la colonne de gauche, le plus à côté de « Autres agendas », Créer un agenda, nommez-le `IA`.
- **Outlook:** onglet Calendrier, Ajouter un calendrier, Créer un calendrier vierge, nommez-le `IA`.

Quand c'est fait, notez le nom exact du calendrier dans le CLAUDE.md, section des règles. Toutes les autres compétences le liront là.

## Étape 6: la routine du matin

Vérifiez si le courtier a une routine du matin dans son bureau. Sinon, écrivez `Projets/ma-routine-du-matin.md` avec la commande de son brief quotidien, et montrez-lui comment la lancer.

Ne la lancez pas maintenant. Ses connexions ne sont peut-être pas branchées, et un brief vide au premier essai fait mauvaise impression. Dites-lui simplement où elle est et quand l'utiliser.

## Étape 7: la règle à corriger dans ses réglages

Vous ne pouvez pas lire les réglages de son application. Vous pouvez seulement lui donner le geste.

Dites-lui: dans vos instructions globales, la règle qui commence par « Ne me demande jamais de renseignements personnels de mes clients » est trop large. Elle va bloquer votre assistant le jour où vous lui donnerez une vraie promesse d'achat à traiter. Remplacez-la par celle-ci:

> Les noms de mes clients, de mes collaborateurs et de mes fournisseurs font partie de mon travail: utilise-les normalement et ne me propose jamais de les anonymiser. Ce qui ne doit jamais entrer dans une conversation: un numéro d'assurance sociale, un numéro de compte ou de carte, une copie de pièce d'identité, un mot de passe. Si j'en colle un par erreur, signale-le tout de suite.

Ne lui faites pas chercher la ligne parmi les autres. Le geste le plus rapide est de tout sélectionner dans la boîte et de recoller son bloc au complet, corrigé.

Une règle trop large finit par bloquer le travail utile. Celle-ci protège ce qui compte vraiment et laisse passer le reste.

## Étape 8: le rapport

Court. Quatre lignes maximum, dans cet ordre:

1. **Ce que j'ai réparé.** La liste, sans dramatiser.
2. **Ce qui est prêt.** Ce qu'il peut faire tout de suite.
3. **Ce qui reste à vous.** Les fichiers vides qu'il est le seul à pouvoir remplir, avec une phrase sur ce que ça débloquerait.
4. **Un test immédiat.** Proposez-lui UNE chose à essayer dans la minute. Exemple: « Demandez-moi un courriel de suivi pour votre dernier acheteur. Vous allez voir la différence maintenant que je vous connais. »

Ne livrez jamais une liste de fichiers créés. Livrez un bureau qui fonctionne.

## Ce que cette compétence ne fait jamais

- Elle ne crée jamais un deuxième bureau par-dessus un bureau existant.
- Elle n'écrase jamais un fichier rempli. Elle complète.
- Elle ne supprime rien.
- Elle ne remplit jamais à la place du courtier ce que lui seul sait: sa voix, son secteur, ses chiffres. Elle prépare la place et elle le dit.
