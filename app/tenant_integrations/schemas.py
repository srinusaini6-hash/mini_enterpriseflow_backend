from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# -----------------------------
# Create Schema
# -----------------------------
class TenantIntegrationCreate(BaseModel):
    tenant_id: int
    provider_id: int
    integration_name: str
    status: str = "CONNECTED"
    config_json: Optional[dict] = None
    connected_by: int


# -----------------------------
# Update Schema
# -----------------------------
class TenantIntegrationUpdate(BaseModel):
    integration_name: Optional[str] = None
    status: Optional[str] = None
    config_json: Optional[dict] = None
    last_sync_at: Optional[datetime] = None


# -----------------------------
# Response Schema
# -----------------------------
class TenantIntegrationResponse(BaseModel):
    id: int
    tenant_id: int
    provider_id: int
    integration_name: str
    status: str
    config_json: Optional[dict]
    connected_by: int
    connected_at: datetime
    last_sync_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)