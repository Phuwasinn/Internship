from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
 
 #Ex.2   
class User(Base):
    __tablename__ = "users"
    id         = Column(Integer, primary_key = True, index = True)
    username   = Column(String, unique = True, nullable = False)
    email      = Column(String, unique = True, nullable = False)
    password   = Column(String, nullable = False)
    role       = Column(String, default = "user")  
    created_at = Column(DateTime, default = datetime.utcnow)

    posts = relationship("Post", back_populates = "author",
                        cascade = "all, delete-orphan")
    
class Post(Base):
    __tablename__ = "posts"
    id         = Column(Integer, primary_key = True, index = True)
    title      = Column(String, nullable = False)
    content    = Column(String, nullable = False)
    category   = Column(String, default = "general")
    published  = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.utcnow)
    author_id  = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")