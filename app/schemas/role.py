from pydantic import BaseModel
from uuid import UUID

class BaseRole(BaseModel):
    name: str
    can_invite: bool
    can_delete: bool
    can_edit: bool