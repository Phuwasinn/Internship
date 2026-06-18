from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import User
from ..schemas import UserCreate, UserUpdate
from ..dependencies import get_db

router = APIRouter(prefix="/users", tags=["Users"])

#Ex.3
@router.post("/", status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username = data.username,
        email = data.email,
        password = data.password
    )
    db.add(user)    
    db.commit()      
    db.refresh(user)  
    return user

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.put("/{user_id}")
def update_user(
    user_id: int, 
    data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)
    if not user: 
        raise HTTPException(404, "Not found")
    for k, v in data.model_dump(exclude_none = True).items():
        setattr(user, k, v)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}", status_code = 204)
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)
    if not user: 
        raise HTTPException(404, "Not found")
    db.delete(user)
    db.commit()
    
#Ex.4  
@router.get("/{user_id}/posts")
def get_user_posts(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "User not found")

    return user.posts