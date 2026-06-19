from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models import User
from ..dependencies import get_db
from ..auth import verify_password, create_access_token

router = APIRouter(tags=["Authentication"])

@router.post("/login")
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