from fastapi import FastAPI
from database import Base, engine
import models 
from routers import auth, todos, admin, Users

# pip install psycopg2-binary

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(Users.router)


