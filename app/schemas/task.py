from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseTask(BaseModel):
    title: str
    description: Optional[str] = None
    