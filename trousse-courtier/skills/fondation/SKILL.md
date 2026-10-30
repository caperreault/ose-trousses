---
name: fondation
description: >-
  Vérifie, répare et complète le bureau IA d'un courtier immobilier contre la fondation enseignée à L'École de l'IA: le CLAUDE.md de la racine et ses sections, les fichiers d'À propos de moi, les Exemples, l'associé et sa mémoire, le registre de l'équipe, le calendrier IA et la routine du matin. Retrouve dans les conversations passées les réponses déjà données au lieu de faire recommencer le courtier. Termine par un bulletin court, chaque point à faire avec la phrase exacte à dire. À utiliser quand le courtier dit « vérifie mon bureau », « vérifie ma fondation », « est-ce que mon bureau est bien monté », « répare mon bureau IA », « mon assistant ne se souvient de rien », « on commence le Jour 2 », « je viens d'installer la trousse », ou au tout premier passage après l'installation de la trousse OSE. À utiliser aussi quand un assistant semble ignorer le contexte du courtier alors que les fichiers existent.
---

# La fondation : le vérificateur du bureau

Vous vérifiez le bureau IA d'un courtier immobilier du Québec contre la fondation enseignée à L'École de l'IA, et vous réparez ce qui manque. C'est la première compétence qui tourne après l'installation de la trousse, et elle ouvre le Jour 2 pour tout le monde.

**Ce courtier sort d'une formation. Il n'a pas envie d'un diagnostic technique.** Il veut savoir que son affaire est solide. Travaillez en silence, réparez, et livrez un bulletin court à la fin.

Trois cas se présentent, souvent dans la même salle : le bureau est complet, le bureau est à moitié monté, le bureau a des fichiers vides. Vous gérez les trois sans jamais faire sentir au courtier qu'il est en retard sur son voisin. **Et vous ne le faites jamais recommencer ce qu'il a déjà fait** : ses réponses sont souvent dans ses conversations passées (étape 4).

La référence est `references/CLAUDE-fondation.md` : le CLAUDE.md exact que la page des commandes fait écrire au Jour 1. Lisez-le avant de commencer.

## Étape 1 : le bon dossier

Regardez le dossier ouvert dans la conversation.

- Il s'appelle « Mon bureau IA » ou l'équivalent chez ce courtier : continuez.
- Il porte un autre nom et ne contient ni `CLAUDE.md` ni « À propos de moi » : **arrêtez tout de suite.** Dites au courtier que la conversation n'est pas ouverte sur son bureau, et expliquez le geste : cliquer le sélecteur de dossier en haut, choisir « Mon bureau IA » dans les dossiers récents. Ne créez jamais un deuxième bureau par-dessus le premier.

## Étape 2 : l'inventaire, en silence

Faites le tour et notez, pour la grille du bulletin :

| Ce que vous vérifiez | Ce qui compte comme bon |
|---|---|
| `CLAUDE.md` à la racine | Il a les sections du gabarit : Qui je suis, Qui répond ici, Comment ce bureau est organisé, Quoi lire selon la tâche, Tenir mes fichiers à jour, Mes règles permanentes |
| « Qui je suis » | Trois vraies lignes, pas « Profil à remplir » |
| `À propos de moi/` | Les quatre fichiers existent et sont remplis : a-propos-de-moi.md, mon-secteur-chiffres.md, mes-regles-decriture.md, ma-voix.md |
| `Exemples/` | Au moins un vrai texte du courtier |
| `Résultats/`, `Projets/` | Présents |
| L'associé | Un dossier dans `Mes agents/`, nommé dans « Qui répond ici » |
| La mémoire de chaque agent | Son CLAUDE.md a la section « Ta mémoire », et `memoire/decisions.md` a au moins une ligne datée |
| La liste de lecture de chaque agent | Chaque chemin pointe vers un fichier qui existe |
| « Mon équipe » | Une ligne par agent qui existe vraiment, aucune de plus |
| `À décider.md` | Présent à la racine |
| Le calendrier IA | Son nom est écrit dans le CLAUDE.md |
| La routine du matin | `Projets/ma-routine-du-matin.md` existe |

Un fichier de moins de 200 caractères, ou qui ne contient que des titres, des crochets ou « à remplir », compte comme vide.

## Étape 3 : le CLAUDE.md de la racine, contre le gabarit

C'est le coeur du travail. Ce fichier est lu au début de chaque conversation. Sans lui, chaque conversation repart de zéro.

- **Il n'existe pas :** écrivez le gabarit tel quel.
- **Il existe :** ne l'écrasez jamais. Ajoutez, mot pour mot depuis le gabarit, chaque section qui manque. Gardez intact tout ce que le courtier ou son assistant a déjà écrit. Corrigez les chemins morts.
- **Un bureau bâti avant octobre 2026** a souvent un CLAUDE.md qui n'est qu'une table des matières, avec la règle « tu écris dans Résultats, et seulement là ». Remplacez cette seule phrase par la règle du gabarit : Résultats reçoit les livrables, À propos de moi, Exemples, la mémoire des agents et le CLAUDE.md sont la mémoire du courtier et se tiennent à jour. C'est cette phrase qui empêchait les conversations de s'enregistrer.

### Qui répond ici

S'il existe un associé dans `Mes agents/` (l'agent bâti avec le gabarit Bâtisseur d'agent, en général le seul ou le premier), la section doit le nommer :

```
## Qui répond ici

[Prénom] est la porte d'entrée de ce bureau. Toute conversation ouverte ici est une conversation avec lui : son mandat, son ton et ses règles s'appliquent dès le premier message. Avant de répondre, lis « Mes agents/[Prénom]/CLAUDE.md », puis sa mémoire. Il délègue aux autres agents de l'équipe quand la demande est leur métier, et il révise leur travail avant de me le remettre. Au premier message de chaque conversation, il se présente par son prénom.
```

Sans associé, laissez la ligne du gabarit (« Aucun associé encore ») et notez-le au bulletin. Ne recopiez jamais le contenu du CLAUDE.md de l'associé dans celui de la racine : vous écrivez où aller lire.

### Mon équipe

Une section « Mon équipe », juste après « Qui répond ici », avec un tableau Poste, Qui, Ce qu'il fait. Une ligne par agent qui existe vraiment dans `Mes agents/`. Un poste non monté ne s'écrit pas, et vous ne proposez pas d'en monter un : c'est la compétence `activer-un-agent`, quand le courtier le demande (un poste, ou toute l'équipe avec « monte toute mon équipe »).

Si le courtier a un `AI_CONTEXT.md`, le registre de l'équipe vit là, pas dans le CLAUDE.md. Ne le dupliquez pas.

**Le routage fin ne va pas là.** À partir du quatrième poste seulement, quand deux agents peuvent se disputer une demande, le détail sort dans `Mes agents/[Associé]/regles/carte-routage.md`. C'est `activer-un-agent` qui le crée à ce moment-là.

## Étape 4 : un fichier vide ? Cherchez d'abord dans ses conversations

Le courtier a souvent fait ses interviews en classe, mais les réponses ne se sont pas rendues dans les fichiers. Elles sont presque toujours encore sur son ordinateur. Avant de déclarer un fichier vide, allez les chercher.

**Demandez d'abord, une seule fois :** « Votre profil semble vide, mais vous avez probablement déjà répondu à ces questions en classe. Je peux relire vos conversations passées sur cet ordinateur pour récupérer vos réponses. D'accord? »

Sur son oui :

1. **Où elles sont.** Claude Code garde chaque conversation dans un fichier, sous le dossier caché `.claude/projects/` du dossier personnel : `~/.claude/projects/` sur Mac, `%USERPROFILE%\.claude\projects\` sur PC. Il y a un sous-dossier par dossier de travail, nommé d'après son chemin, chaque séparateur et chaque espace remplacé par un tiret (par exemple `-Users-marc-Desktop-Mon-bureau-IA`).
2. **Lesquelles lire.** Une conversation reste rangée sous le dossier où elle a COMMENCÉ, même si elle a été déplacée ensuite dans « Mon bureau IA ». En classe, la première conversation commence dans Documents : son historique est donc sous `-Users-<nom>-Documents`, pas sous « Mon bureau IA ». Lisez dans cet ordre : le sous-dossier de Documents, celui de « Mon bureau IA », puis tous les autres sous-dossiers modifiés depuis la formation (conversations ouvertes par erreur dans le mauvais dossier). Gardez celles qui parlent de son bureau : on y voit « Mon bureau IA », « À propos de moi » ou le nom de son associé.
3. **Comment les lire.** Chaque conversation est un fichier `.jsonl`, une ligne par message. Les lignes `"type":"user"` portent ce que le courtier a écrit; les lignes `"type":"assistant"` portent les questions posées. Reliez chaque réponse à sa question.
4. **Ce que vous en tirez.** Seulement ce qui va dans son profil : son rôle, son territoire, ses buts, son client idéal, son équipe, ses outils, sa façon de travailler, ses mots interdits, sa voix, et l'interview de son associé. **Aucune donnée de client** n'entre dans le profil, même si la conversation en contient.
5. **Écrivez** chaque réponse dans le bon fichier, comme le ferait la commande d'interview, sans rien inventer pour combler un trou. Ce qui manque reste à demander.
6. **Montrez-lui** ce que vous avez récupéré, fichier par fichier, et faites valider. Il corrige, vous appliquez dans le fichier.

Rien trouvé ? Claude Code efface ses vieilles conversations après environ 30 jours. Dites-le simplement, sans en faire un drame : « Vos conversations d'avant ne sont plus sur l'ordinateur. Dites "continue mon profil" et on le remplit ensemble, ça prend vingt minutes. »

## Étape 5 : Exemples et voix, à partir de ses courriels envoyés

Si `Exemples/` est vide, ou si `ma-voix.md` dit « À enrichir avec mes courriels envoyés », regardez si son courriel est branché (le devoir de la semaine du Jour 1).

- **Branché :** proposez-le. « Je peux lire vos courriels envoyés des six derniers mois pour trouver vos meilleurs textes et compléter votre voix. D'accord? » Sur son oui, lisez ses envoyés. Gardez seulement ce qu'il a écrit lui-même : ni les envois automatiques, ni les transferts, ni les réponses d'une ligne. Rangez un bon courriel de suivi dans `Exemples/courriel-suivi.md`, une lettre ou présentation dans `Exemples/lettre-presentation.md`, et un texte délicat (mauvaise nouvelle, refus, négociation) s'il y en a un. Remplacez les noms de clients par [client] : un exemple sert à copier la forme. Puis complétez `ma-voix.md` avec ce que vous observez (longueur des phrases, vouvoiement ou tutoiement, ouverture, fermeture, expressions qui reviennent) et retirez la ligne « À enrichir ».
- **Pas branché :** notez-le au bulletin avec le geste : dans l'application Claude, Personnaliser, puis Connecteurs, puis le +.

## Étape 6 : les agents, leur mémoire et leur liste de lecture

Pour chaque agent de `Mes agents/` :

- **Sa mémoire se tient.** Son CLAUDE.md doit avoir une section « Ta mémoire ». Si elle manque, ajoutez-la telle quelle :

  ```
  ## Ta mémoire

  À la fin de chaque tâche : mets à jour memoire/etat.md, ajoute une ligne datée à memoire/decisions.md pour chaque décision que j'ai prise, et termine par « Enregistré : » avec les fichiers changés.
  ```

  Sans elle, `etat.md` et `decisions.md` gardent leur première ligne pour toujours. C'est le bris le plus fréquent des bureaux d'août et de septembre 2026.
- **Sa liste de lecture pointe vers du vrai.** Le défaut classique : la liste nomme `../../À propos de moi/ma-voix.md` alors que le fichier n'a jamais été créé. L'agent ne plante pas, il lit dans le vide à chaque conversation. Pour chaque chemin mort, corrigez-le si le fichier existe sous un autre nom, sinon retirez la ligne et notez-le au bulletin.
- **Sa règle d'écriture ne bloque pas sa mémoire.** Une règle « aucune écriture ailleurs que dans Résultats et memoire/ » doit permettre aussi d'écrire dans À propos de moi ce que l'agent apprend sur le courtier. Ajustez la phrase.

- **Ses compétences sont rangées.** Si `Mes agents/competences.md` n'existe pas, ou s'il date d'une version plus ancienne de la trousse, notez-le au bulletin avec la phrase : « Dites "range mes compétences" ». Si son équipe compte seulement l'associé, ajoutez : « Dites "monte toute mon équipe" : les cinq postes de la trousse se montent dans la même conversation. » Ne les montez pas vous-même : c'est `activer-un-agent`, sur son oui.

## Étape 7 : À décider.md

S'il n'existe pas à la racine, créez-le, avec cette seule ligne : « Ce qui attend ma décision. Une ligne datée par item, je raye ce qui est réglé. » C'est la seule pile que le courtier a besoin de regarder pour savoir ce qui l'attend.

## Étape 8 : le calendrier IA

Si le CLAUDE.md ne nomme pas de calendrier IA, demandez au courtier s'il en a un séparé pour son assistant. La plupart n'en ont pas.

Expliquez-lui pourquoi en une phrase : **votre assistant n'écrit jamais dans votre vrai agenda.** Il dépose ce qu'il trouve dans un calendrier à part, et vous glissez vous-même dans le vôtre ce qui est bon.

Donnez-lui le geste selon son outil, une seule fois, sans faire un cours :

- **Calendrier Apple :** menu Fichier, Nouveau calendrier, nommez-le `IA`.
- **Google Agenda :** dans la colonne de gauche, le plus à côté de « Autres agendas », Créer un agenda, nommez-le `IA`.
- **Outlook :** onglet Calendrier, Ajouter un calendrier, Créer un calendrier vierge, nommez-le `IA`.

Quand c'est fait, ajoutez une ligne dans « Mes règles permanentes » du CLAUDE.md : « Mon calendrier IA s'appelle [nom]. Tu n'écris jamais dans mon vrai agenda. » Toutes les autres compétences le liront là.

## Étape 9 : la routine du matin

Si `Projets/ma-routine-du-matin.md` n'existe pas, écrivez-le avec la commande de son brief quotidien, et dites-lui comment la lancer. Ne la lancez pas maintenant : ses connexions ne sont peut-être pas branchées, et un brief vide au premier essai fait mauvaise impression.

## Étape 10 : le bulletin

Court. Une grille, puis une ligne :

```
Votre bureau

✓ Fondation (CLAUDE.md)            ✓ Associé : Marc, mémoire active
✓ Profil                           ✗ Voix : à compléter
✗ Exemples : vide                  ✗ Équipe : 1 poste sur 6
✓ Calendrier IA                    ✓ Routine du matin
✗ Compétences rangées
```

Sous la grille :

1. **Ce que j'ai réparé ou récupéré**, en une ligne. Nommez ce qui vient de ses conversations passées : c'est la bonne nouvelle de la journée.
2. **Pour chaque ✗, la phrase exacte à dire.** Par exemple : « Dites "continue ma voix" », ou « Branchez votre courriel (Personnaliser, Connecteurs, +), puis dites "vérifie mon bureau" ».
3. **Un test immédiat.** Une chose à essayer dans la minute : « Demandez-moi un courriel de suivi pour votre dernier acheteur. Vous allez voir la différence maintenant que je vous connais. »

Ne livrez jamais une liste de fichiers créés. Livrez un bureau qui fonctionne. Terminez par « Enregistré : » avec les chemins changés.

## Ce que cette compétence ne fait jamais

- Elle ne crée jamais un deuxième bureau par-dessus un bureau existant.
- Elle n'écrase jamais un fichier rempli. Elle complète.
- Elle ne supprime rien.
- Elle ne lit ni les conversations passées ni les courriels sans le oui du courtier.
- Elle ne met aucune donnée de client dans le profil.
- Elle n'invente jamais ce que lui seul sait : sa voix, son secteur, ses chiffres. Ce qu'elle ne retrouve pas, elle le lui demande.
- Elle ne monte aucun agent. C'est `activer-un-agent`, quand le courtier le demande.

## Quand quelque chose vous manque

Ne dites jamais « je n'ai pas accès » ni « je ne peux pas faire ça » en vous arrêtant là. C'est la phrase qui a fait abandonner le plus de courtiers. Dites plutôt ce qu'il vous faut et le geste qui l'apporte : un fichier à glisser, une session à ouvrir dans Chrome avant de donner la mission, un connecteur à brancher dans les réglages. Presque tout est possible, et ce qui manque est une porte que le courtier ouvre en dix secondes. La compétence `aide` couvre les cas fréquents.

## La langue

Répondez dans la langue du courtier. S'il écrit en anglais, répondez en anglais du début à la fin, sans le lui demander et sans vous en excuser. S'il écrit en français, français québécois professionnel. Un livrable destiné à un client suit la langue de ce client, pas celle de la conversation.
