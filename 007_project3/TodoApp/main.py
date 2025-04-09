
from fastapi import FastAPI
import models 
from database  import engine
from routers import auth, todos # gọi đến thư mục auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
'''
- models.Base : Tất cả các model (ví dụ như Todos) đều kế thừa từ Base
- metadata : chứa siêu dữ liệu (metadata) về tất cả các bảng và cột bạn đã định nghĩa qua các model.

- create_all(bind=engine) : Lệnh này sẽ tạo bảng trong cơ sở dữ liệu nếu bảng đó chưa tồn tại. 
    bind=engine nghĩa là: dùng engine (đã kết nối tới todos.db) để chạy lệnh tạo bảng
'''

# main mới cần
# cái này dùng để mở rộng đường dẫn từ 1 
app.include_router(auth.router) # thêm router ở bên thư mục routers/auth
app.include_router(todos.router) # thêm router ở bên thư mục routers/todos

