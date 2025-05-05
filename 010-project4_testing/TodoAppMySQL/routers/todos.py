from fastapi import APIRouter , Depends, HTTPException, Path
from starlette import status
from pydantic import BaseModel, Field
from ..models import Todos
from ..database  import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

# lấy thằng user mới được xác thực
from .auth import get_current_user

router = APIRouter(
    # prefix='/todos',
    # tags=['todos'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
# Annotated là một cách để gắn thêm metadata
# session : Đây là kiểu dữ liệu (class) của SQLAlchemy session — dùng để tương tác với database (thêm, sửa, xóa, truy vấn).
# Depends(get_db) : Đây là lời gọi đến hàm get_db() mà FastAPI sẽ tự động gọi giúp bạn mỗi khi API được chạy, và truyền vào session (db) cho bạn.
'''
Ghép lại: Annotated[Session, Depends(get_db)]
- Tôi muốn một biến kiểu Session, và tôi muốn FastAPI tự động tạo biến đó bằng cách gọi hàm get_db().”

'''
# lấy user
user_dependency = Annotated[dict, Depends(get_current_user)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0)
    complete: bool


# ví dụ như 1 người được làm công việc nào nó chỉ hiện công việc đó
@router.get('/')
async def read_all(user : user_dependency ,db: db_dependency):
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='authentication Failed'
            )
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()



@router.get('/todos/{todo_id}', status_code=status.HTTP_200_OK)
async def read_id(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='authentication Failed'
            )
    
    todo_model =  db.query(Todos).filter(Todos.id == todo_id and Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')


# lấy người dùng mới được xác thực bằng jwt và thực hiện hàm dưới đây
@router.post('/todos', status_code=status.HTTP_201_CREATED)
async def create_todo(user : user_dependency, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='authentication Failed'
            )
    # cái owner_id thì sử lý như thế kia vì nó là khóa ngoại khi phân rã dữ liệu không có nó
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))

    db.add(todo_model)
    db.commit()


@router.put('/todos/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency,db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='authentication Failed'
            )

    todo_model = db.query(Todos).filter(Todos.id == todo_id and Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete('/todos/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='authentication Failed'
            )
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id and Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    db.delete(todo_model)
    db.commit()




    