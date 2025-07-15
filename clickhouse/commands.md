# run with docker
```
docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 clickhouse/clickhouse-server
```

# connect to db
```
curl http://localhost:8123

docker exec -it clickhouse-server clickhouse-client
docker exec -it clickhouse-server clickhouse-client --database=mydb
docker exec -it clickhouse-server clickhouse-client --user=myuser --password=mypassword
docker exec -it clickhouse-server clickhouse-client --query "SELECT 1"
```

# execute query
```
curl -X POST 'http://localhost:8123' -d 'SELECT version()'

curl -X POST 'http://localhost:8123' \
  --user 'myuser:mypassword' \
  -d 'SELECT version()'
```

# If you have clickhouse-client installed on host:
```
sudo apt-get install clickhouse-client
clickhouse-client --host localhost --port 9000

docker run -it --rm --network host clickhouse/clickhouse-client \
  --host localhost --query "SELECT version()"

```