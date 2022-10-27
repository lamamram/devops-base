#!/bin/bash
# shebang: le fichier est exécuté par bash
#REM: utilisation de cut pour séparer la commande du package
# cut travaille sur des flux (fichier, stdin , sortie de commande)
# non sur des chaines de caractères
# echo "chaine" | envoie une chaine de caractère comme flux d'entrée
# echo "gpg,gnupg" | cut -d ',' -f1

check()
{
  command -v $1 > /dev/null
  if [ "$?" -ne "0" ]; then
    echo "installation de $2"
    apt-get install -y $2
  else
    echo "$1 détecté"
  fi
}

prerequisites="curl,curl lsb_release,lsb_relase tree,tree gpg,gnupg sshd,openssh-server"
for pair in $prerequisites
do
  # $(): valeur de sortie de la commande à l'intérieur
  cmd=$(echo "$pair" | cut -d ',' -f1)
  package=$(echo "$pair" | cut -d ',' -f2)
  check $cmd $package
done