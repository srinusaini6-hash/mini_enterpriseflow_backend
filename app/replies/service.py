from sqlalchemy.orm import Session

from .models import Reply


def create_reply(
    db: Session,
    message_id: int,
    sender_id: int,
    content: str
):
    reply = Reply(
        message_id=message_id,
        sender_id=sender_id,
        content=content
    )

    db.add(reply)
    db.commit()
    db.refresh(reply)

    return reply


def get_replies(
    db: Session,
    message_id: int
):
    return db.query(Reply).filter(
        Reply.message_id == message_id
    ).all()


def get_reply(
    db: Session,
    reply_id: int
):
    return db.query(Reply).filter(
        Reply.id == reply_id
    ).first()


def delete_reply(
    db: Session,
    reply_id: int
):
    reply = db.query(Reply).filter(
        Reply.id == reply_id
    ).first()

    if reply:
        db.delete(reply)
        db.commit()

    return reply