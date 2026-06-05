from pydantic import BaseModel


class MeetingNoteCreate(BaseModel):
    note: str
    author_id: int


class MeetingNoteUpdate(BaseModel):
    note: str
    updated_by: int