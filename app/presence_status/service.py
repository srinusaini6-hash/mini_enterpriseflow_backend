from sqlalchemy.orm import Session
from app.presence_status.models import PresenceStatus


def update_presence(
    db: Session,
    tenant_id: int,
    user_id: int,
    status: str
):
    presence = db.query(PresenceStatus).filter(
        PresenceStatus.user_id == user_id
    ).first()

    if presence:
        presence.status = status
    else:
        presence = PresenceStatus(
            tenant_id=tenant_id,
            user_id=user_id,
            status=status
        )
        db.add(presence)

    db.commit()
    db.refresh(presence)

    return presence


def get_all_presence(db: Session):
    return db.query(PresenceStatus).all()