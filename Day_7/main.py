from fastapi import FastAPI, APIRouter
from .database import engine, Base

from .routers import user, post

app = FastAPI()

#Ex.1
@app.get("/")
def root():
    return {"message": "Database connected"}

Base.metadata.create_all(bind=engine)

#Ex.3
app.include_router(user.router)

#Ex.5
app.include_router(post.router)