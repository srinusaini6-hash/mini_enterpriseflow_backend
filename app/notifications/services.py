from fastapi import HTTPException

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.notifications.models import Notification


# ---------------- CREATE NOTIFICATION ----------------

def create_notification(
    db,
    user_id,
    message
):

    notification = Notification(
        user_id=user_id,
        message=message
    )

    db.add(notification)

    db.commit()

    db.refresh(notification)

    return notification


# ---------------- GET NOTIFICATIONS ----------------

def get_notifications_service(
    db,
    current_user
):

    query = select(Notification).where(
        Notification.user_id == current_user.id
    )

    return paginate(
        db,
        query
    )


# ---------------- MARK AS READ ----------------

def mark_as_read_service(
    db,
    notification_id,
    current_user
):

    notification = db.execute(
        select(Notification).where(
            Notification.id == notification_id,
            Notification.user_id == current_user.id
        )
    ).scalars().first()

    if not notification:

        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    notification.is_read = True

    db.commit()

    db.refresh(notification)

    return {
        "message": "Notification marked as read"
    }


# ---------------- DELETE NOTIFICATION ----------------

def delete_notification_service(
    db,
    notification_id,
    current_user
):

    notification = db.execute(
        select(Notification).where(
            Notification.id == notification_id,
            Notification.user_id == current_user.id
        )
    ).scalars().first()

    if not notification:

        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(notification)

    db.commit()

    return {
        "message": "Notification deleted successfully"
    }