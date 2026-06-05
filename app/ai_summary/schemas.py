from pydantic import BaseModel
from typing import List


class SummaryRequest(BaseModel):
    notes: List[str]


class SummaryResponse(BaseModel):
    meeting_id: int
    summary: str
    decisions: List[str]
    action_items: List[str]
    suggested_owners: List[str]


class SummaryDBResponse(BaseModel):
    id: int
    meeting_id: int
    summary: str
    decisions: str | None = None
    action_items: str | None = None
    suggested_owners: str | None = None

    class Config:
        from_attributes = True