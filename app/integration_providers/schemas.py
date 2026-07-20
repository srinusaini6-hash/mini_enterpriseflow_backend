from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# -----------------------------
# Create Integration Provider
# -----------------------------
class IntegrationProviderCreate(BaseModel):
    name: str
    provider_code: str
    provider_type: str
    auth_type: str
    base_url: Optional[str] = None


# -----------------------------
# Update Integration Provider
# -----------------------------
class IntegrationProviderUpdate(BaseModel):
    name: Optional[str] = None
    provider_code: Optional[str] = None
    provider_type: Optional[str] = None
    auth_type: Optional[str] = None
    base_url: Optional[str] = None
    is_active: Optional[bool] = None


# -----------------------------
# Disable Provider
# -----------------------------
class IntegrationProviderDisable(BaseModel):
    is_active: bool = False


# -----------------------------
# Response Schema
# -----------------------------
class IntegrationProviderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    provider_code: str
    provider_type: str
    auth_type: str
    base_url: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime


# -----------------------------
# Generic Success Response
# -----------------------------
class IntegrationProviderMessage(BaseModel):
    success: bool
    message: str


# -----------------------------
# List Response
# -----------------------------
class IntegrationProviderListResponse(BaseModel):
    success: bool
    message: str
    data: list[IntegrationProviderResponse]