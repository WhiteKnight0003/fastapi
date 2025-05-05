from datetime import timedelta, datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated, Optional
from starlette import status
from ..database import SessionLocal
from fastapi import Depends, HTTPException, APIRouter
from ..models import User 
from sqlalchemy.orm import Session
from passlib.context import CryptContext
# CryptContext giúp bạn dễ dàng mã hóa và xác minh mật khẩu bằng cách định nghĩa một "ngữ cảnh mã hóa" (encryption context), tức là cấu hình các thuật toán và tùy chọn mã hóa.

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

# pip install "python-jose[cryptography]" 


'''
➡️ Có thêm prefix='/auth' → tất cả các API trong file này sẽ có URL bắt đầu bằng /auth (ví dụ /auth/token, /auth/)
➡️ tags=['auth'] → giúp nhóm lại trong Swagger UI cho rõ ràng.
'''
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

# phần Header
# lấy ngẫu nhiên token :  trong terminal gõ   openssl rand -hex 32   để tạo 1 mã ngẫu nhiên như trong secret_key
SECRET_KEY = 'ff7bee372bc1d7e7dfed41be278807b8c5e037c6cbede3c82f4c6697cc8a999d'
ALGORITHM = 'HS256' # gọi thuật toán


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
'''
- schemes=['bcrypt']: nghĩa là bạn đang chỉ định thuật toán mã hóa là bcrypt.
- bcrypt là một thuật toán băm mạnh, thường dùng để lưu trữ mật khẩu một cách an toàn
- deprecated='auto': là một tùy chọn giúp tự động đánh dấu những thuật toán không còn được dùng nữa là đã lỗi thời (deprecated).
'''

# Thêm tính năng phân quyền (bảo vệ route với JWT)
# Đây là cơ chế để tự động lấy token từ header Authorization của request khi client gửi.
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


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


"""
Tạo JWT chứa payload gồm:
sub: username (chủ thể)
id: user id
role : vai trò của ng đang muốn xác thưcj
exp: thời gian hết hạn
Mã hóa bằng SECRET_KEY với HS256.
"""
def create_access_token(username: str, user_id: int, role : str,expires_delta: timedelta):
        encode = {'sub': username, 'id': user_id, 'role': role} 
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


'''
➡️ Hàm này giúp giải mã token, xác thực người dùng đang gọi API nào đó.
👉 Dùng để áp dụng cho các route cần bảo vệ như /profile, /todo, v.v.


✅ Mục tiêu của get_current_user()
Hàm này dùng để xác thực người dùng đang gọi API, bằng cách:

Lấy JWT token từ HTTP Header (Authorization: Bearer <token>).
Giải mã token bằng secret key.
Trích xuất thông tin người dùng từ payload (ví dụ: username, user_id).
Trả về thông tin người dùng hiện tại
'''

# token : Annotated[str, Depends(oauth2_bearer)]  : "Lấy token từ header Authorization, đảm bảo đó là kiểu chuỗi (str), và gán vào biến token để sử dụng."
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role : str = payload.get('role')

        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate user'
            )
        return {'username': username, 'id': user_id, 'role':user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail='Could not validate user')
            

class CreateUserRequest(BaseModel):
    email: str 
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active:bool
    role: str
    phone_number: str


class Token(BaseModel):
    access_token: str
    token_type: str



@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserRequest, db : db_dependency):
    user_model = User(**user.model_dump())
    user_model.hashed_password = bcrypt_context.hash(user.hashed_password)
    db.add(user_model)
    db.commit()
    return 'them thanh cong'

@router.get('/', status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(User).all()


# response_model=Token	Giúp FastAPI kiểm soát và tự sinh docs chuẩn xác
@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
    db : db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db) 
    """usernaem, pass, db"""
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail='Could not validate user')
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}
    

