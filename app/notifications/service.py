from app.notifications.models import Notification


def create_notification(db, user_id, message):

    notification = Notification(
        user_id=user_id,
        message=message
    )

    db.add(notification)

    db.commit()

    db.refresh(notification)

    return notification