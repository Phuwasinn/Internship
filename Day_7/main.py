from fastapi import FastAPI, APIRouter, Depends, HTTPException
from .database import engine, Base
from .routers import user, post, auth
from .dependencies import get_current_user
from .models import User

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
#Ex.9-11
app.include_router(auth.router)

@app.get("/profile")
def profile(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user