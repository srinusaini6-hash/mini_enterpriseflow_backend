from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from .schemas import (
    ReplyCreate,
    ReplyResponse
)

from .service import (
    create_reply,
    get_replies,
    get_reply,
    delete_reply
)

router = APIRouter(
    prefix="",
    tags=["Replies"]
)


@router.post(
    "/messages/{message_id}/replies",
    response_model=ReplyResponse
)
def add_reply(
    message_id: int,
    payload: ReplyCreate,
    db: Session = Depends(get_db)
):
    return create_reply(
        db,
        message_id,
        payload.sender_id,
        payload.content
    )


@router.get(
    "/messages/{message_id}/replies",
    response_model=list[ReplyResponse]
)
def list_replies(
    message_id: int,
    db: Session = Depends(get_db)
):
    return get_replies(
        db,
        message_id
    )


@router.get(
    "/replies/{reply_id}",
    response_model=ReplyResponse
)
def get_single_reply(
    reply_id: int,
    db: Session = Depends(get_db)
):
    return get_reply(
        db,
        reply_id
    )


@router.delete(
    "/replies/{reply_id}"
)
def remove_reply(
    reply_id: int,
    db: Session = Depends(get_db)
):
    delete_reply(
        db,
        reply_id
    )

    return {
        "message": "Reply deleted successfully"
    }