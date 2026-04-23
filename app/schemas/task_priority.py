from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class BaseTaskPriority(BaseModel):
    name: str
    level: int