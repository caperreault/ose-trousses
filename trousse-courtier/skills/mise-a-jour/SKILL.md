---
name: mise-a-jour
description: >-
  Vérifie si la trousse du courtier est à jour, guide la réinstallation quand elle ne l'est pas, confirme après coup et fait essayer une nouveauté tout de suite. À utiliser quand le courtier dit « mets ma trousse à jour », « est-ce que ma trousse est à jour », « quoi de neuf dans ma trousse », « j'ai la dernière version? », « update my toolkit », « il paraît qu'il y a du nouveau », ou quand une compétence qu'il nomme n'existe pas chez lui. À utiliser aussi de vous-même, une seule fois, si vous constatez que sa trousse est en retard pendant un autre travail.
---

# Mettre la trousse à jour

Le courtier veut savoir s'il a la dernière version, et l'avoir. Vous faites le tour vous-même et vous ne lui donnez que des gestes.

**Vous ne pouvez pas installer le plugin à sa place.** L'installation passe par l'application, c'est lui qui clique. Votre travail: lui dire s'il en a besoin, lui donner les quatre gestes, confirmer après, et lui faire essayer une nouveauté tout de suite. Sans cette dernière partie, une trousse à jour ne change rien à sa semaine.

## Étape 1: quelle version il a, en silence

Lisez le fichier `installed_plugins.json` dans le dossier `.claude/plugins` de son compte.

- Sur Mac: `~/.claude/plugins/installed_plugins.json`
- Sur PC: le même chemin sous son dossier d'utilisateur, `.claude\plugins\installed_plugins.json`

Cherchez la clé **`trousse-courtier@ose-trousses`**. Elle donne deux choses: `version`, et `installPath`, le dossier réellement chargé.

Vérifiez ensuite ce que ce dossier contient vraiment: listez `installPath/skills`. C'est la seule preuve de ce qui tourne chez lui. Le nombre de compétences vous dit tout de suite où il en est.

Si la clé est absente, la trousse n'est pas installée sous ce compte: allez directement à l'étape 3, les quatre gestes règlent aussi ce cas.

## Étape 2: quelle version existe

Allez lire la version publiée:

`https://raw.githubusercontent.com/caperreault/ose-trousses/main/trousse-courtier/.claude-plugin/plugin.json`

Si vous n'arrivez pas à la lire, ne bloquez pas et ne lui demandez pas de la chercher. Dites-lui simplement que vous ne pouvez pas comparer aujourd'hui, et proposez la réinstallation quand même: réinstaller une trousse déjà à jour ne casse rien et prend deux minutes.

## Étape 3: le verdict, et seulement le verdict

**Si les versions sont identiques**, une phrase, puis sautez à l'étape 5:

> Votre trousse est à jour, version X, vingt compétences chargées.

**Si sa version est en retard**, dites l'écart en une ligne, puis les quatre gestes, sans rien autour:

> Vous êtes sur la version X, la version en ligne est la Y. Deux minutes:
> 1. Dans une conversation, le bouton **+** à côté de la boîte de message, puis Plugins.
> 2. Collez cette adresse: https://github.com/caperreault/ose-trousses
> 3. Installez trousse-courtier.
> 4. Fermez cette conversation et ouvrez-en une neuve.
>
> Vos fichiers, vos agents et votre mémoire ne sont pas touchés. Une conversation charge ses outils à l'ouverture, jamais après: c'est pour ça qu'il en faut une neuve.
> Dans la nouvelle, retapez `/`, écrivez « trousse », et choisissez `trousse-courtier: mise-a-jour` dans la liste. Je confirme que c'est passé et je vous montre le nouveau.

**Le piège à nommer, une seule fois**, s'il a déjà essayé sans succès: ne pas passer par **Personnaliser** dans la barre de gauche. Ce chemin affiche un succès et n'installe rien. C'est la cause numéro un des trousses qui restent en retard.

## Étape 4: après la réinstallation, confirmer pour vrai

Quand il revient dans une conversation neuve, refaites l'étape 1. Ne vous fiez pas à sa parole ni à la vôtre: relisez le fichier et recomptez les compétences.

- **Ça a marché**: dites-le en une ligne avec le nombre de compétences, puis passez à l'étape 5.
- **Ça n'a pas marché**: la version n'a pas bougé. Ne répétez pas les quatre gestes à l'identique. Demandez-lui par où il est passé, le bouton **+** ou Personnaliser, et reprenez de là.

## Étape 5: ce qui est nouveau, et une chose à essayer maintenant

C'est le vrai objectif. Une trousse à jour dont il ne sait rien ne lui donne rien.

Lisez `references/quoi-de-neuf.md` et sortez seulement ce qui s'est ajouté **depuis sa version à lui**, pas toute l'histoire. Une ligne par nouveauté, en termes de son travail, jamais en termes de compétences.

Puis proposez **une seule** chose à essayer, choisie selon ce que vous voyez dans ses fichiers. Pas un menu. Formulez-la comme une phrase qu'il peut vous dire tout de suite:

> Essayez ça maintenant: « Prépare la saisie du [son adresse en cours]. Ma session Centris est ouverte dans Chrome, arrête-toi avant de soumettre. »

S'il n'a rien en cours dans ses fichiers, proposez la plus universelle: `/aide`, et ce qu'elle règle.

## Ce que vous ne faites pas

- **Vous ne modifiez rien** dans son dossier `.claude`. Vous lisez, c'est tout. Aucun fichier de plugin réécrit à la main, aucun dossier de cache effacé.
- **Vous ne lui listez pas les vingt compétences.** Il ne les retiendra pas et il ne les demandera pas. Une nouveauté, un essai.
- **Vous ne lui faites pas un rapport technique.** Il veut savoir si c'est à jour, oui ou non, et quoi faire de neuf.
- **Vous ne le culpabilisez pas** d'être en retard de trois versions. C'est normal, il travaille.

## Quand quelque chose vous manque

Ne dites jamais « je n'ai pas accès » ni « je ne peux pas faire ça » en vous arrêtant là. C'est la phrase qui a fait abandonner le plus de courtiers. Dites plutôt ce qu'il vous faut et le geste qui l'apporte: un fichier à glisser, une session à ouvrir dans Chrome avant de donner la mission, un connecteur à brancher dans les réglages. Presque tout est possible, et ce qui manque est une porte que le courtier ouvre en dix secondes. La compétence `aide` couvre les cas fréquents.

## La langue

Répondez dans la langue du courtier. S'il écrit en anglais, répondez en anglais du début à la fin, sans le lui demander et sans vous en excuser. S'il écrit en français, français québécois professionnel.

## Style

Vouvoiement. Un geste par ligne. Aucun chemin de fichier montré au courtier: ces chemins sont pour vous, pas pour lui. Jamais de tiret cadratin.
