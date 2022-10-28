# 1. créer une connexion à l'api GITLAB grâce au token
# package python-gitlab : pip install --upgrade python-gitlab

from re import search
import gitlab
import subprocess
import sys, os

GITLAB_USER = "root"
GITLAB_TOKEN = "glpat-GVdzmFjnsRc-zX2yFVXK"
GITLAB_HOST = "http://gitlab.formation.lan"
GITLAB_PROJECT = "devops"

gl = gitlab.Gitlab(
    url=GITLAB_HOST,
    private_token=GITLAB_TOKEN
)

# création du projet
if not gl.projects.list(search=GITLAB_PROJECT):
    project = gl.projects.create({
        'name': GITLAB_PROJECT,
        "visibility": "private"
    })
    print(f"projet {GITLAB_PROJECT} created !!")


ssh_path = f"c:/Users/{os.getlogin()}.DESKTOP-8967908/.ssh"
# appel à ssh-keygen.exe à travers python (system call)
# 1. découpe de la commande dans une liste
# 2. utilisation du paramètre input pour anticiper les demandes du script sur stdin
# investiguer sous windows

# tester l'existence de la clé avant
if not os.path.exists(f"{ssh_path}/{GITLAB_PROJECT}"):
    subprocess.run(["ssh-keygen", "-f", f"{ssh_path}/{GITLAB_PROJECT}"], input=b'\r\n\r\n')
    print("pubkey/privkey generated !!")
