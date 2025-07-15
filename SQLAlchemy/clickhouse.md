# method 1:
### مزیت این روش این است که کلید را خودش کنترل می کند
```
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('clickhouse://<username>:<pass>@127.0.0.1:8123/TSETMC')
Session = sessionmaker(bind=engine)
session = Session()

Base = automap_base()
Base.prepare(engine, reflect=True)

session.bulk_insert_mappings(Base.classes.marketwatch, record_list)
session.commit()
```

# method 2:
```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from clickhouse_sqlalchemy import types

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'marketwatch'

    symbol = Column(types.String, primary_key=True)
    market_time = Column(types.DateTime64(3), primary_key=True)

    __table_args__ = {'autoload_with': engine, 'extend_existing': True}


# or

class ETF(Base):
    __table__ = Table("ETF", Base.metadata, autoload_with=mzfund_engine)
    __mapper_args__ = {
        "primary_key": [__table__.c.confirmdate, __table__.c.fund, __table__.c.mellinumber, __table__.c.requesttype, __table__.c.count]
    }
```