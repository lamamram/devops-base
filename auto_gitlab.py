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


ssh_path = f"c:/Users/{os.getlogin()}/.ssh"
# appel à ssh-keygen.exe à travers python (system call)
# 1. découpe de la commande dans une liste
# 2. utilisation du paramètre input pour anticiper les demandes du script sur stdin
subprocess.run(["ssh-keygen", "-f", f"{ssh_path}/{GITLAB_PROJECT}"], input="\n\n")