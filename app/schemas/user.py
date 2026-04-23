from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseUser(BaseModel):
    name: str
    email: EmailStr
