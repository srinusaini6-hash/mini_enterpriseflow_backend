from sqlalchemy.orm import Session
from app.messages.models import Message


def create_message(db: Session, channel_id: int, sender_id: int, content: str):

    message = Message(
        channel_id=channel_id,
        sender_id=sender_id,
        content=content
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


def get_channel_messages(db: Session, channel_id: int):
    return db.query(Message).filter(
        Message.channel_id == channel_id
    ).all()


def get_message(db: Session, message_id: int):
    return db.query(Message).filter(
        Message.id == message_id
    ).first()


def delete_message(db: Session, message_id: int):

    message = db.query(Message).filter(
        Message.id == message_id
    ).first()

    if not message:
        return None

    db.delete(message)
    db.commit()

    return True