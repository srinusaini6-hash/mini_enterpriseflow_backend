from datetime import datetime
from pydantic import BaseModel


class ReminderCreate(BaseModel):
    reminder_time: datetime


class ReminderStatusUpdate(BaseModel):
    status: str