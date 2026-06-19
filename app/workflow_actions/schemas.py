from pydantic import BaseModel


class WorkflowActionResponse(BaseModel):
    message: str