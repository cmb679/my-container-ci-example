# Container + Sandbox + CI Example

This project demonstrates:

- A FastAPI app running in a Docker container
- A local sandbox environment using Docker Compose
- A complete CI pipeline using GitHub Actions

## Run locally

Start the sandbox:

docker compose up --build


Then open:

http://localhost:8000

## Run tests

pytest


## Build container manually

docker build -t myapp .
docker run -p 8000:8000 myapp