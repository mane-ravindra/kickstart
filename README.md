# kickstart
Kick Start Journey

## Password less auth in Git
  * Generate an SSH key and add it to GitHub:
    * ssh-keygen -t ed25519 -C "mane.ravindra@gmail.com"
  * Then add it to GitHub: https://github.com/settings/keys
    * Find your public key (should end with .pub):
        * cat ~/.ssh/id_ed25519.pub
    * Copy the entire output (starts with ssh-ed25519 and ends with your email)
    * Go to GitHub → https://github.com/settings/keys
    * Click "New SSH key" and paste the public key content
    * Give it a title (e.g., "My Laptop")
    * Click "Add SSH key"
  * Change your repository remote to SSH:
      * git remote set-url origin git@github.com:mane-ravindra/kickstart.git
  * Then push:
      * git push --set-upstream origin <brnach>
      * git push --set-upstream origin hw
  * Reference - https://github.com/copilot/c/46d44ddf-e255-44f7-873d-90d249f05294 
