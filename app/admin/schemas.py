from datetime import datetime

from pydantic import (
    BaseModel,
    Field
)


# ---------------- CREATE DEPARTMENT ----------------

class DepartmentCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )


# ---------------- DEPARTMENT RESPONSE ----------------

class DepartmentResponse(BaseModel):

    id: int
    name: str
    description: str | None
    created_at: datetime

    class Config:

        from_attributes = True


# ---------------- USER RESPONSE ----------------

class UserResponse(BaseModel):

    id: int
    name: str
    email: str
    role: str
    tenant_id: int | None
    created_at: datetime

    class Config:

        from_attributes = True


# ---------------- AUDIT LOG RESPONSE ----------------

class AuditLogResponse(BaseModel):

    id: int
    module_name: str
    action_type: str
    record_id: int | None
    old_data: str | None
    new_data: str | None
    ip_address: str | None
    user_agent: str | None
    created_at: datetime

    class Config:

        from_attributes = True