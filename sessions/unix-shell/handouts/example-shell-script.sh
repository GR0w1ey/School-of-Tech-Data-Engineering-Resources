```sh
#!/usr/bin/env bash

set -e

sudo apt-get update

# install ukuu
echo "Installing ukuu..."
wget -O ukuu.deb https://github.com/teejee2008/ukuu/releases/download/v18.9.1/ukuu-v18.9.1-amd64.deb
sudo apt-get install -fy ./ukuu.deb

# install Linux 5.2
echo "Installing Linux 5.2 ..."
sudo ukuu --install v5.2.11

# back up existing wifi firmware
echo "Creating backup directory..."
mkdir ~/bkp
echo "Backing up existing wifi drivers..."
sudo cp -r /lib/firmware/iwlwifi* ~/bkp

echo "Downloading drivers..."
wget -O iwlwifi.tgz https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi/iwlwifi-cc-46.3cfab8da.0.tgz

tar xzvf ./iwlwifi.tgz
echo "Installing drivers..."
sudo cp ./iwlwifi-cc-46.3cfab8da.0/iwlwifi-cc-a0-46.ucode /lib/firmware

echo "Done"
echo "Press any key to reboot"
read 
echo "Rebooting..."
sudo reboot
```