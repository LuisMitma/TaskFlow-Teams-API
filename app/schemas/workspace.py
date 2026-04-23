from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseWorkspace(BaseModel):
    name: str
    owner_id: UUID