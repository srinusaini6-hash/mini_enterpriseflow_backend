from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_notifications.schemas import (
    NotificationCreate,
    NotificationResponse
)

from app.workflow_notifications.service import (
    create_notification,
    get_notifications,
    get_notification,
    get_user_notifications,
    mark_as_read,
    delete_notification
)

router = APIRouter(
    prefix="/workflow-notifications",
    tags=["Workflow Notifications"]
)


@router.post(
    "",
    response_model=NotificationResponse
)
def create_new_notification(
    payload: NotificationCreate,
    db: Session = Depends(get_db)
):
    return create_notification(db, payload)


@router.get(
    "",
    response_model=list[NotificationResponse]
)
def list_notifications(
    db: Session = Depends(get_db)
):
    return get_notifications(db)


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse
)
def get_single_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = get_notification(db, notification_id)

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification


@router.get(
    "/user/{user_name}",
    response_model=list[NotificationResponse]
)
def get_notifications_by_user(
    user_name: str,
    db: Session = Depends(get_db)
):
    return get_user_notifications(db, user_name)


@router.put(
    "/{notification_id}/read"
)
def read_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = mark_as_read(db, notification_id)

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return {
        "message": "Notification marked as read"
    }


@router.delete(
    "/{notification_id}"
)
def remove_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = delete_notification(db, notification_id)

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return {
        "message": "Notification deleted successfully"
    }