from typing import Optional

from pydantic import (
    BaseModel,
    Field
)


# ---------------- CREATE TASK ----------------

class TaskCreate(BaseModel):

    title: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    description: str = Field(
        ...,
        min_length=5
    )

    priority: str

    assigned_to: int


# ---------------- UPDATE TASK ----------------

class TaskUpdate(BaseModel):

    title: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100
    )

    description: Optional[str] = Field(
        None,
        min_length=5
    )

    priority: Optional[str] = None

    status: Optional[str] = None


# ---------------- TASK RESPONSE ----------------

class TaskResponse(BaseModel):

    id: int

    title: str

    description: str

    priority: str

    status: str

    assigned_to: int

    created_by: int

    class Config:

        from_attributes = True