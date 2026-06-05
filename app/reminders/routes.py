from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.reminders.schemas import (
    ReminderCreate,
    ReminderStatusUpdate
)

from app.reminders.service import (
    ReminderService
)

router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"]
)


@router.post("/{meeting_id}")
def create_reminder(
    meeting_id: int,
    payload: ReminderCreate,
    db: Session = Depends(get_db)
):

    return ReminderService.create_reminder(
        db=db,
        meeting_id=meeting_id,
        reminder_time=payload.reminder_time
    )


@router.get("/{meeting_id}")
def get_reminders(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    return ReminderService.get_reminders(
        db=db,
        meeting_id=meeting_id
    )


@router.patch("/{reminder_id}/status")
def update_status(
    reminder_id: int,
    payload: ReminderStatusUpdate,
    db: Session = Depends(get_db)
):

    return ReminderService.update_status(
        db=db,
        reminder_id=reminder_id,
        status=payload.status
    )


@router.get("/history/{meeting_id}")
def get_history(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    return ReminderService.get_history(
        db=db,
        meeting_id=meeting_id
    )