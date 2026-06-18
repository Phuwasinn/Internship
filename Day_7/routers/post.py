from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import User, Post
from ..schemas import UserCreate, UserUpdate
from ..dependencies import get_db
from typing import Optional

router = APIRouter(prefix="/products", tags=["Products"])

#Ex.6
@router.get("/posts")
def list_posts(
    page: int = 1, 
    limit: int = 10, 
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    query  = db.query(Post)
    total  = query.count()
    posts  = query.offset(offset).limit(limit).all()
    return {
        "page": page, 
        "limit": limit, 
        "total": total, 
        "data": posts
    }