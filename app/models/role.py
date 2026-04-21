from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    can_invite = Column(Boolean, default=False)
    can_delete = Column(Boolean, default=False)
    can_edit = Column(Boolean, default=False)

    #relaciones

    memberships = relationship("Membership", back_populates="role") 
