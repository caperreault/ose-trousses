---
name: activer-un-agent
description: >-
  Ajoute un coéquipier à l'équipe d'agents d'un courtier immobilier: sa charte, sa mémoire, sa liste de lecture, et son branchement à son assistant principal. À utiliser quand le courtier dit « monte-moi un agent », « ajoute quelqu'un à mon équipe », « je veux quelqu'un qui s'occupe de ça », « occupe-toi de ça pour de bon », « je refais la même chose chaque semaine », « quels agents je peux avoir », ou nomme une tâche qui revient. À utiliser aussi pour réviser un agent qui ne livre plus comme avant, ou pour en retirer un devenu inutile. Un poste à la fois, jamais toute l'équipe d'un coup.
---

# Activer un agent

Le courtier travailleur autonome fait le travail de huit personnes. Vous en installez un poste à la fois.

**Un poste à la fois, à son rythme.** Quand celui-là roule et qu'il est prêt pour le suivant, il vous le dira. Ne proposez jamais d'en monter deux dans la même conversation, et ne mettez aucune date sur le prochain. Celui qui installe toute l'équipe le mercredi soir débranche tout la semaine d'après.

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

Le `CLAUDE.md` de l'agent contient, dans cet ordre: son identité et son mandat en une phrase, sa frontière, sa liste de lecture, ses livrables, ses règles.

**La liste de lecture est la section la plus importante.** Écrivez où aller lire, jamais quoi lire:

```
Avant chaque tâche, lis :
- ../../CLAUDE.md
- ../../À propos de moi/a-propos-de-moi.md
- ../../À propos de moi/ma-voix.md
- ../../À propos de moi/mes-regles-decriture.md
- memoire/etat.md
- memoire/decisions.md
```

Ne listez que des fichiers qui existent vraiment. Un chemin mort fait lire l'agent dans le vide, en silence, à chaque conversation.

Ne recopiez jamais le contenu d'un fichier dans le CLAUDE.md de l'agent. Deux copies de la même information finissent toujours par se contredire.

## Étape 5: le brancher et le tester

Ajoutez une ligne dans le `CLAUDE.md` de la racine: le nom de l'agent, son mandat en une phrase, son chemin. C'est ce qui fait que l'assistant principal sait qu'il existe.

Remplissez ensuite sa ligne dans le registre de l'équipe: sans ça, l'associé ne saura pas quand lui passer la demande, et le poste restera muet. Le registre vit dans `AI_CONTEXT.md` si le courtier en a un, sinon dans le `CLAUDE.md` de la racine.

**Au quatrième poste seulement**, quand deux agents peuvent se disputer une même demande, sortez le routage fin dans `Mes agents/[Associé]/regles/carte-routage.md`: quelle demande va à qui, et quoi faire quand deux postes conviennent. Avant le quatrième, le registre suffit et un fichier de plus est du poids mort.

Vérifiez aussi que la section « Qui répond ici » du CLAUDE.md de la racine nomme bien l'associé du courtier comme porte d'entrée. Si elle manque, écrivez-la: c'est elle qui fait qu'une conversation ouverte dans le bureau tombe sur son équipe et non sur un assistant générique. La compétence `fondation` en donne le gabarit.

Puis proposez **un test tout de suite**, une vraie tâche, pas un test. « Demandez-lui son premier rapport. » Un agent qu'on ne teste pas le jour où on le monte ne sert jamais.

## Ce que cette compétence ne fait jamais

- Elle ne monte jamais deux agents dans la même conversation.
- Elle ne remplace ni ne double l'assistant principal du courtier.
- Elle ne supprime aucun agent sans confirmation explicite.
- Elle ne donne à un agent aucune permission d'envoi. Tous les agents préparent, le courtier envoie.
