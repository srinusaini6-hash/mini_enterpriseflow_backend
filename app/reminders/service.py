from sqlalchemy import select

from app.reminders.models import MeetingReminder


class ReminderService:

    @staticmethod
    def create_reminder(
        db,
        meeting_id,
        reminder_time
    ):

        reminder = MeetingReminder(
            meeting_id=meeting_id,
            reminder_time=reminder_time
        )

        db.add(reminder)
        db.commit()
        db.refresh(reminder)

        return reminder

    @staticmethod
    def get_reminders(
        db,
        meeting_id
    ):

        return db.scalars(
            select(MeetingReminder)
            .where(
                MeetingReminder.meeting_id == meeting_id
            )
        ).all()

    @staticmethod
    def update_status(
        db,
        reminder_id,
        status
    ):

        reminder = db.get(
            MeetingReminder,
            reminder_id
        )

        reminder.status = status

        db.commit()
        db.refresh(reminder)

        return reminder

    @staticmethod
    def get_history(
        db,
        meeting_id
    ):

        return db.scalars(
            select(MeetingReminder)
            .where(
                MeetingReminder.meeting_id == meeting_id
            )
        ).all()