from fastapi import FastAPI
from database import Base, engine
import models 
from routers import auth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


