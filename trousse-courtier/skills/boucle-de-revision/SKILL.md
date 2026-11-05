---
name: boucle-de-revision
description: >-
  Monte et fait tourner la boucle de révision du courtier : des gardiens qui bloquent avant l'écriture (tiret long, mot de passe, ses mots interdits), un gardien des règles et un réviseur à froid qui vérifient un livrable avant qu'il lui arrive, et ses corrections qui descendent dans ses fichiers au lieu de mourir avec la conversation. À utiliser quand il dit « monte ma boucle », « installe mes gardiens », « teste ma boucle », « passe ça dans la boucle », « fais-moi vérifier ça », « passe-le au gardien », « relis ça à froid », « est-ce que ça respecte mes règles », « ce n'est pas comme ça que je le dis », « corrige ça pour de bon », « tu refais toujours la même erreur », « n'écris plus jamais ce mot », « retiens ça », ou quand il corrige la même chose une deuxième fois. À utiliser aussi avant de remettre au courtier un texte qui part vers un client, un collaborateur ou le public, et pour sa révision hebdomadaire.
---

# La boucle de révision

Deux idées : rien ne sort sans être vérifié, et rien de corrigé ne se reperd.

**L'agent produit. Le gardien des règles vérifie. Le réviseur à froid relit. Le courtier signe.** Si ça ne passe pas, ça retourne à l'agent. Rien ne sort de la boucle sans avoir passé les deux garde-fous.

## Partie 0 : monter la boucle

Quand le courtier dit « monte ma boucle », « installe mes gardiens » ou lance le raccourci `monter-ma-boucle` : suivez `references/installation.md`, étape par étape.

Pour savoir si la boucle est déjà montée : `.claude/gardiens/gardiens.pl` et `.claude/agents/reviseur-a-froid.md` existent dans son bureau. Si un texte doit passer la boucle et qu'elle n'est pas montée, faites la vérification quand même avec la méthode de secours (fin de la partie 1), puis proposez une fois : « Dites "monte ma boucle" et vos vérificateurs seront installés pour de bon, dix minutes. »

**Mise à jour des gardiens.** La ligne `# VERSION` en tête de `gardiens.pl` porte sa version. Si celle du bureau est plus ancienne que celle de `references/gardiens/gardiens.pl`, recopiez le fichier, relancez le test, et dites-le en une ligne.

## Partie 1 : faire passer un livrable

Sur tout ce qui sort vers un client, un collaborateur ou le public. Pas sur une note interne, pas sur un brouillon de travail. Une boucle qui tourne sur tout devient une boucle qu'on débranche.

### Tour 1 : le gardien des règles

Lancez l'agent `gardien-des-regles` avec l'outil Agent. Donnez-lui SEULEMENT :
- le livrable (son chemin dans `Résultats/`, ou son texte),
- à qui il est destiné,
- les documents d'où viennent ses faits (la promesse d'achat, la fiche, le rapport), s'il y en a,
- l'agent qui l'a produit, s'il y en a un.

Il répond PASSE ou RETOUR. Sur RETOUR, corrigez exactement ce qu'il liste (ou renvoyez à l'agent producteur), et relancez-le. Au troisième RETOUR, arrêtez la boucle : montrez au courtier ce qui bloque encore. Une donnée introuvable ne s'invente pas pour faire passer le gardien : elle se demande au courtier.

### Tour 2 : le réviseur à froid

Lancez l'agent `reviseur-a-froid` avec l'outil Agent. Donnez-lui SEULEMENT le texte qui a passé le gardien, à qui il est destiné et ce qu'il doit obtenir. Pas l'historique, pas les brouillons, pas vos intentions. S'il les connaît, il excuse les défauts : c'est tout l'intérêt qu'il ne les connaisse pas.

Il rend le texte corrigé. S'il a changé un chiffre, un nom ou une date, annulez ce changement : ce n'est pas son travail.

### Ce que le courtier reçoit

Le texte final, puis trois lignes au plus : ce que le gardien a vérifié, ce qu'il a fait corriger, ce que le réviseur a changé. Le courtier signe. Rien ne part sans lui.

### Méthode de secours

Si l'outil Agent n'est pas disponible ou si les vérificateurs ne sont pas montés : faites le tour du gardien vous-même avec la liste de `references/agents/gardien-des-regles.md`. Pour le réviseur, dites au courtier que relire dans la même conversation n'est pas une relecture à froid, et donnez-lui le geste : ouvrir une nouvelle conversation, coller seulement le texte, et écrire « Relis ça à froid. C'est pour [destinataire], il doit [but]. »

### Quand un gardien bloque une écriture

Le message commence par « BLOQUÉ par les gardiens du bureau ». Ce n'est pas une panne. Corrigez le texte comme il le dit et réécrivez. Ne passez jamais par une commande pour écrire quand même : c'est exactement le trou que les gardiens bouchent. Si le blocage vous paraît injustifié (le courtier cite un texte qui contient le mot, par exemple), dites-le au courtier et laissez-le trancher.

## Partie 2 : teste ma boucle

Quand il dit « teste ma boucle », une démonstration en trois minutes, dans cet ordre :

1. **Le gardien qui bloque.** Tentez d'écrire `Résultats/essai-boucle.md` avec une phrase qui contient un de ses mots interdits. Le gardien refuse : montrez-lui le message. Puis écrivez la phrase corrigée. « Votre règle est devenue un gardien. »
2. **Le gardien des règles qui attrape un chiffre.** Rédigez un court courriel à un vendeur qui cite un prix médian de son secteur, sans source. Passez-le au tour 1 : RETOUR, donnée sans source. Montrez-le.
3. **Le réviseur qui coupe.** Retirez le chiffre, passez le courriel au tour 2. Montrez ce qu'il a coupé.

Terminez par : « Votre associé fait ça tout seul, maintenant, avant de vous remettre un texte qui part vers l'extérieur. » Ne gardez pas `essai-boucle.md` sans lui demander.

## Partie 3 : la correction qui reste

Un courtier corrige son assistant dans la conversation. La conversation se ferme. La semaine d'après, il corrige la même chose. C'est là que les gens débranchent.

**La correction ne reste jamais dans la conversation. Elle descend dans un fichier.**

### La règle des deux corrections

Si le courtier corrige la même chose deux fois, ce n'est plus une correction. C'est une compétence qui attend. Dites-le-lui, et proposez de la monter.

### Où descend chaque correction

| Ce que le courtier corrige | Où ça descend |
|---|---|
| Un mot qu'il ne veut plus jamais voir | `À propos de moi/mes-regles-decriture.md`, section « Mots interdits » : le gardien le bloque dès l'écriture suivante |
| Un mot, un ton, une tournure | `À propos de moi/ma-voix.md` |
| Une règle d'écriture, un format | `À propos de moi/mes-regles-decriture.md` |
| Un fait sur sa pratique, son secteur, ses chiffres | `À propos de moi/a-propos-de-moi.md` |
| La façon de faire d'un poste précis | Le `CLAUDE.md` de cet agent |
| Une décision qu'il vient de prendre | `memoire/decisions.md` de l'agent, datée |
| L'état d'un dossier qui a changé | `memoire/etat.md` de l'agent |
| Une procédure complète qui revient | Une nouvelle compétence |

En cas d'hésitation entre la voix et un agent : si la correction vaut pour tout ce qu'il écrit, elle va dans la voix. Si elle vaut pour un seul poste, elle va chez l'agent.

Un mot interdit est la seule correction qui devient un gardien. Dites-le-lui quand ça arrive : « Je l'ai ajouté à vos mots interdits. À partir de maintenant, il ne peut plus s'écrire dans vos livrables. »

### Écrire une règle, pas une anecdote

« Ne pas écrire n'hésitez pas à me contacter » est une règle. « Il n'a pas aimé la fin du courriel de mardi » n'en est pas une.

Une bonne règle dit quoi faire et pas seulement quoi éviter, tient en une ou deux lignes, et se vérifie : quelqu'un d'autre pourrait dire si un texte la respecte.

Datez-la. Une règle datée peut être révisée, une règle sans date devient une loi que personne n'ose toucher.

**N'écrasez jamais une règle existante qui dit autre chose.** Nommez la contradiction au courtier, c'est lui qui tranche.

### Montrer le fichier changé

Dites QUEL fichier a changé et pourquoi, en une phrase. C'est ce qui apprend au courtier que son système est fait de fichiers qu'il contrôle, pas d'une mémoire magique.

## Partie 4 : la révision de la semaine

Quand le courtier demande où en est son équipe :

1. **Ce qui a été corrigé cette semaine**, et dans quels fichiers.
2. **Ce qui a été corrigé deux fois.** Ce sont ses prochaines compétences, ou ses prochains mots interdits. Nommez-les.
3. **Ce qui traîne dans `À décider.md`** depuis plus de sept jours.
4. **Les agents muets.** Un poste monté qui n'a rien produit depuis deux semaines est soit inutile, soit mal branché. Posez la question, ne tranchez pas.

Quatre points, quelques lignes chacun. Un rapport de révision qui prend dix minutes à lire ne sera pas lu la semaine suivante.

## Ce que cette compétence ne fait jamais

- Le gardien ne laisse jamais passer une donnée invérifiable en la qualifiant de mineure.
- Le réviseur à froid ne vérifie aucun chiffre et ne reçoit jamais la conversation.
- Elle ne contourne jamais un gardien, même pour un test.
- Elle n'écrase jamais une règle existante sans nommer la contradiction.
- Elle n'invente pas une règle ni un mot interdit à partir d'une seule remarque ambiguë.
- Elle ne juge jamais le travail d'un agent devant le courtier. Elle décrit ce qui a été corrigé, pas qui a échoué.

## Quand quelque chose te manque

Ne dis jamais « je n'ai pas accès » ni « je ne peux pas faire ça » en t'arrêtant là. C'est la phrase qui a fait abandonner le plus de courtiers. Dis plutôt ce qu'il te faut et le geste qui l'apporte : un fichier à glisser, une session à ouvrir dans Chrome avant de donner la mission, un connecteur à brancher dans les réglages. Presque tout est possible, et ce qui manque est une porte que le courtier ouvre en dix secondes. La compétence `aide` couvre les cas fréquents.

## La langue

Réponds dans la langue du courtier. S'il écrit en anglais, réponds en anglais du début à la fin, sans le lui demander et sans t'en excuser. S'il écrit en français, français québécois professionnel. Un livrable destiné à un client suit la langue de ce client, pas celle de la conversation.
