from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import asc
from sqlalchemy.orm import Session
from ..models import User, Post
from ..schemas import PostCreate, PostUpdate, PostResponse, APIResponse, ok
from ..dependencies import get_db, require_role, get_current_user
from ..cache import cache_get, cache_set, clear_posts_cache
from ..limiter import limiter

router = APIRouter(prefix = "/posts", tags = ["Posts"])

SAFE_SORT_FIELDS = {"created_at", "title", "category"}

#Create Post
@router.post(
    "/",
    status_code = 201,
    summary = "Create post",
    description = "Create a new blog post"
)
def create_post(
    data: PostCreate,
    current_user: User = Depends(
        get_current_user
    ),
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

    return ok(
    data = PostResponse.model_validate(post),
    message="Post created successfully"
)

#List All Post
@router.get(
    "/",
    summary = "List posts",
    description = """
    Retrieve posts with:
    - Pagination
    - Filtering
    - Searching
    - Sorting
    """
)
@limiter.limit("100/minute")
async def list_posts(
    request: Request,
    page: int = 1,
    limit: int = 100,
    author: str = None,
    category: str = None,
    published: bool = None,
    search: str = None,
    sort:   str = "created_at",
    db: Session = Depends(get_db)
):
    cache_key = (
        f"posts:"
        f"{page}:"
        f"{limit}:"
        f"{author}:"
        f"{category}:"
        f"{published}:"
        f"{search}:"
        f"{sort}"
    )

    cached = cache_get(cache_key)

    if cached:
        print("CACHE HIT")
        return cached

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

    result = {
        "page": page,
        "limit": limit,
        "total": total,
        "data": [
            {
                "id": p.id,
                "title": p.title,
                "content": p.content,
                "category": p.category,
                "published": p.published,
                "author_id": p.author_id
            }
            for p in posts
        ]
    }
    cache_set(
        cache_key,
        result
    )
    print("CACHE MISS")

    return ok(result)

#Get Post By ID
@router.get(
    "/{post_id}",
    response_model = APIResponse,
    summary = "Get post by ID",
    description = "Retrieve a specific post by ID"
)
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    post = db.get(Post, post_id)

    if not post:
        raise HTTPException(
            status_code = 404,
            detail = "Post not found"
        )

    return ok(
        data = PostResponse.model_validate(post).model_dump()
    )

# UPDATE POST
@router.put(
    "/{post_id}",
    response_model = APIResponse,
    summary = "Update post",
    description = "Update an existing post"
)
def update_post(
    post_id: int,
    data: PostUpdate,
    db: Session = Depends(get_db)
):
    post = db.get(Post, post_id)

    if not post:
        raise HTTPException(
            status_code = 404,
            detail = "Post not found"
        )

    for k, v in data.model_dump(
        exclude_none = True
    ).items():
        setattr(post, k, v)

    db.commit()
    db.refresh(post)

    return ok(
        data = PostResponse.model_validate(post).model_dump(),
        message = "Post updated successfully"
    )    
    
#Ex.11
#Delete Post
@router.delete(
    "/{post_id}",
    status_code = 204,
    summary = "Delete post",
    description = "Delete a post (Admin only)"
)
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
    
    clear_posts_cache
    return ok(
        message = "Post deleted successfully"
    )