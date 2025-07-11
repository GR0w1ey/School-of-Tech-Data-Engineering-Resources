#!/bin/sh

###
### Script to create a local postgres container
###

echo "Starting local postgres container..."

# remove any old container from earlier in the session
set +e;
podman stop my-postgres | true;
podman rm my-postgres | true;
set -e;

# Start it
podman run --name my-postgres -p 5432:5432 \
   -e POSTGRES_PASSWORD=mysecretpassword -d postgres;

# Check it is running
podman ps -a;
