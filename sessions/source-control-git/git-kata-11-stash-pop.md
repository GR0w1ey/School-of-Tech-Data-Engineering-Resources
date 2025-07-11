---
title: Git Kata 11 - Stash and pop
resources: source-control-git
---

## Git Kata 11

### Stash and Pop

---

### Stash and Pop

Today you will be learning how to temporarily stash changes so that you can switch branches, and then unstash (or "pop") them when you want them back.

Don't forget to push any mini-project changes!

---

### Exercise

- Check out the branch you created in exercise 8 (or for extra practice, create a new one)
- Make a change to one of your files
- Use `git stash` to temporarily remove your changes (git will remember them in the "stash")
- Checkout the main branch
- Use `git stash pop` to reinsert your changes onto the main branch (you could also switch back to your feature branch before you do this and put them back there instead)

---

### Use Cases

`git stash` is a useful command when you are working on changes not ready to commit, but need to perform some other work in the meantime, e.g.:

- Stashing WIP (work in progress) in order to change branch to help a colleague or fix something more important
- Stashing some changes to allow you to pull changes a colleague has made to the same file without losing your WIP (note: this might result in a conflict when you run `git stash pop` but this can be resolved manually)
