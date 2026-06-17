from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

#Ex.13
router = APIRouter(prefix="/users", tags=["Users"])

#Ex.4 
@router.get("")
def get_users(limit: int = 10, offset: int = 0):
    return {
        "limit": limit,
        "offset": offset
    }

#Ex.3 --> Ex.10
FAKE_USERS = {1: "A", 2: "B"}

@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    if user_id not in FAKE_USERS:
        raise HTTPException(status_code = 404, detail = "User not found")
    return {"user_id": user_id, "name": FAKE_USERS[user_id]}

#Ex.5 --> Ex.8,9
class User(BaseModel):
    id: int 
    username: str 
    age: int
    password: str

@router.post("/create", status_code = status.HTTP_201_CREATED)
def create_user(user: User):
    return {
        "message": f"User {user.username} created", 
        "id": user.id,
        "username": user.username, 
        "age": user.age,
        "password": user.password
    }

@router.delete("/{user_id}/delete", status_code = status.HTTP_204_NO_CONTENT) 
def delete_user_204(user_id: int):
   return 

#Ex.6
class ValidatedUser(BaseModel):
    name: str
    email: EmailStr
    age: int
    
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

#Ex.8
class UserPublic(BaseModel):
   id: int
   username: str
   age: int

@router.get("/admin/profile", response_model=UserPublic)
def get_admin_profile():
   internal = User(id = 1, username = "admin", age = 30 , password = "123456")
   return internal

#Ex.20
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    age: int
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

_db: dict[int, dict] = {}
_next_id = 1

@router.post("/crud/", response_model = UserOut, status_code=201)
def crud_create(user: ValidatedUser):
    global _next_id
    record = {"id": _next_id, **user.model_dump()}
    _db[_next_id] = record; _next_id += 1
    return record

@router.get("/crud/", response_model = list[UserOut])
def crud_list():
    return list(_db.values())

@router.get("/crud/{user_id}", response_model = UserOut)
def crud_get(user_id: int):
    if user_id not in _db:
        raise HTTPException(404, "User not found")
    return _db[user_id]

@router.put("/crud/{user_id}", response_model = UserOut)
def crud_update(user_id: int, update: UserUpdate):
    if user_id not in _db:
        raise HTTPException(404, "User not found")
    _db[user_id].update({k: v for k, v in update.model_dump().items() if v is not None})
    return _db[user_id]

@router.delete("/crud/{user_id}", status_code = 204)
def crud_delete(user_id: int):
    if user_id not in _db:
        raise HTTPException(404, "User not found")
    del _db[user_id]