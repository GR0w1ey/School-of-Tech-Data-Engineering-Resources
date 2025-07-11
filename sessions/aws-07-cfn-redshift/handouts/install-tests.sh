#!/bin/sh

###
### Script to install pip packages for local development
###

# Check if .venv folder exists
if [ ! -d ".venv" ]; then
    echo "Creating .venv folder..."
    # Create .venv folder using python3 venv module
    python3 -m venv .venv
    echo ".venv created successfully."
else
    echo ".venv already exists."
fi

# Activate venv
echo "Activating venv"
source .venv/bin/activate

# Install local packages for testing
echo "Installing pip packages"
pip install -r requirements-test.txt
