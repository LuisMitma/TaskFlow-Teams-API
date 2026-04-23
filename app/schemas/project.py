from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseProject(BaseModel):

    name: str
    description: Optional[str] = None