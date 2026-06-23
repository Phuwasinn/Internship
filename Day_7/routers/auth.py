from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models import User, Post
from ..dependencies import get_db
from ..auth import verify_password, create_access_token
from ..schemas import UserCreate, UserUpdate, ok
from ..auth import hash_password

router = APIRouter(prefix = "/auth", tags = ["Authentication"])

#REGISTER
@router.post("/register", status_code = 201)
def register(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.username == data.username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code = 400,
            detail = "Username already exists"
        )
    try:
        user = User(
        username = data.username,
        email = data.email,
        password = hash_password(data.password),
        role = data.role
        )
        db.add(user)
        db.flush()  

        welcome_post = Post(
            title = f"Welcome, {user.username}!",
            content = "This is your first post",
            author_id = user.id
        )
        db.add(welcome_post)

        db.commit()

        db.refresh(user)
        return user

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code = 500,
            detail = f"Registration failed: {str(e)}"
        )

#LOGIN
@router.post(
    "/login",
    summary = "Login",
    description = "Authenticate user and return JWT access token"
)
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.username == form.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid credentials"
        )
    if not verify_password(
        form.password,
        user.password
    ):
        raise HTTPException(
            status_code = 401,
            detail = "Invalid credentials"
        )
    token = create_access_token(user)

    return {
    "access_token": token,
    "token_type": "bearer"
}