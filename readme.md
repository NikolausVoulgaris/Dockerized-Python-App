# Dockerized Python App

Simple Flask app running in Docker.

## Run locally
docker build -t app .
docker run -p 5000:5000 app
(or use docker compose)

## Tech
- Python
- Flask
- Docker

## CI/CD

This project uses GitHub Actions to:
- Install dependencies
- Run basic checks
- Build Docker image automatically on push

