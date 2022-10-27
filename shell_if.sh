#!/bin/bash
# shebang: le fichier est exécuté par bash

# redirection vers le périph nul => plus d'affichage
command -v tree > /dev/null
# code de retour dans $?
if [ "$?" -ne "0" ]; then
  echo "installation de tree"
  apt-get install -y tree
else
  echo "tree détecté"
fi

  