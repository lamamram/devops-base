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