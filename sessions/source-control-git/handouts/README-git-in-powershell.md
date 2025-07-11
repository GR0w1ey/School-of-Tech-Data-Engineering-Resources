# How to get a repo cloned in powershell

- In a Powershell (Admin) terminal use choco to install git with `choco install git`
- Close the terminal
- Open a new Powershell (Admin) terminal (not GitBash!)
- In the terminal make a new ssh token specifically for windows:
    - Follow <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows>
    - Copy the SSH key Public details from `C:Users\your.name\.ssh\id_*.pub`
- Browse to GitHub, then find "User | Settings | SSH and GPG keys"
    - Add your new ssh key
    - Give it a name like "My work laptop in Powershell"
    - Enable it for SSO with our GitHub org
- In your PowerShell terminal, you need to set all these settings as per your work email and work ssh key registered in Git:

    ```bash
    git config --global user.name "Alice Bloggs"
    git config --global user.email "alice.bloggs@accenture.com"
    git config --global init.defaultBranch main
    git config --global core.pager cat
    git config --global core.editor "nano"
    git config --global pull.rebase false
    git config --global fetch.prune true
    ```

- Now you can run `git clone <my-repo>` in Powershell:
    - Change directory to `C:\sot-de-<month>-<year>`
    - Run `git clone <my-repo>`
