from sqlalchemy import select

from app.action_items.models import ActionItem
from app.meetings.models import Meeting


class ActionItemService:

    @staticmethod
    def create_action_item(
        db,
        meeting_id,
        payload
    ):

        meeting = db.scalar(
            select(Meeting).where(
                Meeting.id == meeting_id
            )
        )

        if not meeting:
            raise Exception("Meeting not found")

        item = ActionItem(
            meeting_id=meeting_id,
            title=payload.title,
            owner_id=payload.owner_id,
            due_date=payload.due_date
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item

    @staticmethod
    def get_action_items(
        db,
        meeting_id
    ):

        return db.scalars(
            select(ActionItem).where(
                ActionItem.meeting_id == meeting_id
            )
        ).all()

    @staticmethod
    def convert_to_task(
        db,
        action_item_id,
        task_id
    ):

        item = db.scalar(
            select(ActionItem).where(
                ActionItem.id == action_item_id
            )
        )

        if not item:
            raise Exception("Action Item not found")

        item.task_id = task_id
        item.status = "CONVERTED"

        db.commit()
        db.refresh(item)

        return item