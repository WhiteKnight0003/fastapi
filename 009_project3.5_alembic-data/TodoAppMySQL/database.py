from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# phải cài # pip install pymysql

# trong file alembic.ini cũng phải sửa sqlaichemy theo đường dẫn ở dưới
# định dạng chuỗi kết nối với MySQL :  mysql+pymysql://username:password@hostname:port/database_name
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:sktt1popo@127.0.0.1:3306/TodoAppdb'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False , autoflush= False , bind= engine)

Base = declarative_base() 

