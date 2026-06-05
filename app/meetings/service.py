from sqlalchemy import select

from app.meetings.models import Meeting


class MeetingService:

    @staticmethod
    def create_meeting(
        db,
        payload,
        current_user
    ):

        meeting = Meeting(
            tenant_id=current_user["tenant_id"],
            title=payload.title,
            description=payload.description,
            meeting_type=payload.meeting_type,
            start_time=payload.start_time,
            end_time=payload.end_time,
            location=payload.location,
            meeting_link=payload.meeting_link,
            created_by=current_user["id"]
        )

        db.add(meeting)
        db.commit()
        db.refresh(meeting)

        return meeting

    @staticmethod
    def list_meetings(
        db,
        tenant_id
    ):
        return db.scalars(
            select(Meeting).where(
                Meeting.tenant_id == tenant_id
            )
        ).all()

    @staticmethod
    def get_meeting(
        db,
        meeting_id,
        tenant_id
    ):
        return db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id,
                Meeting.tenant_id == tenant_id
            )
        )

    @staticmethod
    def update_meeting(
        db,
        meeting_id,
        payload,
        tenant_id
    ):

        meeting = db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id,
                Meeting.tenant_id == tenant_id
            )
        )

        if not meeting:
            return {"message": "Meeting not found"}

        meeting.title = payload.title
        meeting.description = payload.description
        meeting.meeting_type = payload.meeting_type
        meeting.start_time = payload.start_time
        meeting.end_time = payload.end_time
        meeting.location = payload.location
        meeting.meeting_link = payload.meeting_link

        db.commit()
        db.refresh(meeting)

        return meeting

    @staticmethod
    def cancel_meeting(
        db,
        meeting_id,
        tenant_id
    ):

        meeting = db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id,
                Meeting.tenant_id == tenant_id
            )
        )

        if not meeting:
            return {"message": "Meeting not found"}

        meeting.status = "CANCELLED"

        db.commit()

        return {
            "message": "Meeting cancelled successfully"
        }

    @staticmethod
    def complete_meeting(
        db,
        meeting_id,
        tenant_id
    ):

        meeting = db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id,
                Meeting.tenant_id == tenant_id
            )
        )

        if not meeting:
            return {"message": "Meeting not found"}

        meeting.status = "COMPLETED"

        db.commit()

        return {
            "message": "Meeting completed successfully"
        }