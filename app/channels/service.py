from sqlalchemy.orm import Session
from app.channels.models import Channel


def get_workspace_channels(db: Session, workspace_id: int):
    return db.query(Channel).filter(
        Channel.workspace_id == workspace_id
    ).all()


def get_channel_by_id(db: Session, channel_id: int):
    return db.query(Channel).filter(
        Channel.id == channel_id
    ).first()


def update_channel(db: Session, channel_id: int, data):
    channel = get_channel_by_id(db, channel_id)

    if not channel:
        return None

    channel.name = data.name
    channel.description = data.description
    channel.channel_type = data.channel_type

    db.commit()
    db.refresh(channel)

    return channel


def archive_channel(db: Session, channel_id: int):
    channel = get_channel_by_id(db, channel_id)

    if not channel:
        return None

    channel.is_archived = True

    db.commit()

    return {"message": "Channel archived successfully"}


def restore_channel(db: Session, channel_id: int):
    channel = get_channel_by_id(db, channel_id)

    if not channel:
        return None

    channel.is_archived = False

    db.commit()

    return {"message": "Channel restored successfully"}