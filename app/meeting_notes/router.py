from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.meeting_notes.schemas import (
    MeetingNoteCreate,
    MeetingNoteUpdate
)

from app.meeting_notes.service import (
    MeetingNoteService
)

router = APIRouter(
    prefix="/meeting-notes",
    tags=["Meeting Notes"]
)


@router.post("/{meeting_id}")
def add_note(
    meeting_id: int,
    payload: MeetingNoteCreate,
    db: Session = Depends(get_db)
):

    return MeetingNoteService.add_note(
        db=db,
        meeting_id=meeting_id,
        note=payload.note,
        author_id=payload.author_id
    )


@router.get("/{meeting_id}")
def get_notes(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    return MeetingNoteService.get_notes(
        db=db,
        meeting_id=meeting_id
    )


@router.patch("/{note_id}")
def update_note(
    note_id: int,
    payload: MeetingNoteUpdate,
    db: Session = Depends(get_db)
):

    return MeetingNoteService.update_note(
        db=db,
        note_id=note_id,
        note=payload.note,
        updated_by=payload.updated_by
    )


@router.get("/history/{note_id}")
def get_history(
    note_id: int,
    db: Session = Depends(get_db)
):

    return MeetingNoteService.get_history(
        db=db,
        note_id=note_id
    )