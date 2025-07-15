# docker-compose.yaml Naming
### Standard Names (Auto-detected by Docker Compose)
### Primary convention:

```
docker-compose.yml (most common)
docker-compose.yaml (also widely used)
```

### Secondary options:
```
compose.yml (newer, simpler convention)
compose.yaml
```
**Docker Compose automatically looks for these files in the current directory, so you don't need to specify the -f flag.**

### For multiple services in one project:

```
docker-compose.web.yml
docker-compose.db.yml
docker-compose.cache.yml
```

### For different deployment targets:
```
docker-compose.local.yml
docker-compose.dev.yml
docker-compose.prod.yml
```
### File Extension Preference
Both .yml and .yaml are valid:

- .yml is shorter and more common in Docker ecosystem
- .yaml is more explicit **and follows YAML specification**

# Run a single service with automatic cleanup
```
docker-compose run --rm web bash
docker-compose run --rm app python script.py
```