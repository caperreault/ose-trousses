---
name: activer-un-agent
description: >-
  Ajoute un coéquipier à l'équipe d'agents d'un courtier immobilier, ou monte toute l'équipe d'un coup: la charte de chaque agent, sa mémoire, sa liste de lecture, son branchement à l'associé, et le registre des compétences de la trousse rangées par agent. À utiliser quand le courtier dit « monte-moi un agent », « ajoute quelqu'un à mon équipe », « je veux quelqu'un qui s'occupe de ça », « occupe-toi de ça pour de bon », « je refais la même chose chaque semaine », « quels agents je peux avoir », ou nomme une tâche qui revient. À utiliser aussi quand il dit « monte toute mon équipe », « installe tous les agents », « active ma trousse », « range mes compétences », « qu'est-ce que ma trousse peut faire », ou juste après l'installation de la trousse. Aussi pour réviser un agent qui ne livre plus comme avant, ou pour en retirer un devenu inutile.
---

# Activer un agent

Le courtier travailleur autonome fait le travail de huit personnes. Deux façons de lui monter son équipe :

- **Il nomme une tâche ou un poste :** un poste, celui-là. Étapes 1 à 5.
- **Il demande toute l'équipe** (« monte toute mon équipe », « active ma trousse », la commande `/monter-mon-equipe`) : les cinq postes dans la même conversation, et ses compétences rangées. Section « Toute l'équipe d'un coup », plus bas.

Ne proposez pas d'en monter un deuxième quand il en a demandé un seul. Mais quand il demande toute l'équipe, faites-la au complet : c'est sa décision, et un courtier qui doit revenir cinq fois ne revient pas.

**Dans les deux cas, ses compétences sont rangées.** L'associé doit savoir ce que la trousse sait faire et à qui le passer. Sans le registre `Mes agents/competences.md`, il ignore la moitié de ce qui est installé.

## Étape 1: regarder ce qui existe déjà

Ouvrez `Mes agents/` dans son bureau. Notez qui est déjà là, en particulier son assistant principal, celui qu'il a bâti en formation. **Vous ne le remplacez jamais et vous ne le doublez pas.** Le nouveau poste travaille à côté de lui.

Si `Mes agents/` n'existe pas, créez-le. Si le bureau lui-même n'est pas monté, lancez d'abord la compétence `fondation`.

## Étape 2: choisir le poste

Cinq postes sont déjà écrits dans `references/postes-disponibles.md`. Lisez le fichier avant de proposer quoi que ce soit.

- **Le courtier nomme une tâche qui revient:** trouvez le poste qui la couvre, proposez-le, une seule recommandation.
- **Il ne sait pas par où commencer:** présentez les cinq en une ligne chacun et demandez lequel lui enlèverait le plus de poids cette semaine. Ne présentez pas un menu de quinze options.
- **Aucun poste ne correspond:** montez-lui un poste sur mesure avec la même structure. Les cinq modèles servent de patron, pas de limite.

## Étape 3: l'interview courte

Cinq questions, **une à la fois**, en reformulant chaque réponse en une phrase pour confirmer.

1. Quel prénom donnez-vous à cet agent? Un prénom, pas une fonction. Il devient un collègue.
2. Son mandat, en une phrase.
3. Sa frontière: qu'est-ce qu'il ne fait JAMAIS? Un agent sans frontière ne tient pas.
4. Ses livrables typiques.
5. Qu'est-ce qu'il doit toujours vous demander avant de faire?

Le modèle de poste répond déjà à la plupart de ces questions. Servez-vous-en pour proposer une réponse et faites confirmer, au lieu de faire remplir un formulaire vide.

## Étape 4: écrire le poste

Créez `Mes agents/[Prénom]/` avec:

```
Mes agents/[Prénom]/
├── CLAUDE.md          son mandat, 100 lignes maximum
└── memoire/
    ├── etat.md        l'état de ses dossiers en cours
    └── decisions.md   une ligne datée par décision du courtier
```

Le `CLAUDE.md` de l'agent contient, dans cet ordre: son identité et son mandat en une phrase, sa frontière, sa liste de lecture, ses livrables, ses règles, sa mémoire.

**La liste de lecture est la section la plus importante.** Écrivez où aller lire, jamais quoi lire:

```
Avant chaque tâche, lis :
- memoire/etat.md
- memoire/decisions.md
- ../../À propos de moi/a-propos-de-moi.md
Puis ce que demande la section « Quoi lire selon la tâche » du CLAUDE.md de la racine.
```

Ne listez que des fichiers qui existent vraiment. Un chemin mort fait lire l'agent dans le vide, en silence, à chaque conversation.

**La mémoire se tient toute seule ou elle ne se tient pas.** Écrivez cette section telle quelle à la fin de son CLAUDE.md :

```
## Ta mémoire

À la fin de chaque tâche : mets à jour memoire/etat.md, ajoute une ligne datée à memoire/decisions.md pour chaque décision que j'ai prise, et termine par « Enregistré : » avec les fichiers changés.
```

Sans elle, `etat.md` et `decisions.md` gardent leur première ligne pour toujours.

Ne recopiez jamais le contenu d'un fichier dans le CLAUDE.md de l'agent. Deux copies de la même information finissent toujours par se contredire.

## Étape 5: le brancher et le tester

Ajoutez sa ligne dans la section « Mon équipe » du `CLAUDE.md` de la racine : le poste, son prénom, son mandat en une phrase. C'est ce qui fait que l'associé sait qu'il existe et quand lui passer la demande; sans elle, le poste reste muet. Si le courtier a un `AI_CONTEXT.md`, le registre vit là. Une seule ligne, à un seul endroit.

**Au quatrième poste seulement**, quand deux agents peuvent se disputer une même demande, sortez le routage fin dans `Mes agents/[Associé]/regles/carte-routage.md`: quelle demande va à qui, et quoi faire quand deux postes conviennent. Avant le quatrième, le registre suffit et un fichier de plus est du poids mort.

Vérifiez aussi que la section « Qui répond ici » du CLAUDE.md de la racine nomme bien l'associé du courtier comme porte d'entrée. Si elle manque, écrivez-la: c'est elle qui fait qu'une conversation ouverte dans le bureau tombe sur son équipe et non sur un assistant générique. La compétence `fondation` en donne le gabarit.

Puis proposez **un test tout de suite**, une vraie tâche, pas un test. « Demandez-lui son premier rapport. » Un agent qu'on ne teste pas le jour où on le monte ne sert jamais.

Enfin, mettez à jour le registre des compétences (section suivante) : la colonne « Qui s'en sert » prend le prénom du nouveau poste.

## Le registre des compétences

Le fichier `Mes agents/competences.md` dit à l'associé ce que la trousse sait faire, la phrase qui le déclenche, et quel agent s'en sert. Écrivez-le ou mettez-le à jour chaque fois que cette compétence tourne.

1. Partez de `references/competences-de-la-trousse.md`. Ajoutez toute compétence de la trousse que vous voyez chez le courtier et qui n'y est pas (son nom commence par `trousse-courtier:`), retirez celles qui n'y sont plus.
2. Dans la colonne « Qui s'en sert », remplacez chaque poste par le prénom de l'agent qui l'occupe chez lui. Poste vide : le prénom de l'associé.
3. En tête du fichier, une ligne : « Les compétences de ma trousse OSE. Quand une demande correspond à une ligne, utilise la compétence, ou passe la demande à l'agent nommé. Mis à jour le [date], version [version] de la trousse. »
4. Dans le CLAUDE.md de la racine, ajoutez cette ligne au tableau « Quoi lire selon la tâche », si elle n'y est pas : `| peut se faire avec une compétence de ma trousse, ou demande ce que ma trousse sait faire | Mes agents/competences.md |`
5. Dans le CLAUDE.md de chaque agent, sa liste de lecture nomme déjà les compétences de son poste (« Ce qu'il lit en plus » des fiches). Vérifiez qu'elles y sont.

Ne recopiez jamais le contenu d'une compétence dans le registre. Une ligne par compétence : ce qu'elle fait, la phrase, qui.

## Toute l'équipe d'un coup

Quand le courtier demande toute l'équipe. Dans l'ordre, sans sauter d'étape.

1. **L'associé d'abord.** Regardez `Mes agents/` et la section « Qui répond ici » du CLAUDE.md de la racine. Pas d'associé : on le bâtit avant tout le reste, avec les cinq questions de l'étape 3, en lui donnant le rôle d'associé et de porte d'entrée. Les autres postes travaillent sous lui.
2. **Les compétences rangées.** Écrivez le registre (section précédente). C'est ce qui fait que son associé connaît sa trousse dès aujourd'hui.
3. **Les postes manquants.** Comparez `Mes agents/` aux cinq postes de `references/postes-disponibles.md`. Dites-lui lesquels manquent, en une ligne chacun, et demandez **en un seul message** le prénom de chacun. S'il répond « choisis pour moi », choisissez des prénoms courants au Québec, tous différents, aucun pareil à celui de l'associé ni à un nom de son profil, et continuez sans le relancer.
4. **Montez-les un par un, sans interview.** Pour chaque poste : la fiche répond au mandat, à la frontière et aux livrables. Adaptez à ce que dit son profil (son secteur, ses outils), sans poser de question. Écrivez le dossier complet du poste (étape 4) avant de passer au suivant : s'il ferme la conversation au milieu, les postes finis restent finis. Ne doublez aucun agent existant et ne touchez pas au mandat de l'associé.
5. **Branchez-les.** Une ligne par poste dans « Mon équipe ». Puis, comme l'équipe dépasse trois postes, écrivez `Mes agents/[Associé]/regles/carte-routage.md` : quelle demande va à qui, et quoi faire quand deux postes conviennent (l'associé tranche et le dit). Ajoutez à la liste de lecture de l'associé : « Pour savoir à qui passer une demande : regles/carte-routage.md ». Remplissez la colonne « Qui s'en sert » du registre avec les prénoms.
6. **Le bulletin.** Un tableau : prénom, poste, la phrase pour lui donner du travail. Puis **un seul** agent à faire travailler cette semaine, celui qui lui enlève le plus de poids d'après son profil, avec sa première mission en une phrase. Terminez par « Enregistré : » avec les chemins.

Ce qui reste une règle : chaque agent prépare, le courtier envoie. Aucun ne reçoit de permission d'envoi parce qu'il a été monté en lot.

## Ce que cette compétence ne fait jamais

- Elle ne monte pas un deuxième agent quand le courtier en a demandé un seul.
- Elle ne remplace ni ne double l'assistant principal du courtier.
- Elle ne supprime aucun agent sans confirmation explicite.
- Elle ne donne à un agent aucune permission d'envoi. Tous les agents préparent, le courtier envoie.

## Quand quelque chose vous manque

Ne dites jamais « je n'ai pas accès » ni « je ne peux pas faire ça » en vous arrêtant là. C'est la phrase qui a fait abandonner le plus de courtiers. Dites plutôt ce qu'il vous faut et le geste qui l'apporte: un fichier à glisser, une session à ouvrir dans Chrome avant de donner la mission, un connecteur à brancher dans les réglages. Presque tout est possible, et ce qui manque est une porte que le courtier ouvre en dix secondes. La compétence `aide` couvre les cas fréquents.

## La langue

Répondez dans la langue du courtier. S'il écrit en anglais, répondez en anglais du début à la fin, sans le lui demander et sans vous en excuser. S'il écrit en français, français québécois professionnel. Un livrable destiné à un client suit la langue de ce client, pas celle de la conversation.
