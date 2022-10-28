# 1. créer une connexion à l'api GITLAB grâce au token
# package python-gitlab : pip install --upgrade python-gitlab

from re import search
import gitlab

GITLAB_USER = "root"
GITLAB_TOKEN = "glpat-GVdzmFjnsRc-zX2yFVXK"
GITLAB_HOST = "http://gitlab.formation.lan"
GITLAB_PROJECT = "devops"

gl = gitlab.Gitlab(
    url=GITLAB_HOST,
    private_token=GITLAB_TOKEN
)

if not gl.projects.list(search=GITLAB_PROJECT):
    project = gl.projects.create({
        'name': GITLAB_PROJECT,
        "visibility": "private"
    })
    print(f"projet {GITLAB_PROJECT} created !!")

