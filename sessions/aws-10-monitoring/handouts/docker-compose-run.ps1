###
### Script to rebuild the db
###

# create the .env file with default values
$env_file = '.env'

"POSTGRES_HOST=localhost" | out-file -filepath $env_file -encoding ascii
"POSTGRES_USER=postgres" | out-file -filepath $env_file -encoding ascii -Append
"POSTGRES_DB=postgres" | out-file -filepath $env_file -encoding ascii -Append
"POSTGRES_PASSWORD=mysecretpassword" | out-file -filepath $env_file -encoding ascii -Append

# remove the old containers, if any
docker compose down

# build and run the containers
docker compose up -d

# see whats running
docker ps -a

# should show what sql has been run
docker logs my-postgres
