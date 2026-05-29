from pydantic import BaseModel

from datetime import datetime


class RolePermissionCreate(BaseModel):

    role_id: int

    permission_id: int


class RolePermissionResponse(BaseModel):

    id: int

    role_id: int

    permission_id: int

    created_at: datetime

    class Config:

        from_attributes = True