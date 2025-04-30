from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated, Optional
from starlette import status
from database import SessionLocal
from fastapi import Depends, HTTPException, APIRouter
from models import User , Todos
from sqlalchemy.orm import Session
from passlib.context import CryptContext
# CryptContext giúp bạn dễ dàng mã hóa và xác minh mật khẩu bằng cách định nghĩa một "ngữ cảnh mã hóa" (encryption context), tức là cấu hình các thuật toán và tùy chọn mã hóa.

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
'''
- schemes=['bcrypt']: nghĩa là bạn đang chỉ định thuật toán mã hóa là bcrypt.

- bcrypt là một thuật toán băm mạnh, thường dùng để lưu trữ mật khẩu một cách an toàn.

- deprecated='auto': là một tùy chọn giúp tự động đánh dấu những thuật toán không còn được dùng nữa là đã lỗi thời (deprecated).
'''

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user: # not None and not empty
        return False
    if not bcrypt_context.verify(password, user.hashed_password): 
        ''' so sánh mật khẩu đã nhập rồi dùng thuật toán mã hóa  với mật khẩu đã được mã hóa trong db '''
        return False
    return user

class CreateUserRequest(BaseModel):
    email: str 
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active:bool
    role: str

@router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserRequest, db : db_dependency):
    user_model = User(**user.model_dump())
    user_model.hashed_password = bcrypt_context.hash(user.hashed_password)
    db.add(user_model)
    db.commit()
    return 'them thanh cong'

@router.get('/', status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(User).all()


@router.post('/token')
async def login_for_access_token(
    form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
    db : db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db) 
    """usernaem, pass, db"""
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Failed Authentication"
        )
    return {"message": "Success Authentication"}
    

