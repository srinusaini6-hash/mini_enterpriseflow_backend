from sqlalchemy.orm import Session

from .models import Conversation, ConversationMember


def create_conversation(db: Session, data):
    obj = Conversation(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_conversations(db: Session):
    return db.query(Conversation).all()


def get_conversation(db: Session, conversation_id: int):
    return db.query(Conversation).filter(
        Conversation.id == conversation_id
    ).first()


def add_member(
    db: Session,
    conversation_id: int,
    user_id: int
):
    obj = ConversationMember(
        conversation_id=conversation_id,
        user_id=user_id
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


def get_members(db: Session, conversation_id: int):
    return db.query(ConversationMember).filter(
        ConversationMember.conversation_id == conversation_id
    ).all()


def remove_member(
    db: Session,
    conversation_id: int,
    user_id: int
):
    member = db.query(ConversationMember).filter(
        ConversationMember.conversation_id == conversation_id,
        ConversationMember.user_id == user_id
    ).first()

    if member:
        db.delete(member)
        db.commit()

    return member