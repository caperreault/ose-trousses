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

### La section qui manque presque toujours: qui répond ici

C'est la partie qui transforme un dossier bien rangé en bureau qui fonctionne. Sans elle, le courtier ouvre une conversation dans son bureau et tombe sur un assistant générique qui ne sait pas que son associé existe.

Écrivez cette section en tête du CLAUDE.md, juste après les trois lignes qui disent qui il est:

```
## Qui répond ici

[Prénom de l'associé] est la porte d'entrée de ce bureau. Toute conversation
ouverte ici est une conversation avec lui: son mandat, son ton et ses règles
s'appliquent dès le premier message.

Avant de répondre, lis « Mes agents/[Prénom]/CLAUDE.md », puis sa mémoire.

Il délègue aux autres agents de l'équipe quand la demande est leur métier,
et il révise ce qu'ils produisent avant de me le remettre.
```

Adaptez le prénom à celui que le courtier a choisi. S'il n'a pas encore d'associé, écrivez la section quand même, avec une ligne qui dit qu'aucun associé n'est encore bâti et que la compétence `activer-un-agent` sert à en monter un.

**Ne recopiez jamais le contenu du CLAUDE.md de l'associé dans celui de la racine.** Vous écrivez où aller lire.

### Le reste de la table des matières

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

## Étape 7: le rapport

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
