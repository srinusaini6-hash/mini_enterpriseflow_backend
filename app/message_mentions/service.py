from sqlalchemy.orm import Session

from .models import MessageMention
from .schemas import MentionCreate


def create_mention(
    db: Session,
    message_id: int,
    mention: MentionCreate
):
    obj = MessageMention(
        message_id=message_id,
        mentioned_user_id=mention.mentioned_user_id,
        mention_type=mention.mention_type
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


def get_mentions_by_message(
    db: Session,
    message_id: int
):
    return db.query(MessageMention).filter(
        MessageMention.message_id == message_id
    ).all()


def get_mention(
    db: Session,
    mention_id: int
):
    return db.query(MessageMention).filter(
        MessageMention.id == mention_id
    ).first()


def delete_mention(
    db: Session,
    mention_id: int
):
    mention = db.query(MessageMention).filter(
        MessageMention.id == mention_id
    ).first()

    if mention:
        db.delete(mention)
        db.commit()

    return mention