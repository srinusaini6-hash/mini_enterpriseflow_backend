from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.ai_summary.schemas import (
    SummaryRequest
)

from app.ai_summary.service import (
    AISummaryService
)

router = APIRouter(
    prefix="/ai-summary",
    tags=["AI Meeting Summary"]
)


@router.post("/{meeting_id}")
def generate_summary(
    meeting_id: int,
    payload: SummaryRequest,
    db: Session = Depends(get_db)
):

    return AISummaryService.generate_summary(
        db=db,
        meeting_id=meeting_id,
        notes=payload.notes
    )


@router.get("/{meeting_id}")
def get_summary(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    return AISummaryService.get_summary(
        db=db,
        meeting_id=meeting_id
    )