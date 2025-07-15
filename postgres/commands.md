# run with docker
```
docker run -d --name postgres \
  -e POSTGRES_DB=mydb \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  postgres
```

# Connect using psql:
```
docker exec -it postgres psql -U postgres
```

# Connect with custom user:
```
docker exec -it postgres psql -U myuser -d mydb
```

# Connect from host machine (if psql is installed):
```
psql -h localhost -U postgres -d postgres
```

# With Initialization Scripts
### Any .sql files in the init directory will be executed when the container starts for the first time.
```
docker run -d --name postgres \
  -e POSTGRES_PASSWORD=mypassword \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  -v ./init:/docker-entrypoint-initdb.d \
  postgres
```

# Common Environment Variables
- **POSTGRES_DB**: Database name to create
- **POSTGRES_USER**: Username to create
- **POSTGRES_PASSWORD**: Password for the user
- **POSTGRES_INITDB_ARGS**: Additional arguments for initdb
- **PGDATA**: Data directory path (default: /var/lib/postgresql/data

# run with docker compose
```
version: '3.8'
services:
  postgres:
    image: postgres:15
    container_name: postgres
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./init:/docker-entrypoint-initdb.d
    restart: unless-stopped

volumes:
  postgres-data:
```