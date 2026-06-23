from datetime import datetime

from pydantic import BaseModel


class KnowledgeCategoryCreate(BaseModel):
    tenant_id: int
    name: str
    description: str
    created_by: int


class KnowledgeCategoryUpdate(BaseModel):
    name: str
    description: str
    is_active: bool


class KnowledgeCategoryResponse(BaseModel):
    id: int
    tenant_id: int
    name: str
    description: str
    is_active: bool
    created_by: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True