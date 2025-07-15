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
