from sqlalchemy import select

from app.meetings.models import Meeting
from app.meeting_attendees.models import MeetingAttendee


class AvailabilityService:

    @staticmethod
    def check_availability(
        db,
        user_ids: list[int],
        start_time,
        end_time
    ):

        conflicts = []

        for user_id in user_ids:

            meetings = db.scalars(
                select(Meeting)
                .join(
                    MeetingAttendee,
                    Meeting.id == MeetingAttendee.meeting_id
                )
                .where(
                    MeetingAttendee.user_id == user_id,
                    Meeting.start_time < end_time,
                    Meeting.end_time > start_time
                )
            ).all()

            for meeting in meetings:
                conflicts.append({
                    "user_id": user_id,
                    "meeting_id": meeting.id,
                    "meeting_title": meeting.title,
                    "reason": "Meeting overlap"
                })

        return {
            "available": len(conflicts) == 0,
            "conflicts": conflicts
        }