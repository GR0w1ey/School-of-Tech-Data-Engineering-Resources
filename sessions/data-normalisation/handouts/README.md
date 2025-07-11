# Data Normalisation Exercises

Postgres files are provided for running your database.

## Notes

If you are using Podman in WSL:

- As Podman Compose does not work well in WSL2, files to run containers without compose are also given.

If you are using Docker Engine in WSL:

- The Compose files should behave, else use the separate scripts as above.

## Setup

1. If on Windows, make sure your Docker or Postman engine is running
    1. For Docker, run `docker ps -a` to check you can see your new and old containers
    1. For Podman, run:
        1. `podman machine list`
        1. **If** it is off (e.g. has no active memory `0b`),
            1. then run `podman machine start`
        1. Run `podman ps -a` to check you can see your new and old containers
1. Ensure your PostgreSQL container is running
    - You can either use Docker or Podman
    - Scripts for both are provided in the `./handouts` folder
    - **If** you have `docker compose` or `podman compose` working you can use:

        ```sh
        docker compose up -d
        # or
        podman compose up -d
        ```

    - If `compose` is **not** working for you, you can use the `./run*.sh` and `./setup*.sh` scripts provided in the `./handouts` folder

## Using a venv

> You can either re-use an existing venv, or create a new one just for this session. To use an existing one, jump ahead to the `Activate` step below.

1. You can create a virtual environment with python by running:
    - `python3 -m venv .venv` (MacOS / Unix)
    - `py -m venv .venv` (Windows)
    - `python3 -m venv .venv` (GitBash)
1. Activate your virtual environment by running:
    - `source .venv/bin/activate` (MacOS / Unix)
    - `.venv\Scripts\activate` (Windows)
    - `source .venv/Scripts/activate` (GitBash)
1. Install the `requirements.txt` file by running:
    - `py -m pip install -r requirements.txt` (Windows)
    - `python3 -m pip install -r requirements.txt` (MacOS / Unix)
    - `python -m pip install -r requirements.txt` (GitBash)
