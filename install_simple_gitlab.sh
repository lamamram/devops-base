#!/bin/bash

# $# : nombre de paramètres du script
if [ "$#" -lt 2 ]; then
  echo "this script needs two arguments: [gitlab domain name] & [network interface]"
  exit 1
fi

# $1, $2 correspondent à la position des paramètres à l'appel
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

# 1. prérequis
apt-get update
apt-get install -y ca-certificates tzdata

prerequisites="curl,curl lsb_release,lsb_relase tree,tree gpg,gnupg sshd,openssh-server"
for pair in $prerequisites
do
  # $(): valeur de sortie de la commande à l'intérieur
  cmd=$(echo "$pair" | cut -d ',' -f1)
  package=$(echo "$pair" | cut -d ',' -f2)
  check $cmd $package
done

apt-get install -y apt-transport-https


dist=$(lsb_release -c | cut -f2)
os=$(lsb_release -i | cut -f2 | tr "[A-Z]" "[a-z]")

# 2. ajout du dépôt
apt_repo_url="https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/config_file.list?os=${os}&dist=${dist}&source=script"
apt_repo_path="/etc/apt/sources.list.d/gitlab_gitlab-ee.list"
# REM: différence entre variable et $variable aui désigne la valeur de la variable
# REM: les valeurs de vairables sont interpolées dans les chaines de caractères
curl -sSf "$apt_repo_url" > $apt_repo_path
if [ "$?" -eq "0" ]; then
  echo "gitlab repo installed !"
else
  echo "could not find repo version for os: $os ans dist: $dist !!"
  exit 1
fi

# 3. ajout de la clé d'authentification GPG
gpg_key_url="https://packages.gitlab.com/gitlab/gitlab-ee/gpgkey"
gpg_keyring_path="/usr/share/keyrings/gitlab_gitlab-ee-archive-keyring.gpg"
curl -fsSL "$gpg_key_url" | gpg --dearmor > $gpg_keyring_path

# recharger le cache apt pour tenir compte du nouveau dépôt
# apt-cache search 'gitlab-*' pour vérifier la dispo de gitlab-ee
apt-get update

# EXTERNAL_URL va être utilisée par l'installeur gitlab pour constituer 
# le nom d'hôte du site
# 1. il faut gérer un dns local dans windows 192.168.???.??? http://gitlab.formation.lan
# 2. on va récupérer le mdp root de gitlab
EXTERNAL_URL=$1 apt-get install gitlab-ee -y
cat /etc/gitlab/initial_root_password
# afficher l'interface enp0s8 | récupérer la regex inet IP | récupérer IP  
ip a show dev $2 | grep -owP "inet (\d+\.){3}\d+" | cut -d ' ' -f2
# gitlab-rake "gitlab:password:reset[root]"
