

from pydantic import BaseModel

class WorkflowTemplateCreate(BaseModel):
 tenant_id: int
 name: str
 description: str
 module_name: str

class WorkflowTemplateUpdate(BaseModel):
 tenant_id: int
 name: str
 description: str
 module_name: str
 is_active: bool

class WorkflowTemplateResponse(BaseModel):
 id: int
 tenant_id: int
 name: str
 description: str
 module_name: str
 is_active: bool


class Config:
    from_attributes = True

