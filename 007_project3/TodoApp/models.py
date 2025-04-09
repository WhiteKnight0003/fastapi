from database import Base
from sqlalchemy import Column, Integer, String, Boolean

# define structer sqlite databases
class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    
'''
- Dùng SQLAlchemy ORM để định nghĩa bảng todos trong database.
- Mỗi todo có: id, title, description, priority, complete.
'''