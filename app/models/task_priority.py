from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class TaskPriority(Base):
    __tablename__ = "task_priorities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    level = Column(Integer, unique=True, nullable=False)

    #relaciones 

    tasks = relationship("Task", back_populates="priority")