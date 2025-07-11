#!/bin/sh

# See https://stackoverflow.com/a/65570275/23819566, "GitBash: How to stop MinGW and MSYS from mangling path names given at the command line"
export MSYS2_ARG_CONV_EXCL="*" # Stops MinGW and MSYS from fiddling with paths
export MSYS_NO_PATHCONV=1      # Stops GitBash fiddling with paths

###
### Script to create local postgres and adminer containers
###

echo ""
echo "Starting local postgres container..."

# remove any old containers from earlier in the session
echo "...removing old containers..."
set +e;
podman stop my-postgres | true;
podman rm my-postgres | true;
podman stop my-adminer | true;
podman rm my-adminer | true;
podman network rm databases_network | true;
set -e;

podman network create databases_network

python3 replace_cniVersion.py ~/.config/cni/net.d/databases_network.conflist

# The double quotes here are designed to work in GitBash
SRC="$(cd "$(dirname "$0")"; "pwd")/db-scripts"

# The scripts in ./db-scripts are executed in lexographical order
# Start it
podman run --name my-postgres \
  --network databases_network \
  -p 5432:5432 \
  -v "${SRC}":/docker-entrypoint-initdb.d \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -d docker.io/postgres;

echo ""
echo "...starting adminer container..."
podman run --name my-adminer \
  --network databases_network \
  -p 8080:8080 \
  -d docker.io/adminer;

# Check it is running
echo ""
podman ps -a;
echo ""

# Check what happened in the sql scripts
echo ""
podman logs my-postgres;
echo ""

echo "all done"
