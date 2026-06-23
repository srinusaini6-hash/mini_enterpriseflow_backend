from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_notifications.models import (
    WorkflowNotification
)


def create_notification(
    db: Session,
    payload
):
    notification = WorkflowNotification(
        execution_id=payload.execution_id,
        user_name=payload.user_name,
        message=payload.message
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification


def get_notifications(
    db: Session
):
    stmt = select(WorkflowNotification)

    result = db.execute(stmt)

    return result.scalars().all()


def get_notification(
    db: Session,
    notification_id: int
):
    stmt = select(WorkflowNotification).where(
        WorkflowNotification.id == notification_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()


def get_user_notifications(
    db: Session,
    user_name: str
):
    stmt = select(WorkflowNotification).where(
        WorkflowNotification.user_name == user_name
    )

    result = db.execute(stmt)

    return result.scalars().all()


def mark_as_read(
    db: Session,
    notification_id: int
):
    notification = get_notification(
        db,
        notification_id
    )

    if notification:
        notification.status = "Read"

        db.commit()
        db.refresh(notification)

    return notification


def delete_notification(
    db: Session,
    notification_id: int
):
    notification = get_notification(
        db,
        notification_id
    )

    if notification:
        db.delete(notification)
        db.commit()

    return notification