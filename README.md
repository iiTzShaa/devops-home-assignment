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
Workflow Diagram
plaintext
Copy code
                     +------------------+
                     | GitHub Actions   |
                     |   Workflow       |
                     +------------------+
                             |
                             | Push to Main
                             |
                     +------------------+
                     | Docker Compose   |
                     |  (Local / CI)    |
                     +------------------+
                             |
                             |
                    +--------+--------+
                    |                 |
           +--------v--------+ +------v-------+
           |   Nginx Server  | | Python Test   |
           |  (Responds on   | |   Service     |
           |   Two Ports)    | | (Validates    |
           |                 | | Responses)    |
           +-----------------+ +---------------+
Nginx Server: Responds on two ports, each with a distinct response.
Python Test Service: Sends requests to both ports and checks if the responses match the expected output.
