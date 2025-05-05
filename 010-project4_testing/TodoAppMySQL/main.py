from fastapi import FastAPI
# from database import  engine
from .database import  engine
#import models 
from .models import Base 
#from routers import auth, todos, admin, Users
from .routers import auth, todos, admin, Users

# pip install psycopg2-binary

app = FastAPI()
#models.Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)

@app.get('/healthy')
def health_check():
    return {'status': 'healthy'}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(Users.router)


