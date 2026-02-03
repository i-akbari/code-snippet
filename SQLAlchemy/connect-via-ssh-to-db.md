# feat: how to use ssh in sqlalchemy to connect to db.

### this is not possible to connect to the db in third party tools when the code waited on a line in debugger. You must run the code and use time.sleep()

### you must use `connect_args={"autocommit": True}` in create_engine() in sqlalchemy

```
tunnel = SSHTunnelForwarder(
    ssh_address_or_host=('10.2.17.38', 22),  # SSH server
    ssh_username='',
    ssh_password='',  # or use ssh_pkey for key-based auth
    remote_bind_address=('172.23.104.16', 1433),  # Database server
    local_bind_address=('127.0.0.1', 0)  # Local port to forward to
)

# Start the tunnel
tunnel.start()
print(f"Local port assigned: {tunnel.local_bind_port}")

# uncomment to use tunnel to connect to db in Dtagrip

# import time
# while True:
#     time.sleep(10)  # Don't let it exit

try:
    # 2. Create SQLAlchemy engine through the tunnel
    # Note: Using localhost and the tunnel's local port
    
    username = "AirflowETLOperation"
    password = "m5mU37WBh0Kfg"
    server = "127.0.0.1"
    port = tunnel.local_bind_port
    database_name = "MofidDW"
    connection_string = f"mssql+pyodbc://{username}:{quote_plus(password)}@{server}:{port}/{database_name}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes&Encrypt=no"
    engine = create_engine(connection_string, echo=False, 
    connect_args={"autocommit": True}) # this line did the work!
    
    # 3. Use the engine normally
    df = pd.read_sql('SELECT top(10) * FROM MofidDW.dbo.FactBasketEfficiency', engine)
        
finally:
    # 4. Close the tunnel when done
    tunnel.stop()
```

# there is no extra work to connect via pyodbce
```
import pyodbc
conn_str = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server},{port};"
    f"DATABASE={database_name};"
    f"UID={username};"
    f"PWD={password};"
    "TrustServerCertificate=yes;"
    "Encrypt=no;"
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    # cursor.execute("SELECT TOP(1) 1")
    cursor.execute("SELECT top(10) * FROM MofidDW.dbo.FactBasketEfficiency")
    print(cursor.fetchone())
    conn.close()
except Exception as e:
    print("Connection failed:", e)
```