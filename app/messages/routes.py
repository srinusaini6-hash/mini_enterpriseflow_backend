from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.database import Base, get_db

from app.messages.schemas import (
    MessageCreate,
    MessageResponse
)

from app.messages.service import (
    create_message,
    get_channel_messages,
    get_message,
    delete_message
)

router = APIRouter(
    tags=["Messages"]
)


@router.post(
    "/channels/{channel_id}/messages",
    response_model=MessageResponse
)
def create_new_message(
    channel_id: int,
    payload: MessageCreate,
    db: Session = Depends(get_db)
):
    return create_message(
        db,
        channel_id,
        payload.sender_id,
        payload.content
    )


@router.get(
    "/channels/{channel_id}/messages",
    response_model=list[MessageResponse]
)
def list_messages(
    channel_id: int,
    db: Session = Depends(get_db)
):
    return get_channel_messages(db, channel_id)


@router.get(
    "/messages/{message_id}",
    response_model=MessageResponse
)
def get_single_message(
    message_id: int,
    db: Session = Depends(get_db)
):
    message = get_message(db, message_id)

    if not message:
        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )

    return message


@router.delete("/messages/{message_id}")
def remove_message(
    message_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_message(db, message_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )

    return {
        "message": "Message deleted successfully"
    }