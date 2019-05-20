docker-nginx-letsencrypt
========================

This contains reference files for SSL enabled Nginx configs with Docker

- https://github.com/jwilder/nginx-proxy
- https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion
- https://blog.ssdnodes.com/blog/host-multiple-ssl-websites-docker-nginx/

## Installation

1. Create a docker network:
```bash
docker network create nginx-proxy
```

2. Get the **`nginx.tmpl`** file into the same directory as **`docker-compose.yml`**:
```bash
curl https://raw.githubusercontent.com/jwilder/nginx-proxy/master/nginx.tmpl > nginx.tmpl
```

3. Docker compose:

```bash
docker-compose up -d
```

There are other **`docker-compose.yml`** options at https://github.com/buchdag/letsencrypt-nginx-proxy-companion-compose

## Usage

Basic configuration for containers that want to be proxied and encrypted:

**`docker-compose.yml`:**

```yaml
version: '3'

services:
  example-app:
    container_name: example-app
    image: example/example-app
    expose:
      - 80
    environment:
      VIRTUAL_HOST: app.example.com
      LETSENCRYPT_HOST: app.example.com
      LETSENCRYPT_EMAIL: foo@example.com
    depends_on:
      - nginx-proxy
      - nginx-proxy-gen
      - nginx-proxy-le
    restart: unless-stopped

networks:
  default:
    external:
      name: nginx-proxy
```