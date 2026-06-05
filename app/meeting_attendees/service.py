from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import select

from app.meeting_attendees.models import MeetingAttendee
from app.meetings.models import Meeting


class MeetingAttendeeService:

    @staticmethod
    def add_attendees(
        db,
        meeting_id: int,
        user_ids: list[int]
    ):

        meeting = db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id
            )
        )

        if not meeting:
            raise HTTPException(
                status_code=404,
                detail="Meeting not found"
            )

        attendees = []

        for user_id in user_ids:

            existing = db.scalar(
                select(MeetingAttendee).where(
                    MeetingAttendee.meeting_id == meeting_id,
                    MeetingAttendee.user_id == user_id
                )
            )

            if existing:
                continue

            attendee = MeetingAttendee(
                meeting_id=meeting_id,
                user_id=user_id,
                response_status="PENDING"
            )

            db.add(attendee)
            attendees.append(attendee)

        db.commit()

        for attendee in attendees:
            db.refresh(attendee)

        return attendees

    @staticmethod
    def get_attendees(
        db,
        meeting_id: int
    ):

        meeting = db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id
            )
        )

        if not meeting:
            raise HTTPException(
                status_code=404,
                detail="Meeting not found"
            )

        attendees = db.scalars(
            select(MeetingAttendee).where(
                MeetingAttendee.meeting_id == meeting_id
            )
        ).all()

        return attendees

    @staticmethod
    def remove_attendee(
        db,
        meeting_id: int,
        user_id: int
    ):

        attendee = db.scalar(
            select(MeetingAttendee).where(
                MeetingAttendee.meeting_id == meeting_id,
                MeetingAttendee.user_id == user_id
            )
        )

        if not attendee:
            raise HTTPException(
                status_code=404,
                detail="Attendee not found"
            )

        db.delete(attendee)
        db.commit()

        return {
            "message": "Attendee removed successfully"
        }

    @staticmethod
    def respond_invitation(
        db,
        meeting_id: int,
        user_id: int,
        response_status: str
    ):

        attendee = db.scalar(
            select(MeetingAttendee).where(
                MeetingAttendee.meeting_id == meeting_id,
                MeetingAttendee.user_id == user_id
            )
        )

        if not attendee:
            raise HTTPException(
                status_code=404,
                detail="Invitation not found"
            )

        attendee.response_status = response_status
        attendee.responded_at = datetime.utcnow()

        db.commit()
        db.refresh(attendee)

        return attendee