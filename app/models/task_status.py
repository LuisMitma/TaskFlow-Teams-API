from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base


class TaskStatus(Base):
    __tablename__ = "tasks_statuses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    order = Column(Integer, nullable=False)

    #relacion

    tasks = relationship("Task", back_populates="status")

