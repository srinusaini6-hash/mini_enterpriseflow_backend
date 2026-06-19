from pydantic import BaseModel


class WorkflowConditionCreate(BaseModel):
    field_name: str
    operator: str
    value: str


class WorkflowConditionUpdate(BaseModel):
    field_name: str
    operator: str
    value: str


class WorkflowConditionResponse(BaseModel):
    id: int
    workflow_template_id: int
    field_name: str
    operator: str
    value: str

    class Config:
        from_attributes = True