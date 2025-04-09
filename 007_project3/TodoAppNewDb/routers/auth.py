from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from starlette import status
from database import SessionLocal
from models import User , Todos

router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


class CreateUserRequest(BaseModel):
    email: str 
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active:bool
    role: str

@router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserRequest):
    user_model = User(**user.model_dump())
    # db.add(user_model)
    return user_model
