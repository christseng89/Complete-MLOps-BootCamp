# Role of Git in MLOps

1. Version Control
2. Collaboration and Team Workflow
3. Tracking Experiments
4. Branching for Experimentation (Dev, SIT, UAT, Prod etc.)
5. CI/CD
6. IaC
7. Collaboration Across Teams
8. Artifact Management
9. Auditability and Compliance

## Git Configurations

git version
git config --global --list
git config --global user.name "nachiketh"
git config --global user.email "support@manifoldailearning.in"
git config --global init.defaultBranch main
git config --global --list

## Git Commands

- git init
.. Loop #1 Start
- git add .
- git status
- git commit -am "..."
- git status
.. Loop #1 End

- git branch
- git branch dev
- git switch dev
- git status
- // Loop #1

## Git merging

- git swith main
- // Add file gitTest-main.txt
- git commit -am "gitTest-main v1"
- git push 

- git switch -c dev
- git checkout main // Merging from main
- // Edit file gitTest-dev.txt
- git commit -am "gitTest-dev v2"

- git swith main
- // Edit file gitTest-main.txt
- git commit -am "gitTest-main v3"

- git swith dev
- // Edit file gitTest-dev.txt
- git commit -am "gitTest-dev v4"
