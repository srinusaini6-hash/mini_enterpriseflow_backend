from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.users.models import User

from app.notifications.schemas import (
    NotificationResponse
)

from app.notifications import services


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# ---------------- GET NOTIFICATIONS ----------------

@router.get(
    "/",
    response_model=Page[NotificationResponse]
)
def get_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.get_notifications_service(
        db,
        current_user
    )


# ---------------- MARK AS READ ----------------

@router.put("/{notification_id}")
def mark_as_read(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.mark_as_read_service(
        db,
        notification_id,
        current_user
    )


# ---------------- DELETE NOTIFICATION ----------------

@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.delete_notification_service(
        db,
        notification_id,
        current_user
    )