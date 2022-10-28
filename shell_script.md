# script d'installation de gitlab en bash

1. n'installer les dépendances que si non encore installées

2. détecter l'os ubuntu et la distrib focal
  * utiliser lsb_release qui donne des informations sur ces éléments
  * transformer les résultats via 
     - cut : sous chaines liées à un délimiteur
     - tr : chercher / remplacer
  * placer les valeurs dans les variables os et dist
  * injecter ces variables dans l'url du dépôt

