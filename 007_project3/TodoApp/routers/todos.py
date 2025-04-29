
from fastapi import APIRouter , Depends, HTTPException, Path
from starlette import status
from pydantic import BaseModel, Field
from models import Todos
from database  import  Sessionlocal
from typing import Annotated
from sqlalchemy.orm import Session


router = APIRouter()

def get_db():
    db = Sessionlocal()
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

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0)
    complete: bool


@router.get('/')
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@router.get('/todo/{todo_id}', status_code=status.HTTP_200_OK)
async def read_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model =  db.query(Todos).filter(Todos.id == todo_id) .first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')


@router.post('/todo/create', status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()


@router.put('/todo/put/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete('/todo/delete/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    db.delete(todo_model)
    db.commit()




    