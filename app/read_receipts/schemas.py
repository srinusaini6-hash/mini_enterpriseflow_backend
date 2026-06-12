from pydantic import BaseModel
from datetime import datetime


class ReadReceiptCreate(BaseModel):
    user_id: int


class ReadReceiptResponse(BaseModel):
    id: int
    message_id: int
    user_id: int
    read_at: datetime

    class Config:
        from_attributes = True