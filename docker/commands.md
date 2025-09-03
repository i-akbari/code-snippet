# image
docker images --digests

# volume
### Create volume
`docker volume create my-volume`

### List volumes
`docker volume ls`

### Remove volume
`docker volume rm my-volume`

### Remove unused volumes
`docker volume prune`

### Copy data from container to volume
`docker cp mycontainer:/app/data/. my-volume:/`

# system
### see volume size and others things
```
docker system df -v
docker system df
```

# proxy
### docker pull
```
HTTPS_PROXY=http://127.0.0.1:2081 docker pull postgres:16.0

# or

sudo mkdir -p /etc/systemd/system/docker.service.d
sudo nano /etc/systemd/system/docker.service.d/http-proxy.conf

[Service]
Environment="HTTP_PROXY=http://proxyhost:port"
Environment="HTTPS_PROXY=http://proxyhost:port"
Environment="NO_PROXY=localhost,127.0.0.1"

sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl restart docker

sudo systemctl show --property=Environment docker
``
