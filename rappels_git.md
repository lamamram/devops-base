# RAPPELS sur git

1. création dépôt local
  * `git init` : création du dossier .git

2. renseigner les méta user.name et user.email sinon pas de commit
  * `git config --global user.name [name]`
  *  `git config --global user.email [name]`

3. création de commits
  * `git add .`: ajouts de toutes les modifs dans l'index
    - index: zone de préparation au commit (commit == version)
  * `git commit -m "message"`: création du commit
  * `git add . && git commit -m "msg"` 

4. historique des commits
  * `git log -p -[num]`: historique eds num derniers commit avec les modifs

5. état des fichiers dans git
  * `git status`
  * cycle d'un fichier dans git
    - **U**ntracked : nouveau fichier inconnu de git
    - **A**dded : ajouté à l'index
    - unmodified : dans le même état que dans le dernier commit contenant le fichier
    - **M**odified : modifié par rapport à la version du dépôt


6. synchronisation de dépôts
  * création d'un projet "devops" privé et vide dans gitlab
  
  * création de clés privée publique : 
    - `ssh-keygen` dans git bash (pas de passphrase)
    - renommer id_rsa(.pub) par devops(.pub)

  * ajout de la clé publique dans les clés ssh de l'utilisateur gitlab
    - copier le contenu de devops.pub
    - préférences utilisateurs -> SSH Keys -> Add key

  * configuration de la clé privée
    - créer ou éditer le fichier **config** dans **~/.ssh**
    - ajouter et adapter le bloc suivant

    ```
    Host gitlab.formation.lan
     IdentityFile "/c/Users/[username]/.ssh/devops"
     UserKnownHostsFile /dev/null
     StrictHostKeyChecking no
    ```

  * ajout du dépôt distant dans le dépôt local
    - `git remote add [nom du dépôt] [xxx@yyy.zz:path/to/repo.git]`

  * envoi des commits sur la branche master du dépôt distant
    - `git push [nom du dépôt] master`

