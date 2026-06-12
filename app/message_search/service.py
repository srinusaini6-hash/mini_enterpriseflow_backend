from sqlalchemy.orm import Session
from app.messages.models import Message


def search_messages(
    db: Session,
    keyword: str = None,
    sender_id: int = None,
    channel_id: int = None
):

    query = db.query(Message)

    if keyword:
        query = query.filter(
            Message.content.ilike(f"%{keyword}%")
        )

    if sender_id:
        query = query.filter(
            Message.sender_id == sender_id
        )

    if channel_id:
        query = query.filter(
            Message.channel_id == channel_id
        )

    return query.all()