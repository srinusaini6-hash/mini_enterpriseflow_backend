from pydantic import BaseModel
from datetime import datetime


class NotificationCreate(BaseModel):
    execution_id: int
    user_name: str
    message: str


class NotificationResponse(BaseModel):
    id: int
    execution_id: int
    user_name: str
    message: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True