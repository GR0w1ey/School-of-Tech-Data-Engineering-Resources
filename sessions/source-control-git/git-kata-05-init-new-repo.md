---
title: Git Kata 5 - Init a new repo
resources: source-control-git
---

## Git Kata 5 - Init a new a repo

### Init

---

### Creating a repository revisited

Today you will be creating a repository for an existing project from your terminal.

Make sure you have committed and pushed any changes to your mini-project first!

---

### Description

There are many ways to do most things in git.

Today we will:

- Make an empty shell of a repo in the Git website.
- Make content (a new folder with some files) on our local machine
- Link our local folder to the repository "shell"
- Push our folder and files into the "shell" to fill it up

---

### Exercise

- In a finder window or in your terminal, create a new directory and move some files into it (or create some)
- Navigate to the new directory
- Create a README.md file in the new directory and put a title in it
- Use the command `git init` to initialise a local repository for your project
- In the browser, create a new empty repository in GitHub (see day 1 if you have forgotten how to do this). Don't add a README or a .gitignore to it
- Copy the `SSH` link from the `Quick setup - if you've done this kind of thing before` section
- Run this to add the new remote repository as the origin for your local repository:
    - `git remote add origin <your_SSH_link>`
- Add, commit and push your code to the remote
- Don't delete this repository. We will be using it again in future exercises
