from pydantic import BaseModel

from typing import Optional

from datetime import datetime


# ---------------- CREATE ROLE ----------------

class RoleCreate(BaseModel):

    name: str

    description: Optional[str] = None


# ---------------- RESPONSE ROLE ----------------

class RoleResponse(BaseModel):

    id: int

    name: str

    description: Optional[str]

    created_at: datetime

    class Config:

        from_attributes = True