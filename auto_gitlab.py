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

# 2. création du projet
if not gl.projects.list(search=GITLAB_PROJECT):
    project = gl.projects.create({
        'name': GITLAB_PROJECT,
        "visibility": "private"
    })
    print(f"projet {GITLAB_PROJECT} created !!")


ssh_path = f"c:/Users/{os.getlogin()}.DESKTOP-8967908/.ssh"

## 3. création des clés
#. appel à ssh-keygen.exe à travers python (system call)
# 1. découpe de la commande dans une liste
# 2. utilisation du paramètre input pour anticiper les demandes du script sur stdin
# investiguer sous windows

# tester l'existence de la clé avant
if not os.path.exists(f"{ssh_path}/{GITLAB_PROJECT}"):
    subprocess.run(["ssh-keygen", "-f", f"{ssh_path}/{GITLAB_PROJECT}"], input=b'\r\n\r\n')
    print("pubkey/privkey generated !!")


## 4. upload de la clé
try:
    # 1. authentification de l'utilisateur courant
    gl.auth()
    with open(f"{ssh_path}/{GITLAB_PROJECT}.pub", "r") as f:
        key = gl.user.keys.create({
            'title': f'{GITLAB_USER}_ssh_key',
            'key': f.read()
        })
except Exception as e:
    # 2. si l'upload échoue, on sort du programme
    print(e, type(e))
    sys.exit(1)

# r+: lecture + écriture
with open(f"{ssh_path}/config", "r+") as f:
  # "slicing" de la chaine de caractère pour enelever http:// 
  if f"Host {GITLAB_HOST[7:]}\n" not in f.readlines():
    f.writelines([
      f"\n\nHost {GITLAB_HOST[7:]}\n",
      f" IdentityFile {ssh_path}/{GITLAB_PROJECT}\n",
      f" UserKnownHostsFile /dev/null\n",
      f" StrictHostKeyChecking no"
    ])
    print("- privkey config done !")

