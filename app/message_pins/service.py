from sqlalchemy.orm import Session

from .models import MessagePin


def pin_message(
    db: Session,
    message_id: int,
    user_id: int
):
    pin = MessagePin(
        message_id=message_id,
        user_id=user_id
    )

    db.add(pin)
    db.commit()
    db.refresh(pin)

    return pin


def get_pinned_messages(
    db: Session
):
    return db.query(MessagePin).all()


def get_single_pin(
    db: Session,
    pin_id: int
):
    return db.query(MessagePin).filter(
        MessagePin.id == pin_id
    ).first()


def delete_pin(
    db: Session,
    pin_id: int
):
    pin = db.query(MessagePin).filter(
        MessagePin.id == pin_id
    ).first()

    if pin:
        db.delete(pin)
        db.commit()

    return pin