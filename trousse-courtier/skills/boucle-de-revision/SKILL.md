---
name: boucle-de-revision
description: >-
  Fait passer un livrable par deux garde-fous avant qu'il arrive au courtier, et fait descendre ses corrections dans les fichiers au lieu de les laisser mourir avec la conversation. À utiliser quand il dit « fais-moi vérifier ça », « passe-le au gardien », « relis ça à froid », « est-ce que ça respecte mes règles », « ce n'est pas comme ça que je le dis », « corrige ça pour de bon », « tu refais toujours la même erreur », « retiens ça », ou quand il corrige la même chose une deuxième fois. À utiliser aussi pour sa révision hebdomadaire: ce qui a été corrigé, ce qui devrait devenir une compétence.
---

# La boucle de révision

Deux mécanismes, une même idée: rien ne sort sans être vérifié, et rien de corrigé ne se reperd.

## Partie 1: la boucle de production

**L'agent produit. Le gardien des règles vérifie. Le réviseur à froid relit. Le courtier signe.**

Si ça ne passe pas, ça retourne à l'agent. Rien ne sort de la boucle sans avoir passé les deux garde-fous.

### Le gardien des règles

Il vérifie la **conformité et les données**. Il ne juge pas le style. Sa liste, dans cet ordre:

1. **Les chiffres.** Chaque donnée de marché, prix, statistique ou date est-elle vérifiable à la source? Une donnée sans source se signale, elle ne se corrige pas toute seule. L'IA produit des chiffres plausibles et faux avec le même aplomb.
2. **Les dates.** Correspondent-elles au document d'origine, pas à un souvenir.
3. **Les règles du courtier.** Ce qui est écrit dans `À propos de moi/mes-regles-decriture.md` est-il respecté? Les mots interdits sont-ils absents?
4. **Les obligations du métier.** Aucun avis juridique, fiscal ou réglementaire présenté comme un avis. Aucun critère discriminatoire dans une fiche, une annonce ou un message. Aucun renseignement sensible.
5. **La frontière de l'agent.** A-t-il produit quelque chose qui n'est pas son mandat?

Sortie: **PASSE** ou **RETOUR**, avec la liste exacte de ce qui bloque. Jamais un « c'est bon dans l'ensemble ».

### Le réviseur à froid

Il relit **sans contexte**, comme si le texte arrivait d'un inconnu. C'est tout l'intérêt: celui qui a écrit ne voit plus ce qui manque.

Il ne vérifie aucune donnée. Il répond à quatre questions:

1. Est-ce que ça se comprend du premier coup, sans relire une phrase?
2. Est-ce que ça sonne comme une personne, ou comme une machine?
3. Qu'est-ce qui manque pour que le destinataire sache quoi faire ensuite?
4. Qu'est-ce qu'on peut couper sans rien perdre?

Sortie: le texte corrigé, plus une ligne sur ce qui a été changé et pourquoi.

### Quand la lancer

Sur tout ce qui sort vers un client, un collaborateur ou le public. Pas sur une note interne, pas sur un brouillon de travail. Une boucle qui tourne sur tout devient une boucle qu'on débranche.

## Partie 2: la correction qui reste

Un courtier corrige son assistant dans la conversation. La conversation se ferme. La semaine d'après, il corrige la même chose. C'est là que les gens débranchent.

**La correction ne reste jamais dans la conversation. Elle descend dans un fichier.**

### La règle des deux corrections

Si le courtier corrige la même chose deux fois, ce n'est plus une correction. C'est une compétence qui attend. Dites-le-lui, et proposez de la monter.

### Où descend chaque correction

| Ce que le courtier corrige | Où ça descend |
|---|---|
| Un mot, un ton, une tournure | `À propos de moi/ma-voix.md` |
| Une règle d'écriture, un mot interdit, un format | `À propos de moi/mes-regles-decriture.md` |
| Un fait sur sa pratique, son secteur, ses chiffres | `À propos de moi/a-propos-de-moi.md` |
| La façon de faire d'un poste précis | Le `CLAUDE.md` de cet agent |
| Une décision qu'il vient de prendre | `memoire/decisions.md` de l'agent, datée |
| L'état d'un dossier qui a changé | `memoire/etat.md` de l'agent |
| Une procédure complète qui revient | Une nouvelle compétence |

En cas d'hésitation entre la voix et un agent: si la correction vaut pour tout ce qu'il écrit, elle va dans la voix. Si elle vaut pour un seul poste, elle va chez l'agent.

### Écrire une règle, pas une anecdote

« Ne pas écrire n'hésitez pas à me contacter » est une règle. « Il n'a pas aimé la fin du courriel de mardi » n'en est pas une.

Une bonne règle dit quoi faire et pas seulement quoi éviter, tient en une ou deux lignes, et se vérifie: quelqu'un d'autre pourrait dire si un texte la respecte.

Datez-la. Une règle datée peut être révisée, une règle sans date devient une loi que personne n'ose toucher.

**N'écrasez jamais une règle existante qui dit autre chose.** Nommez la contradiction au courtier, c'est lui qui tranche.

### Montrer le fichier changé

Dites QUEL fichier a changé et pourquoi, en une phrase. C'est ce qui apprend au courtier que son système est fait de fichiers qu'il contrôle, pas d'une mémoire magique.

## Partie 3: la révision de la semaine

Quand le courtier demande où en est son équipe:

1. **Ce qui a été corrigé cette semaine**, et dans quels fichiers.
2. **Ce qui a été corrigé deux fois.** Ce sont ses prochaines compétences. Nommez-les.
3. **Ce qui traîne dans `À décider.md`** depuis plus de sept jours.
4. **Les agents muets.** Un poste monté qui n'a rien produit depuis deux semaines est soit inutile, soit mal branché. Posez la question, ne tranchez pas.

Quatre points, quelques lignes chacun. Un rapport de révision qui prend dix minutes à lire ne sera pas lu la semaine suivante.

## Ce que cette compétence ne fait jamais

- Le gardien ne laisse jamais passer une donnée invérifiable en la qualifiant de mineure.
- Le réviseur à froid ne vérifie aucun chiffre: ce n'est pas son travail, et croire qu'il le fait est le meilleur moyen de laisser passer une erreur.
- Elle n'écrase jamais une règle existante sans nommer la contradiction.
- Elle n'invente pas une règle à partir d'une seule remarque ambiguë.
- Elle ne juge jamais le travail d'un agent devant le courtier. Elle décrit ce qui a été corrigé, pas qui a échoué.
