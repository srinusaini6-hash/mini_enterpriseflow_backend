from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.meeting_attendees.schemas import (
    AttendeeCreate,
    MeetingResponseUpdate
)

from app.meeting_attendees.service import (
    MeetingAttendeeService
)

router = APIRouter(
    prefix="/meetings",
    tags=["Meeting Attendees"]
)

@router.post("/{meeting_id}/attendees")
def add_attendees(
    meeting_id: int,
    payload: AttendeeCreate,
    db: Session = Depends(get_db)
):

    return MeetingAttendeeService.add_attendees(
        db,
        meeting_id,
        payload.user_ids
    )

@router.get("/{meeting_id}/attendees")
def get_attendees(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    return MeetingAttendeeService.get_attendees(
        db,
        meeting_id
    )

@router.delete("/{meeting_id}/attendees/{user_id}")
def remove_attendee(
    meeting_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):

    return MeetingAttendeeService.remove_attendee(
        db,
        meeting_id,
        user_id
    )

@router.patch("/{meeting_id}/respond")
def respond_invitation(
    meeting_id: int,
    payload: MeetingResponseUpdate,
    db: Session = Depends(get_db)
):

    user_id = 1

    return MeetingAttendeeService.respond_invitation(
        db,
        meeting_id,
        user_id,
        payload.response_status
    )

