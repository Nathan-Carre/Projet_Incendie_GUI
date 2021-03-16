# Projet d'informatique en Python du second semestre. 

## Contexte
L'objectif de ce projet est de mettre en place une solution permettant de simuler la propagation d'un incendie sur un terrain de 2500 parcelles. Chacune de ces parcelles à un état initial parmis les suivants :

- Eau
- Forêt
- Prairie

L'état d'une parcelle peut évoluer selon l'état des parcelles l'avoisinant. L'evolution des parcelles suit les règles suivantes : 

- une parcelle d’eau reste une parcelle d’eau durant toute la simulation;
- une parcelle qui devient en feu reste en feu durant la durée DUREE_FEU avant de devenir des cendres tièdes pendant la durée DUREE_CENDRE et enfin devenir des cendres éteintes durant le reste de la simulation; les valeurs de ces deux constantes sont à définir et laissées à votre appréciation;
- une parcelle de prairie prend feu dès qu’une des 4 cases voisines (gauche, droite, haut, bas) est en feu;
- une parcelle de forêt prend feu avec la probabilité 0.1 × nf où nf est le nombre de ses voisins en feu;

On considère que les bords du terrain ne peuvent pas brûler et qu’ils n’interviennent pas dans la propagation du feu.

## Solution
La solution mise en place est dôté d'une interface graphique permettant à l'utilisateur de générer aléatoirement un terrain de 2500 parcelles, de le manipuler, de simuler la propagation d'un incendie et de sauvegarder son état.

![alt texte](https://github.com/Nathan-Carre/projet_incendie/blob/main/ressources/Capture01.PNG)

### 1 - Générer un terrain 

Le boutton "Générer un nouveau terrain" comme son nom l'indique permet de générer un terrain de façon aléatoire. Celui-ci sera composé d'un nombre aléatoire de parcelles d'eau, de forêt et de prairie, représenté respectivement par les couleurs bleu, vert et jaune.

![alt texte](https://github.com/Nathan-Carre/projet_incendie/blob/main/ressources/Capture02.PNG)


### 2 - Première flamme 

Une fois le terrain généré l'utilisateur peux selectionner une parcelle parmis les parcelles de forêt et de prairie disponible afin de l'enflamer. Cette selection se fait d'un simple click sur la parcelle en question, qui sera par la suite représenté par la couleur rouge.

![alt texte](https://github.com/Nathan-Carre/projet_incendie/blob/main/ressources/Capture03.PNG)

### 3 - Effectuer une étape de simulation

Afin de pouvoir visualiser la propagation de l'incendie, il est possible d'effectuer manuellement une étape de la simulation. Pour ce faire l'utilisateur peut utiliser le bouton "Simuler (1 étape)".

![alt texte](https://github.com/Nathan-Carre/projet_incendie/blob/main/ressources/Capture04.PNG)


### 3 - Simulation Automatique

Tout comme la simulation manuelle, il est possible d'activer la simulation automatique. Celle-ci permet d'effectuer automatiquement 10 étape de simulation par seconde. Pour ce faire l'utilisateur peut utiliser le bouton "Simulation automatique".

![alt texte](https://github.com/Nathan-Carre/projet_incendie/blob/main/ressources/Capture05.PNG)

Une fois la simulation automatique lancée, il est possible de l'arrêter à tout moment en appuyant sur le bouton "Stop" qui aura remplacé le bouton "Simulation automatique".

![alt texte](https://github.com/Nathan-Carre/projet_incendie/blob/main/ressources/Capture06.PNG)


### 4 - Sauvegarder le terrain


