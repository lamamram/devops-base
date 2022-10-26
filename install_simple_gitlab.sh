#!/bin/bash


# 1. prérequis
apt-get update
apt-get install -y gnupg curl lsb_release openssh-server ca-certificates tzdata 
apt-get install -y apt-transport-https

# 2. ajout du dépôt
apt_repo_url="https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/config_file.list?os=ubuntu&dist=focal&source=script"
apt_repo_path="/etc/apt/sources.list.d/gitlab_gitlab-ee.list"
curl -sSf "$apt_repo_url" > $apt_repo_path

# 3. ajout de la clé d'authentification GPG
gpg_key_url="https://packages.gitlab.com/gitlab/gitlab-ee/gpgkey"
gpg_keyring_path="/usr/share/keyrings/gitlab_gitlab-ee-archive-keyring.gpg"
curl -fsSL "$gpg_key_url" | gpg --dearmor > $gpg_keyring_path

apt-get update

EXTERNAL_URL=http://gitlab.formation.lan apt-get install gitlab-ee
# gitlab-rake "gitlab:password:reset[root]"
