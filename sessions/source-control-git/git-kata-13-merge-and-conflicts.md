---
title: Git Kata 13 - merge and conflicts
resources: source-control-git
---

## Git Kata 13

### Merge and conflicts

---

### Merging branches and dealing with conflicts

Today you will be learning how to pull remote changes and deal with merge conflicts.

Don't forget to push any mini-project changes!

---

### Exercise

Today's exercise is a little more complicated than previous ones. You need to make sure you follow these steps in the right order, or you might get a different result. Shout for help if you get stuck!

- Open the repository for your mini project in GitHub
- On the `main` branch, make a change to an existing line in the `README.md` file and commit it in GitHub, similar to how you did it in exercise 10
- Open the local repository in VSCode
- Checkout the `main` branch if it isn't already
- Make a change to the _same_ line in the `README.md` file
- Add and commit that change to your local repo
- Try to push your change. What happened?
- Run `git pull` to pull the commit on the remote repository
- You should see a message telling you that the automatic merge failed, and that you need to fix conflicts and commit the result
- VSCode should have helpfully highlighted the conflict(s) for you, and provides some options for how to resolve it. Click on the appropriate choice (either `accept incoming`, i.e. from remote, or `accept current`, i.e. local)
- Save the file after you have resolved the conflict(s)
- Add and commit (you can just type `git commit` without a commit message).
- Push your commit to the remote repository.
- Go and take a look in GitHub. You should see the change that you chose to accept on the remote repository

Note: in this example we again made a commit directly on GitHub. This is not recommended, we are doing this only to pretend that another person pushed a change to the `README.md` file from their local repo in order to demonstrate a merge conflict.
