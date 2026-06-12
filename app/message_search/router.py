from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.messages.schemas import (
    MessageResponse
)

from app.message_search.service import (
    search_messages
)

router = APIRouter(
    tags=["Message Search"]
)


@router.get(
    "/message-search",
    response_model=list[MessageResponse]
)
def search_message_api(
    keyword: Optional[str] = None,
    sender_id: Optional[int] = None,
    channel_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return search_messages(
        db,
        keyword,
        sender_id,
        channel_id
    )