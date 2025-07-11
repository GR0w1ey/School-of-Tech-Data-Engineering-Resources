#!/bin/sh

###
### Script to run local unit tests with pytest
###

### You can run ./install.sh before this file

source .venv/bin/activate

echo "Running pytest..."
python3 -m pytest -v -s
