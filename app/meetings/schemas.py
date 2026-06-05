from datetime import datetime
from pydantic import BaseModel


class MeetingCreate(BaseModel):
    title: str
    description: str | None = None
    meeting_type: str
    start_time: datetime
    end_time: datetime
    location: str | None = None
    meeting_link: str | None = None


class MeetingUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    meeting_type: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    location: str | None = None
    meeting_link: str | None = None
    status: str | None = None


class MeetingResponse(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        from_attributes = True