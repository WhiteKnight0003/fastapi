from database import Sessionlocal
from models import Todos

# Tạo session để làm việc với DB
db = Sessionlocal()

try:
    # Tạo một todo mới
    new_todo = Todos(
        title="Học FastAPI",
        description="Xây dựng REST API với FastAPI và SQLAlchemy",
        priority=1,
        complete=False
    )
    
    # Thêm vào database
    db.add(new_todo)

    new_todo1 = Todos(
        title="Học python",
        description="tren udemy",
        priority=4,
        complete=True
    )
    
    # Thêm vào database
    db.add(new_todo1)
    
    new_todo2 = Todos(
        title="tienchung",
        description="tìm hiểu api",
        priority=2,
        complete=False
    )
    
    # Thêm vào database
    db.add(new_todo2)

    # Commit để lưu thay đổi
    db.commit()
    
    print("Thêm dữ liệu thành công!")
    
    # Nếu bạn muốn lấy ID của todo vừa thêm
    print(f"ID của todo vừa thêm: {new_todo.id}")
    
except Exception as e:
    # Nếu có lỗi, rollback lại thay đổi
    db.rollback()
    print(f"Có lỗi xảy ra: {e}")

finally:
    # Luôn đóng session khi không dùng nữa
    db.close()