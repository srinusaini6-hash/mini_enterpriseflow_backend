from pydantic import BaseModel


class WorkflowStepCreate(BaseModel):
    step_order: int
    approver_role: str
    step_name: str
    is_required: bool = True


class WorkflowStepUpdate(BaseModel):
    step_order: int
    approver_role: str
    step_name: str
    is_required: bool


class WorkflowStepResponse(BaseModel):
    id: int
    workflow_template_id: int
    step_order: int
    approver_role: str
    step_name: str
    is_required: bool

    class Config:
        from_attributes = True