# DevOps Home Assignment

This repository contains a Docker Compose setup to deploy and test an Nginx server. The setup includes:
- An **Nginx** server configured to respond on two different ports with distinct responses.
- A **Python test service** that checks the responses from the Nginx server.
- **GitHub Actions** configured to automate testing on each push to the `main` branch.

## Project Structure

```plaintext
devops-home-assignment/
├── Dockerfile.nginx          # Dockerfile for the Nginx server
├── Dockerfile.test           # Dockerfile for the Python test service
├── docker-compose.yml        # Docker Compose file defining the services
├── test_script.py            # Python script to test Nginx responses
└── .github/
    └── workflows/
        └── ci.yml            # GitHub Actions workflow for automated testing
