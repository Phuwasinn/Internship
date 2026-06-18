from typing import Generator
from sqlalchemy.orm import Session
from .database import SessionLocal

#Ex.5
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db        
    finally:
        db.close()      