from pydantic import BaseModel

from typing import Optional

from datetime import datetime


class PermissionCreate(BaseModel):

    name: str

    description: Optional[str] = None


class PermissionResponse(BaseModel):

    id: int

    name: str

    description: Optional[str]

    created_at: datetime

    class Config:

        from_attributes = True