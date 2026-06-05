from sqlalchemy.orm import Session

from app.ai_summary.models import AIMeetingSummary


class AISummaryService:

    @staticmethod
    def generate_summary(
        db: Session,
        meeting_id: int,
        notes: list[str]
    ):

        summary = " ".join(notes)

        decisions = [
            note for note in notes
            if "approved" in note.lower()
            or "decision" in note.lower()
        ]

        action_items = [
            note for note in notes
            if "will" in note.lower()
        ]

        suggested_owners = []

        for note in notes:
            words = note.split()

            if len(words) > 0:
                suggested_owners.append(words[0])

        ai_summary = AIMeetingSummary(
            meeting_id=meeting_id,
            summary=summary,
            decisions=", ".join(decisions),
            action_items=", ".join(action_items),
            suggested_owners=", ".join(suggested_owners)
        )

        db.add(ai_summary)
        db.commit()
        db.refresh(ai_summary)

        return {
            "meeting_id": meeting_id,
            "summary": summary,
            "decisions": decisions,
            "action_items": action_items,
            "suggested_owners": suggested_owners
        }

    @staticmethod
    def get_summary(
        db: Session,
        meeting_id: int
    ):

        summary = (
            db.query(AIMeetingSummary)
            .filter(
                AIMeetingSummary.meeting_id == meeting_id
            )
            .first()
        )

        return summary