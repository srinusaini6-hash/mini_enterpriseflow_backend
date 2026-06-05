from datetime import date

from pydantic import BaseModel


class ActionItemCreate(BaseModel):
    title: str
    owner_id: int
    due_date: date


class ConvertToTaskRequest(BaseModel):
    task_id: int