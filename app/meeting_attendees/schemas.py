from pydantic import BaseModel
from typing import List


class AttendeeCreate(BaseModel):
    user_ids: List[int]


class AttendeeResponse(BaseModel):
    id: int
    meeting_id: int
    user_id: int
    response_status: str

    class Config:
        from_attributes = True


class MeetingResponseUpdate(BaseModel):
    response_status: str