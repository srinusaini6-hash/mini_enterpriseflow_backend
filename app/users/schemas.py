from pydantic import (
    BaseModel,
    EmailStr
)

from datetime import datetime
from typing import Optional


# ---------------- CREATE USER ----------------

class UserCreate(BaseModel):

    name: str
    email: EmailStr
    password: str
    role: str
    tenant_id: int


# ---------------- USER RESPONSE ----------------

class UserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    role: str
    tenant_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True