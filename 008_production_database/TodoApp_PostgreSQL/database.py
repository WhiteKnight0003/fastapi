from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# phải cài  :   pip install psycopg2-binary

# định dạng chuỗi kết nối với postgreSQL :  postgresql://username:password@hostname:port/database_name
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:sktt1popo@localhost/TodoAppdb'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False , autoflush= False , bind= engine)

Base = declarative_base() 

