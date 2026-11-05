# Monter la boucle de révision dans le bureau du courtier

Le courtier a dit « monte ma boucle », « installe mes gardiens » ou a lancé le raccourci `monter-ma-boucle`. Vous montez avec lui, dans SON bureau, la même boucle que celle de son coach : des gardiens qui bloquent avant l'écriture, deux vérificateurs qui relisent avant que ça sorte, et ses règles à lui au centre. Comptez dix minutes. Il voit chaque fichier changer : c'est ce qui lui apprend que son système est fait de fichiers qu'il contrôle.

Les fichiers à copier sont dans le dossier de cette compétence, sous `references/` : `gardiens/gardiens.pl`, `gardiens/hooks.json`, `agents/gardien-des-regles.md`, `agents/reviseur-a-froid.md`. Le dossier de la compétence est donné au chargement (« Base directory for this skill »).

## Étape 1 : le bon dossier

La conversation doit être ouverte sur son bureau : un `CLAUDE.md` et un dossier `À propos de moi` à la racine. Sinon, arrêtez et donnez le geste (sélecteur de dossier en haut, « Mon bureau IA »). Ne montez jamais une boucle ailleurs.

## Étape 2 : ses mots interdits, trouvés dans ce qu'il a déjà écrit

Ne lui demandez pas sa liste : il l'a déjà donnée, en classe et depuis. Elle est éparpillée dans ses fichiers. Lisez, en silence :

- `À propos de moi/mes-regles-decriture.md`, au complet;
- `À propos de moi/ma-voix.md`;
- la section « Mes règles permanentes » du `CLAUDE.md` de la racine;
- les règles du `CLAUDE.md` de chaque agent de `Mes agents/`, quel que soit le titre de leur section (« Règles », « Ce que je ne fais jamais »...).

Retenez un mot ou une expression **seulement si le courtier l'a lui-même marqué comme à ne jamais écrire** : il est entre guillemets ou en italique, et la même phrase dit « jamais », « ne pas écrire », « ne dis pas », « à éviter », « interdit » ou « bannir », avant ou après lui; ou il est à gauche d'une flèche ou d'un « plutôt » (« commission → rétribution »). Exemples : « Jamais "agent" pour un courtier » donne `agent`; « Je ne dis jamais "n'hésitez pas" » donne `n'hésitez pas`.

Ne retenez pas :
- une règle de style qui n'est pas un mot (« pas de jargon », « phrases courtes ») : elle reste pour le gardien des règles, qui la lit;
- un mot que vous trouvez maladroit dans ses exemples : vous ne bâtissez pas sa liste, vous la recopiez;
- le tiret long : un gardien le bloque déjà, il n'a pas besoin d'être dans la liste.

Gardez la forme la plus courte qui porte l'interdit, pour qu'elle attrape toutes ses variantes : « Ne jamais écrire "n'hésitez pas à me contacter" » s'inscrit `n'hésitez pas`, qui bloque aussi « n'hésitez pas à m'écrire ». Ne raccourcissez pas jusqu'à un mot ordinaire : « coup de cœur assuré » reste entier, parce que « coup de cœur » seul est permis.

Notez pour chaque mot le fichier d'où il vient et ce que le courtier écrit à la place, s'il l'a dit dans la même phrase ou la même ligne (« jamais "agent" pour un courtier » dit que le bon mot est courtier).

Deux cas à connaître :
- **Une règle limitée à un endroit** (« jamais "Au plaisir!" à la fin d'un courriel ») : le mot entre quand même dans la liste, et le gardien le bloquera partout dans ses livrables. Dites-le dans le message, il retire s'il préfère.
- **Une règle d'un seul agent** (« Julie n'écrit jamais "opportunité en or" ») : le mot entre dans la liste, qui vaut pour tout le bureau. Nommer l'agent comme source suffit pour qu'il retire si le mot n'est interdit que là.

Lisez aussi ses `Exemples/`, pour un seul but : si un exemple contient un mot de la liste, c'est une contradiction, et elle compte, parce que l'assistant copie la forme des exemples. Nommez-la en une ligne dans le message, avec les deux fichiers. C'est lui qui tranche : corriger l'exemple ou retirer le mot.

## Étape 3 : le plan, en un seul message, sans attendre

Dites en trois lignes ce que vous installez, puis la liste trouvée :

> Je monte votre boucle de révision. Trois choses : des gardiens qui bloquent un tiret long, un mot de passe ou un de vos mots interdits avant qu'il s'écrive; deux vérificateurs, un gardien des règles et un réviseur à froid, qui relisent tout ce qui part vers un client; et la règle dans votre bureau pour que votre associé s'en serve tout seul.
>
> Vos mots interdits, trouvés dans vos fichiers : « agent » (votre CLAUDE.md), « commission » (votre CLAUDE.md), « n'hésitez pas » (ma-voix.md). Un mot de trop? Dites « retire [mot] ». Un oubli? Dites « ajoute [mot] », maintenant ou n'importe quand.

S'il n'a pas encore d'associé, dites « votre assistant » au lieu de « votre associé ».

Puis continuez l'installation sans attendre de réponse : ces mots, c'est lui qui les a écrits. S'il répond pendant l'installation, appliquez.

**Rien trouvé du tout** (un bureau monté avant que ses règles soient remplies) : c'est le seul cas où vous posez la question, une seule fois, et vous attendez : « Quels mots ou expressions ne doivent jamais sortir de votre bureau? Par exemple "n'hésitez pas", "commission", "agent". »

## Étape 4 : la section Mots interdits

Dans `À propos de moi/mes-regles-decriture.md`, la section `## Mots interdits` existe ou se crée à la fin. C'est la seule que le gardien lit : les mots éparpillés ailleurs y sont rassemblés, sans être retirés de leur fichier d'origine. Une ligne par mot, en puce. Ce qui suit « : » est une explication que le gardien ignore, utile pour dire quoi écrire à la place :

```
## Mots interdits
- n'hésitez pas : je dis plutôt « appelez-moi »
- commission : rétribution
```

Ajoutez une ligne datée sous le titre : « Surveillés par les gardiens depuis le [date]. » Complétez, ne remplacez jamais une règle existante. Si une règle ailleurs dans le fichier dit le contraire d'un mot qu'il donne, nommez la contradiction : il tranche.

## Étape 5 : les gardiens

1. Créez `.claude/gardiens/` dans son bureau et copiez-y `gardiens.pl`. Une commande `cp` suffit, sur Mac comme sur PC.
2. Ouvrez `.claude/settings.json` du bureau. Absent : créez-le avec le contenu de `hooks.json`. Présent : ajoutez les trois entrées de `hooks.json` dans sa section `hooks`, `PreToolUse`, sans toucher au reste du fichier. Une entrée qui appelle déjà `gardiens.pl` ne se double pas.
3. Lancez le bulletin : `perl ".claude/gardiens/gardiens.pl" test "<chemin complet du bureau>"`. Montrez-lui les lignes OK.

**Si `perl` n'existe pas** (rare, un PC sans Git Bash) : dites-le simplement. Les gardiens ne peuvent pas tourner sur cet ordinateur, mais le reste de la boucle fonctionne. Continuez à l'étape 6 et notez-le au bulletin avec le geste : installer Git pour Windows (git-scm.com), puis redire « monte ma boucle ».

## Étape 6 : les deux vérificateurs

Copiez `agents/gardien-des-regles.md` et `agents/reviseur-a-froid.md` dans `.claude/agents/` du bureau. Ce ne sont pas des postes de son équipe : ils n'ont pas de mémoire et ne produisent rien. Ils vérifient.

## Étape 7 : la règle dans son bureau

Dans le `CLAUDE.md` de la racine, ajoutez cette section après « Mon équipe » (ou après « Qui répond ici »), si elle n'y est pas :

```
## Ma boucle de révision

Tout ce qui part vers un client, un collaborateur ou le public passe par la boucle avant de m'arriver : le gardien des règles vérifie les faits et mes règles, le réviseur à froid relit sans contexte, puis je signe. Compétence : boucle-de-revision. Pas pour une note interne ni un brouillon de travail.

Mes gardiens sont dans .claude/gardiens/. Une écriture bloquée, c'est le système qui fonctionne : corrige le texte et réécris. Ne contourne jamais un gardien par une commande.
```

S'il a un associé, ajoutez à la fin du mandat de son `CLAUDE.md` : « Avant de me remettre un livrable qui part vers l'extérieur, passe-le dans la boucle de révision. »

Dans `Mes agents/competences.md`, s'il existe, la ligne de la boucle devient : `| boucle-de-revision | Le gardien et le réviseur à froid avant que ça sorte, et vos corrections qui restent | « Passe ça dans la boucle » | Tous |`.

## Étape 8 : le bulletin

Court, dans cette forme :

> Votre boucle est montée.
> - Gardiens : [n] sur [n] au test, [n] mots interdits surveillés, trouvés dans vos fichiers.
> - Vérificateurs : gardien des règles et réviseur à froid.
> - Votre associé s'en sert tout seul pour ce qui part vers l'extérieur.
>
> **Ouvrez une nouvelle conversation** : les gardiens et les vérificateurs se chargent au démarrage. Puis dites « Teste ma boucle ».
>
> Enregistré : [chaque chemin changé]

## Ce que l'installation ne fait jamais

- Elle ne touche à rien d'autre dans `.claude/settings.json` que ses trois entrées.
- Elle n'invente pas de mots interdits : elle recopie ceux que le courtier a lui-même marqués, et le dit.
- Elle n'écrase aucune règle existante.
- Elle ne contourne jamais un gardien, même pendant l'installation.
