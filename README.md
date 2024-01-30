## Set-up Mage on Docker

This readme provides a guide to setting up a new Mage project using Docker Compose.

### Prerequisites

Docker installed locally. Follow the instructions [here](https://docs.docker.com/get-docker/) if not installed.

### Getting Started

1. Clone the repo:
```bash
git clone https://github.com/yash-chauhan-dev/mage-setup.git mage-project mage
```
2. Navigate to the repo:
```bash
cd mage-data-engineering-zoomcamp
```
3. Build the container:
```bash
docker compose build
```
4. Start the Docker container:
```bash
docker compose up
```
5. Access the Mage platform at http://localhost:6789 in your browser.