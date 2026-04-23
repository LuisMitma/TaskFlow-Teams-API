from sqlalchemy import Column, String,Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone
import uuid

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"),nullable=False)
    assigned_to_id = Column(UUID(as_uuid=True), ForeignKey("users.id"),nullable=False)
    status_id = Column(Integer, ForeignKey("tasks_statuses.id"),nullable=False)
    priority_id = Column(Integer, ForeignKey("task_priorities.id"),nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    #relaciones

    assigned_to = relationship("User", back_populates="assigned_tasks")
    project = relationship("Project", back_populates="tasks")
    status = relationship("TaskStatus", back_populates="tasks")
    priority = relationship("TaskPriority", back_populates="tasks")