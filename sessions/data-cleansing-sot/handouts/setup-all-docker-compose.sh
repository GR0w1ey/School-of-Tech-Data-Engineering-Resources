#!/bin/sh

# See https://stackoverflow.com/a/65570275/23819566, "GitBash: How to stop MinGW and MSYS from mangling path names given at the command line"
export MSYS2_ARG_CONV_EXCL="*" # Stops MinGW and MSYS from fiddling with paths
export MSYS_NO_PATHCONV=1      # Stops GitBash fiddling with paths

###
### Script to rebuild the db
###

# remove any old container from earlier in the session
set +e
docker kill my-postgres | true
set -e

# remove the old containers, if any
docker-compose down

# build and run the containers
docker-compose up --build -d

# see whats running
docker ps -a

# should show what sql has been run
docker logs my-postgres
