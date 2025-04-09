# pip install sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
- create_engine: Tạo kết nối đến cơ sở dữ liệu
- sessionmaker: Tạo lớp Session để tương tác với cơ sở dữ liệu
- declarative_base: Tạo lớp cơ sở để định nghĩa các mô hình (models)
'''


# SQLALCHEMY_DB_URL: sử dụng SQLite, lưu vào file todos.db.
SQLALCHEMY_DB_URL = 'sqlite:///./todos.db'   
# tạo file SQLite có tên todos.db trong thư mục hiện tại

# connect database 
# connect_args={'check_same_thread' : False} Tham số này tắt chế độ kiểm tra luồng (thread) trong SQLite (chỉ riêng với SQLite).
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={'check_same_thread' : False})

# create session to database
Sessionlocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
'''
- là một phần rất quan trọng trong việc làm việc với SQLAlchemy ORM. 
    Nó giúp tạo ra "phiên làm việc với database" (sessions) để bạn có thể thêm, sửa, xóa, truy vấn dữ liệu.
- sessionmaker : để tạo các session mới
- autocommit = False : bạn phải tự gọi commit() để lưu thay đổi vào DB.
- autoflush=False : Khi False: SQLAlchemy không tự động đẩy thay đổi (flush) từ session vào DB mỗi khi bạn query.
- bind=engine : Liên kết (bind) session này với engine – tức là với cơ sở dữ liệu (ở đây là todos.db)
'''

Base = declarative_base()
'''
- Base là lớp cơ sở mà tất cả các model (bảng) sẽ kế thừa từ đó
'''

