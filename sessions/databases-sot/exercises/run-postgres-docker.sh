#!/bin/sh

###
### Script to create a local postgres container
###

echo "Starting local postgres container..."

# remove any old container from earlier in the session
set +e;
docker stop my-postgres | true;
docker rm my-postgres | true;
set -e;

# Start it
docker run --name my-postgres -p 5432:5432 \
   -e POSTGRES_PASSWORD=mysecretpassword -d docker.io/postgres;

# Check it is running
docker ps -a;
