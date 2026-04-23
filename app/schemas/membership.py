from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseMembership(BaseModel):
    workspace_id: UUID
    user_id: UUID
