[![Docker Image CI](https://github.com/banner4422/random_ping/actions/workflows/docker-image.yml/badge.svg)](https://github.com/banner4422/random_ping/actions/workflows/docker-image.yml)
# random_ping
Ping a URL at a random time in the seconds interval you specify.

Logging shows status code and when the next ping will occur.

## Requirements

- Python 3.x
- Docker (if running in a container)

## Usage
### Command Line
```bash
python random_ping.py http://localhost:3000 3600
```
```bash
export PING_URL="http://localhost:3000"
export PING_INTERVAL=3600
python random_ping.py
```
### Docker
If you want to build the image yourself:
```bash
docker build -t random_ping .
docker run -e PING_URL="http://localhost:3000" -e PING_INTERVAL=3600 random_ping
```
If you want to use the pre-built image from GitHub Container Registry with the latest commit on the master branch:
```bash
docker run -e PING_URL="http://localhost:3000" -e PING_INTERVAL=3600 ghcr.io/banner4422/random_ping:master
```
An example of using docker-compose
```yaml
services:
  random-ping:
    image: ghcr.io/banner4422/random_ping:master
    environment:
      - PING_URL=http://localhost:3000
      - PING_INTERVAL=3600
    restart: unless-stopped
```

## License
This project is licensed under the **GNU Affero General Public License, Version 3.0**. See [LICENSE](LICENSE) for more information.
