---
title: Git Kata 8 - Branch
resources: source-control-git
---

## Git Kata 8

### Branch

---

### Creating a branch

Add, commit and push any changes from yesterday to your mini-project repository.

Today you will be creating and pushing to a branch in your repository.

---

### Branches

A branch is an alternative development path in your repository.

Branches are usually created from `main`, but they can branch from anywhere (like a tree).

Branches allow us to commit our work-in-progress, without affecting the original branch.

---

### What is a branch?

![](./img/git-branch-merge.png)

---

### Exercise

- Open any of the projects you already have that are set up with remote repositories
- In your terminal at the root of your project, create a branch using `git branch <branch_name>`.
- Switch to the new branch using `git checkout <branch_name>`.
- Make a change to one of the files and then push your change to the remote.
- Use `git checkout` again to switch back to the main branch (hint: you can either use `main` or `-` as the branch name).
    - aside: you will sometimes see `master` instead of `main`. By default, when you create a repository in GitHub it will use `main`, but you can change this in your settings. They usually mean the same thing.
- Check that the changes you committed are not there.

---

### Extension

Create another new branch, but this time use `git checkout -b <branch_name>`. How does this differ from what you did previously?
