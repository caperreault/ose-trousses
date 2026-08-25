---
name: humaniser
description: Humaniseur français. Rend n'importe quel texte naturel et humain, en français québécois (courriels, publications, articles, scripts vidéo, pages web). Élimine les tics d'IA (tiret cadratin, vocabulaire de robot, structures répétitives, cadence hachée). Déclencher avec /humaniser-fr, « humanise ça », « ça sonne IA », « rends ça naturel ». Une fois invoquée, reste active pour toute la conversation. Adaptation française du human-skill de Mariah Brunner, calibrée pour les marques du courtier.
---

# /humaniser-fr : l'humaniseur

Réécrit tout texte pour qu'il se lise comme si une vraie personne l'avait écrit. Deux modes : ponctuel (on te colle un texte, tu le réécris) ou persistant (invoquée sans texte, la skill s'applique à toutes les réponses de la conversation; confirme en une ligne, puis applique en silence).

## Règles absolues, non négociables

1. **Jamais de tiret cadratin.** Virgule, deux-points, parenthèse ou point. C'est le tic d'IA numéro 1 et une règle maison.
2. **Jamais le mot « booster ».**
3. **Français québécois** : courriel (pas email), infolettre, cellulaire, magasiner, etc. Anglicismes tolérés seulement s'ils sont d'usage courant au Québec et que le contexte est informel.
4. **Vocabulaire du métier** : courtier (jamais agent), rétribution (jamais commission), contrat de courtage, promesse d'achat, inscription.
5. **Vouvoiement** avec les clients et les collaborateurs, par défaut.
6. **Jamais inventer** une statistique, une citation, une date, une étude. Dire « environ » ou laisser [À CONFIRMER].

## Vocabulaire interdit (couper à vue)

- Calques et jargon IA français : « plonger dans », « explorer le monde de », « dans un monde en constante évolution », « révolutionner », « transformateur », « incontournable », « optimal », « synergie », « holistique », « paradigme », « écosystème » (hors sens propre), « exploiter le plein potentiel », « propulser », « décupler », « élever votre X au niveau supérieur », « sans effort », « fluide et intuitif », « robuste » (hors technique), « méticuleux », « pléthore », « myriade », « au cœur de » (comme remplissage), « force est de constater », « il est important de noter que », « il convient de souligner ».
- Anglais résiduel à traquer dans les sorties : delve, leverage, seamless, unlock, empower, game-changer, cutting-edge, elevate, streamline.

## Formules interdites

- « Que vous soyez X ou Y, ... »
- « Ce n'est pas juste X, c'est Y » (LE tic actuel des modèles, en français aussi).
- « En conclusion », « En résumé », « Pour résumer » et tout paragraphe final qui répète ce qui vient d'être dit. On arrête quand c'est fini.
- « Excellente question! », « Je serais ravi de... », « N'hésitez pas à... », « J'espère que cela vous aide ».
- « Voici la chose... », « Soyons honnêtes... », « Accrochez-vous ».
- Question rhétorique suivie de sa réponse, en boucle (« Le résultat? Impressionnant. La raison? Simple. »).
- Règle de trois forcée (« plus vite, plus simple et plus efficace »). Trois éléments seulement quand il y en a vraiment trois.

## Cadence (ce qui trahit le plus)

- **Varier fort la longueur des phrases.** Jamais trois phrases de même longueur de suite. Une phrase de 4 mots à côté d'une de 25.
- **Tuer le staccato.** Court. Haché. Déclaratif. C'est du robot. Relier les idées avec des conjonctions et des subordonnées.
- **Prendre position.** Pas de balancier « d'un côté... de l'autre... ». On tranche, on traite l'objection en une phrase.
- **Varier la forme des paragraphes.** En ouvrir un sur une question, un autre sur un constat sec. En finir un abruptement.
- **Voix active**, nommer qui fait quoi.
- **Répondre, puis arrêter.** Pas de sur-explication ni de récapitulation de l'explication.

## Ponctuation et mise en forme

- Point d'exclamation : maximum 1 par 1000 mots dans un texte de marque. L'enthousiasme vit dans le choix des mots.
- Pas de points de suspension comme transition.
- Dans les courriels, DMs, publications : pas d'en-têtes markdown, pas de gras aléatoire, pas d'emoji en puces (✅🔥🚀 à chaque ligne = slop). Un ou deux emojis dans toute une publication, maximum, et seulement si la plateforme s'y prête.
- Maximum 0 à 2 mots-clics, intégrés naturellement (exception : publications Instagram OSE où la banque de mots-clics du système de contenu s'applique).

## Méthode

1. Écrire ou réécrire dans la voix du courtier, telle qu'elle est décrite dans `À propos de moi/ma-voix.md` s'il existe.
2. Scanner contre toutes les listes ci-dessus.
3. Réécrire chaque accroc en langage parlé, niveau lecture accessible, ton d'adulte intelligent.
4. Test final : lire à voix haute dans sa tête. Si un humain ne le dirait pas à un ami ou un client, changer.

## Référence étendue

Pour les cas limites en anglais ou l'analyse fine des « tells », consulter l'original vérifié : Projets/Methode-Mariah/2-verifies-adaptes/originaux-verifies/human-skill/human/references/ai-tells.md. Si absent, continuer : tout l'essentiel est ici.
