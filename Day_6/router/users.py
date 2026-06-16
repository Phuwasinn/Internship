from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, EmailStr, field_validator

router = APIRouter(prefix="/users", tags=["Users"])

#Ex.4 
@router.get("")
def get_users(limit: int = 10, offset: int = 0):
    return {
        "limit": limit,
        "offset": offset
    }

#Ex.3
@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    return {"user_id": user_id}

#Ex.5 
class User(BaseModel):
    name: str
    age: int

@router.post("/create", status_code=201)
def create_user(user: User):
    return {
        "message": "User created", 
        "name": user.name, 
        "age": user.age
    }
    
#Ex.6
class ValidatedUser(BaseModel):
    name:  str
    email: EmailStr
    age:   int
    
    #Ex.7
    @field_validator("name")
    @classmethod
    def name_min_len(cls, v):
        if len(v) < 3:
            raise ValueError("Name must be at least 3 characters")
        return v
    
    @field_validator("age")
    @classmethod
    def age_range(cls, v):
        if not (18 <= v <= 100):
            raise ValueError("Age must be between 18 - 100")
        return v

@router.post("/validated", status_code=201)
def create_validated_user(user: ValidatedUser):
    return user