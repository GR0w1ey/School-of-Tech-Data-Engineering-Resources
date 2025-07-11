#!/bin/sh

###
### Script to create a local adminer container
###

echo "Starting local adminer container..."

# remove any old container from earlier in the session
set +e;
podman stop adminer_container | true;
podman rm adminer_container | true;
set -e;

# Start it
podman run --name adminer_container -p 8080:8080 \
  -d docker.io/adminer;

# Check it is running
podman ps -a;
