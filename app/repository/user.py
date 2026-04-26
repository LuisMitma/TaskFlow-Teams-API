from sqlalchemy.orm import Session
from typing import Optional

from app.models.user import User
from uuid import UUID

def get_user(db: Session, user_id: UUID) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def get_existing_user(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()
