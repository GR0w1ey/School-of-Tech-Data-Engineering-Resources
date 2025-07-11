# How to get a repo cloned in GitBash

You may find working with repos in GitBash easier than Powershell.

- Install it from <https://git-scm.com/downloads> for Windows
- Restart VSCode so it picks it up
- In a VSCode window, open a GitBash terminal
- In the GitBash terminal, run this `nano ~/.bash_profile`
- In the file that opens paste this:
    - `export PUPPETEER_EXECUTABLE_PATH='/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'`
- Type ctrl-X to exit and save
- Close the terminal
- Open a new GitBash terminal, then run this to check the config is set up:
    - `echo $PUPPETEER_EXECUTABLE_PATH`
- Then you need to set all these settings as per your work email and work ssh key registered in Git:

    ```bash
    git config --global user.name "Alice Bloggs"
    git config --global user.email "alice.bloggs@accenture.com"
    git config --global init.defaultBranch main
    git config --global core.pager cat
    git config --global core.editor "notepad"
    git config --global pull.rebase false
    git config --global fetch.prune true
    ```

- Now you can run `git clone <my-repo>` in Powershell:
    - Change directory to `C:\sot-de-<month>-<year>`
    - Run `git clone <my-repo>`
