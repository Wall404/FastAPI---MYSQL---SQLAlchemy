from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:mysqlpw@localhost:49153/storedb")

meta = MetaData()

conn = engine.connect()