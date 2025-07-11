#!/bin/sh

###
### Script to set your git globals to useful defaults
###

git config --global user.name "Alice Bloggs"
git config --global user.email "alice.bloggs@infinityworks.com"

git config --global init.defaultBranch main
git config --global core.pager cat
git config --global core.editor "nano"
git config --global pull.rebase false
git config --global fetch.prune true
