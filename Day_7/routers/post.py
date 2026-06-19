from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import asc,desc
from sqlalchemy.orm import Session
from ..models import User, Post
from ..schemas import PostCreate
from ..dependencies import get_db, require_role
from typing import Optional

router = APIRouter(prefix="/posts", tags=["Posts"])

SAFE_SORT_FIELDS = {"created_at", "title", "category"}

#Ex.6 --> Ex.7,8
@router.get("/")
def list_posts(
    page: int = 1,
    limit: int = 10,
    author: str = None,
    category: str = None,
    published: bool = None,

    search: str = None,
    sort:   str = "created_at",
    
    db: Session = Depends(get_db)
):
    q = db.query(Post)
    
    #Ex.7(Filter)
    if author:
        q = q.join(User).filter(User.username == author)

    if category:
        q = q.filter(Post.category == category)

    if published is not None:
        q = q.filter(Post.published == published)
    
    #Ex.8(Search & Sort)  
    if search:
        q = q.filter(
            Post.title.ilike(f"%{search}%") |
            Post.content.ilike(f"%{search}%")
        )
    
    if sort in SAFE_SORT_FIELDS:
        q = q.order_by(asc(getattr(Post, sort)))

    total = q.count()
    offset = (page - 1) * limit
    posts = q.offset(offset).limit(limit).all()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": posts
    }

@router.post("/", status_code = 201)
def create_post(
    data: PostCreate,
    db: Session = Depends(get_db)
):
    user = db.get(User, data.author_id)

    if not user:
        raise HTTPException(
            status_code = 404,
            detail="User not found"
        )

    post = Post(
        title = data.title,
        content = data.content,
        category = data.category,
        published = data.published,
        author_id = data.author_id
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post

#Ex.11
@router.delete("/{post_id}", status_code=204)
def delete_post(
    post_id: int,
    current_user: User = Depends(require_role("admin")),
    db: Session = Depends(get_db)
):
    post = db.get(Post, post_id)

    if not post:
        raise HTTPException(
            status_code = 404,
            detail = "Post not found"
        )

    db.delete(post)
    db.commit()