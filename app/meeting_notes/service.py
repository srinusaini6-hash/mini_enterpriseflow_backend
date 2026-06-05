from sqlalchemy import select

from app.meeting_notes.models import MeetingNote
from app.meeting_notes.history_model import MeetingNoteHistory
from app.meetings.models import Meeting


class MeetingNoteService:

    @staticmethod
    def add_note(
        db,
        meeting_id: int,
        note: str,
        author_id: int
    ):

        meeting = db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id
            )
        )

        if not meeting:
            raise Exception("Meeting not found")

        meeting_note = MeetingNote(
            meeting_id=meeting_id,
            note=note,
            author_id=author_id
        )

        db.add(meeting_note)
        db.commit()
        db.refresh(meeting_note)

        return meeting_note

    @staticmethod
    def get_notes(
        db,
        meeting_id: int
    ):

        return db.scalars(
            select(MeetingNote).where(
                MeetingNote.meeting_id == meeting_id
            )
        ).all()

    @staticmethod
    def update_note(
        db,
        note_id: int,
        note: str,
        updated_by: int
    ):

        meeting_note = db.scalar(
            select(MeetingNote).where(
                MeetingNote.id == note_id
            )
        )

        if not meeting_note:
            raise Exception("Note not found")

        history = MeetingNoteHistory(
            note_id=meeting_note.id,
            old_note=meeting_note.note,
            updated_by=updated_by
        )

        db.add(history)

        meeting_note.note = note

        db.commit()
        db.refresh(meeting_note)

        return meeting_note

    @staticmethod
    def get_history(
        db,
        note_id: int
    ):

        return db.scalars(
            select(MeetingNoteHistory).where(
                MeetingNoteHistory.note_id == note_id
            )
        ).all()