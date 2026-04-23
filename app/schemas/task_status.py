from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class BaseTaskStatus(BaseModel):
    name: str
    order: int