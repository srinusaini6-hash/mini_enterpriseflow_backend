from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from .schemas import (
    MentionCreate,
    MentionResponse
)

from .service import (
    create_mention,
    get_mentions_by_message,
    get_mention,
    delete_mention
)

router = APIRouter(
    prefix="",
    tags=["Message Mentions"]
)


@router.post(
    "/messages/{message_id}/mentions",
    response_model=MentionResponse
)
def add_mention(
    message_id: int,
    mention: MentionCreate,
    db: Session = Depends(get_db)
):
    return create_mention(
        db,
        message_id,
        mention
    )


@router.get(
    "/messages/{message_id}/mentions",
    response_model=List[MentionResponse]
)
def list_mentions(
    message_id: int,
    db: Session = Depends(get_db)
):
    return get_mentions_by_message(
        db,
        message_id
    )


@router.get(
    "/mentions/{mention_id}",
    response_model=MentionResponse
)
def get_single_mention(
    mention_id: int,
    db: Session = Depends(get_db)
):
    mention = get_mention(
        db,
        mention_id
    )

    if not mention:
        raise HTTPException(
            status_code=404,
            detail="Mention not found"
        )

    return mention


@router.delete(
    "/mentions/{mention_id}"
)
def remove_mention(
    mention_id: int,
    db: Session = Depends(get_db)
):
    mention = delete_mention(
        db,
        mention_id
    )

    if not mention:
        raise HTTPException(
            status_code=404,
            detail="Mention not found"
        )

    return {
        "message": "Mention deleted successfully"
    }