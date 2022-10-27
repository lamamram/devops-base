#!/bin/bash
# shebang: le fichier est exécuté par bash

# fonction en shell
# pas de paramètres entre ()
# le code n'est pas exécuté
check()
{
  command -v $1 > /dev/null
  # code de retour dans $?
  if [ "$?" -ne "0" ]; then
    echo "installation de $1"
    apt-get install -y $1
  else
    echo "$1 détecté"
  fi
}

# appel à check avec le paramètre tree
# exécution de la fonction check
check tree
check lsb_release