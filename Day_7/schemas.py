from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

# USER
class UserCreate(BaseModel):
    username: str = Field(
        examples=["Alice"]
    )
    email: str = Field(
        examples=["alice@test.com"]
    )
    password: str = Field(
        examples=["secret123"]
    )
    role: str = Field(
        default="user",
        examples=["admin"]
    )

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True

# POST
class PostCreate(BaseModel):
    title: str = Field(
        examples=["My First Post"]
    )
    content: str = Field(
        examples=["Hellooo"]
    )
    category: str = Field(
        default="general",
        examples=["python"]
    )
    published: bool = Field(
        default=True,
        examples=[True]
    )
    author_id: int = Field(
        examples=[1]
    )
    
class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    published: Optional[bool] = None
    

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    published: bool
    author_id: int

    class Config:
        from_attributes = True


#Ex.19
# RESPONSE
class APIResponse(BaseModel):
    success: bool
    message: str
    data: Any = None

def ok(data = None, message = "Success"):
    return APIResponse(
        success = True,
        message = message,
        data = data
    )

def err(message = "Error"):
    return APIResponse(
        success = False,
        message = message
    )