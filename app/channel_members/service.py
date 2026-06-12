from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.channels.models import Channel
from app.channel_members.models import ChannelMember


def add_member(
    db: Session,
    channel_id: int,
    user_id: int
):

    channel = db.query(Channel).filter(
        Channel.id == channel_id
    ).first()

    if not channel:
        raise HTTPException(
            status_code=404,
            detail="Channel not found"
        )

    existing = db.query(ChannelMember).filter(
        ChannelMember.channel_id == channel_id,
        ChannelMember.user_id == user_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists in channel"
        )

    member = ChannelMember(
        channel_id=channel_id,
        user_id=user_id
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    return member


def list_members(
    db: Session,
    channel_id: int
):

    return db.query(ChannelMember).filter(
        ChannelMember.channel_id == channel_id
    ).all()


def remove_member(
    db: Session,
    channel_id: int,
    user_id: int
):

    member = db.query(ChannelMember).filter(
        ChannelMember.channel_id == channel_id,
        ChannelMember.user_id == user_id
    ).first()

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    db.delete(member)
    db.commit()

    return {
        "message": "Member removed successfully"
    }