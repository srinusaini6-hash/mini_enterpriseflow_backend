from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict
)


# ---------------- CREATE TENANT SCHEMA ----------------

class TenantCreate(BaseModel):

    name: str

    slug: str

    contact_email: EmailStr

    phone: Optional[str] = None

    address: Optional[str] = None

    industry: Optional[str] = None


# ---------------- RESPONSE TENANT SCHEMA ----------------

class TenantResponse(BaseModel):

    id: int

    name: str

    slug: str

    contact_email: EmailStr

    phone: Optional[str] = None

    address: Optional[str] = None

    industry: Optional[str] = None

    status: str

    model_config = ConfigDict(
        from_attributes=True
    )