from sqlalchemy.orm import Session
from .models import Reaction


def create_reaction(
    db: Session,
    message_id: int,
    user_id: int,
    emoji: str
):
    reaction = Reaction(
        message_id=message_id,
        user_id=user_id,
        emoji=emoji
    )

    db.add(reaction)
    db.commit()
    db.refresh(reaction)

    return reaction


def get_reactions(
    db: Session,
    message_id: int
):
    return db.query(Reaction).filter(
        Reaction.message_id == message_id
    ).all()


def delete_reaction(
    db: Session,
    message_id: int,
    user_id: int
):
    reaction = db.query(Reaction).filter(
        Reaction.message_id == message_id,
        Reaction.user_id == user_id
    ).first()

    if reaction:
        db.delete(reaction)
        db.commit()

    return reaction