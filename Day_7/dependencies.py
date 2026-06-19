from typing import Generator
from sqlalchemy.orm import Session
from .database import SessionLocal
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .auth import SECRET_KEY, ALGORITHM
from .models import User

#Ex.5
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db        
    finally:
        db.close()      

#Ex.10        
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl = "login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )
        user_id = int(payload["sub"])
        
    except JWTError:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid token"
        )
    user = db.get(User, user_id)
    
    if not user:
        raise HTTPException(
            status_code = 401,
            detail = "User not found"
        )

    return user

#Ex.11
def require_role(role: str):
    def checker(
        current_user: User = Depends(
            get_current_user
        )
    ):
        if current_user.role != role:
            raise HTTPException(
                status_code = 403,
                detail = "Forbidden"
            )
        return current_user

    return checker