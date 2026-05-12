from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5)
    priority: str
    assigned_to: int


class TaskUpdate(BaseModel):

    title: str
    description: str
    priority: str
    status: str
