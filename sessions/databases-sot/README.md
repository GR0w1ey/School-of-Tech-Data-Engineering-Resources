# Databases - Relational (School of Tech)

PostgresSQL session as this is what backs RedShift (used later in AWS).

Focusses on the DDL and DML as practical rather than theory - the Generation `databases` session is twice as long and includes lots of theory.

## Objectives

- Learn the features of a database
- Learn why we need databases
- Get introduced to the differences between relational and non-relational databases
- See some examples of SQL and learn about DDL and DML
- Learn, and practice using, SQL commands to interact with a database
- Learn, and practice using, Python to interact with a database

## Timings

- This session is timetabled for 4 blocks at 1.5 hrs each, i.e. 1 elapsed training day
    - This is best split over 2 days to avoid learner fatigue
    - The first 3 blocks are doing SQL in a PostgresSQL docker container
    - The last (4th) block is connecting with Python
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

### Prep - day before

Get the Academites to do the docker (or podman) pulls in advance.

```sh
podman pull docker.io/postgres:latest
podman pull docker.io/adminer:latest
podman run docker.io/hello-world # checks that something can run
```

Users on AL1 processors (new macbooks) have to use `mariadb`:

```sh
podman pull docker.io/mariadb:latest
```

These are interchangeable with `docker` commands.

Learners on Windows machines can also pull images via the podman-desktop GUI interface.

Make sure they can run a postgres using the command in script [./exercises/run-postgres-podman.sh](./exercises/run-postgres-podman.sh).

To get a terminal open in the database, you can use [./exercises/exec-into-postgres-podman.sh](./exercises/exec-into-postgres-podman.sh). Windows users can run the command directly in Powershell or Windows Terminal.

You can check the docker compose file is good using [./exercises/setup-all-podman-compose.sh](./exercises/setup-all-podman-compose.sh). Podman Compose won't work in WSL.

Equivalent helper scripts and compose files for `docker` as well as `podman` have also been provided should they be useful.

Then as usual;

- Export the presentation to PDF and the zip for distribution using `make generate-session-files f=session_name`
- The cheatsheet MD files in the `handouts` folder can be viewed in the IDE once shared.

*Importantly* make sure you test out the *exercises* and *solutions* as below!

## Windows vs. Mac/Unix

Users doing this session natively in Windows (i.e. not in WSL) will need;

- Python 3.12 natively installed
    - As at April 2024 Python 3.13+ did not work with `psychopg2`
- Podman / Docker natively installed (i.e. not in WSL)
- To use a Powershell terminal, or Windows terminal
- Note on [./exercises/requirements.txt](./exercises/requirements.txt)
    - As at April 2024 we needed the `psychopg2-binary` not `psychopg3`
    - And then had to import and use `psychopg2` in [./exercises/my_db_app.py](./exercises/my_db_app.py)
    - as this is supported on Windows and in Unix / Mac, but `psychopg3` was not yet

Those using WSL can have Podman installed natively inside that, as it's an Ubuntu machine.

Those using Unix/Mac should have no issues with Podman / Docker installed as per the laptop setup sessions.

## Session

1. Make sure you go through the speaker notes during the presentation - there is a lot of good information in there!
1. Distribute the cheatsheets in the `handouts` folder
1. Create breakouts of 3-4 learners at the start of the day, and use these same breakouts all day, for all exercises.
1. Run the slide deck
1. You can connect to the local Podman/Docker postgres container
    1. Any tool you want to use for showing and practicing the SQL is good - including online DB tools
    1. e.g. Can use https://www.db-fiddle.com/ to do a code-along

## Postgres worked example - last block / 1.5 hrs of day

- It works off a pre-built db using a Podman/Docker compose file
    - See `exercises/docker-compose.yaml`
- In addition to [./exercises/setup-all-podman-compose.sh](./exercises/setup-all-podman-compose.sh), [./exercises/setup-all-podman.sh](./exercises/setup-all-podman.sh) has also been provided for instances where learners running podman in WSL have had issues using podman-compose successfully.
- Known issue: There has been a problem in the past during previous cohorts where the cniVersion is updated to 1.0.0 (which is the latest) automatically in `databases_network.conflist` when any network is created with `podman network create`. However there is bug in `cniVersion 1.0.0` and it needs to be reverted to `cniVersion 0.4.0`.
    - Solution: A script `./exercises/replace_cniVersion.py` is provided which can change this automatically and is called in `./exercises/setup-all-podman.sh`.
- Start from `./exercises` and work towards `./solutions`.
- Only the `./exercises/my_db_app.py` file needs updating
