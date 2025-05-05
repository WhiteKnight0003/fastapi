from fastapi import APIRouter , Depends, HTTPException, Path
from starlette import status
from pydantic import BaseModel, Field
# nhưng file nằm ngoài folder thì ..
# những file cùng folder thì .
from ..models import Todos
from ..database  import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

# lấy thằng user mới được xác thực
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/todos', status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    # cái get_current_user trả ra các trường gì thì get theo cái đos
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Todos).all()

# @router.get('/todo/{todo_id}', status_code=status.HTTP_200_OK)
# async def read_user(user: user_dependency, db: db_dependency):
#     if user is None or user.get('user_role') != 'admin':
#         raise

@router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    db.delete(todo_model)
    db.commit()
    
