from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ---------------------------------------------------------
# Base Schema
# ---------------------------------------------------------
class IntegrationCredentialBase(BaseModel):
    tenant_id: int
    integration_id: int
    access_token: str
    refresh_token: Optional[str] = None
    api_key: Optional[str] = None
    expires_at: Optional[datetime] = None


# ---------------------------------------------------------
# Create Schema
# ---------------------------------------------------------
class IntegrationCredentialCreate(IntegrationCredentialBase):
    pass


# ---------------------------------------------------------
# Update Schema
# ---------------------------------------------------------
class IntegrationCredentialUpdate(BaseModel):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    api_key: Optional[str] = None
    expires_at: Optional[datetime] = None


# ---------------------------------------------------------
# Response Schema
# ---------------------------------------------------------
class IntegrationCredentialResponse(IntegrationCredentialBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)