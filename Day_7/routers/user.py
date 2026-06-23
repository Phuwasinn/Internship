from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload, selectinload
from ..models import User
from ..schemas import UserCreate, UserUpdate, ok, APIResponse, PostResponse, UserResponse
from ..dependencies import get_db
from ..auth import hash_password

router = APIRouter(prefix="/users", tags=["Users"])

#Ex.3
#Create 
@router.post(
    "/",
    response_model = APIResponse,
    status_code = 201,
    summary = "Create user",
    description = "Create a new user account",
    response_description = "Created user"
)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username = data.username,
        email = data.email,
        password = hash_password(data.password),
        role = data.role
    )
    db.add(user)    
    db.commit()      
    db.refresh(user)  
    
    return ok(
    data = UserResponse.model_validate(user).model_dump(),
    message = "User created successfully"
)
    
#Get All User
@router.get(
    "/",
    response_model = APIResponse,
    summary = "Get all users",
    description = "Retrieve all users from database"
)
def list_users(db: Session = Depends(get_db)):
    users = (
        db.query(User)
        .options(selectinload(User.posts))
        .all()
    )
    return ok(
    data = [
        UserResponse.model_validate(user).model_dump()
        for user in users
    ]
)
    
#Update User
@router.put(
    "/{user_id}",
    response_model = APIResponse,
    summary = "Update user",
    description = "Update username or email"
)
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
  
    return ok(
    data = UserResponse.model_validate(user).model_dump(),
    message = "User updated successfully"
)
    
#Delete User
@router.delete(
    "/{user_id}",
    status_code = 200,
    summary = "Delete user",
    description = "Delete a user by ID"
)
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)
    if not user: 
        raise HTTPException(404, "Not found")
    db.delete(user)
    db.commit()
   
    return ok(
        message = "User deleted successfully"
    )    
    
#Ex.4 --> Ex.18
#Get User's Posts
@router.get(
    "/{user_id}/posts",
    response_model = APIResponse,
    summary = "Get user's posts",
    description = "Retrieve all posts created by a specific user"
)
def get_user_posts(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .options(joinedload(User.posts))
        .filter(User.id == user_id)
        .first()
    )
    if not user:
        raise HTTPException(404, "User not found")

    posts = [
        PostResponse.model_validate(post).model_dump()
        for post in user.posts
    ]

    return ok(data = posts)