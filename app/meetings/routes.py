from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.meetings.schemas import (
    MeetingCreate,
    MeetingUpdate
)

from app.meetings.service import MeetingService

router = APIRouter(
    prefix="/meetings",
    tags=["Meetings"]
)


@router.post("/")
def create_meeting(
    payload: MeetingCreate,
    db: Session = Depends(get_db)
):
    current_user = {"id": 1, "tenant_id": 1}

    return MeetingService.create_meeting(
        db=db,
        payload=payload,
        current_user=current_user
    )


@router.get("/")
def list_meetings(
    db: Session = Depends(get_db)
):
    current_user = {"tenant_id": 1}

    return MeetingService.list_meetings(
        db=db,
        tenant_id=current_user["tenant_id"]
    )


@router.get("/{meeting_id}")
def get_meeting(
    meeting_id: int,
    db: Session = Depends(get_db)
):
    current_user = {"tenant_id": 1}

    return MeetingService.get_meeting(
        db=db,
        meeting_id=meeting_id,
        tenant_id=current_user["tenant_id"]
    )


@router.put("/{meeting_id}")
def update_meeting(
    meeting_id: int,
    payload: MeetingUpdate,
    db: Session = Depends(get_db)
):
    current_user = {"tenant_id": 1}

    return MeetingService.update_meeting(
        db=db,
        meeting_id=meeting_id,
        payload=payload,
        tenant_id=current_user["tenant_id"]
    )


@router.patch("/{meeting_id}/cancel")
def cancel_meeting(
    meeting_id: int,
    db: Session = Depends(get_db)
):
    current_user = {"tenant_id": 1}

    return MeetingService.cancel_meeting(
        db=db,
        meeting_id=meeting_id,
        tenant_id=current_user["tenant_id"]
    )


@router.patch("/{meeting_id}/complete")
def complete_meeting(
    meeting_id: int,
    db: Session = Depends(get_db)
):
    current_user = {"tenant_id": 1}

    return MeetingService.complete_meeting(
        db=db,
        meeting_id=meeting_id,
        tenant_id=current_user["tenant_id"]
    )