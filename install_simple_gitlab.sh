#!/bin/bash

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

# 2. ajout du dépôt
apt_repo_url="https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/config_file.list?os=ubuntu&dist=focal&source=script"
apt_repo_path="/etc/apt/sources.list.d/gitlab_gitlab-ee.list"
# REM: différence entre variable et $variable aui désigne la valeur de la variable
# REM: les valeurs de vairables sont interpolées dans les chaines de caractères
curl -sSf "$apt_repo_url" > $apt_repo_path

# 3. ajout de la clé d'authentification GPG
gpg_key_url="https://packages.gitlab.com/gitlab/gitlab-ee/gpgkey"
gpg_keyring_path="/usr/share/keyrings/gitlab_gitlab-ee-archive-keyring.gpg"
curl -fsSL "$gpg_key_url" | gpg --dearmor > $gpg_keyring_path

apt-get update

EXTERNAL_URL=http://gitlab.formation.lan apt-get install gitlab-ee
# gitlab-rake "gitlab:password:reset[root]"
