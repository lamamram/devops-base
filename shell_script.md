# script d'installation de gitlab en bash

> en cas d'édition dans windows d'un fichier exécuté sous linux

> on peut convertir les saut de lignes CRLF \r\n de windows en LF \n sous linux

> avec vim -c "ff=unix" -c ":wq" file_name

1. n'installer les dépendances que si non encore installées

2. détecter l'os ubuntu et la distrib focal
  * utiliser lsb_release qui donne des informations sur ces éléments
  * transformer les résultats via 
     - cut : sous chaines liées à un délimiteur
     - tr : chercher / remplacer
  * placer les valeurs dans les variables os et dist
  * injecter ces variables dans l'url du dépôt

3. protéger l'appel curl sur la chaine de caractère paramétrée du dépôt

4. installer gitlab 
   * en récupérant le mdp root 
   * l'ip de la machine sur l'interface enp0s8
   * lancer le script avec les paramètres "http://gitlab.formation.lan" et "enp0s8"

