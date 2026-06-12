from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from .schemas import (
    MessagePinCreate,
    MessagePinResponse
)

from .service import (
    pin_message,
    get_pinned_messages,
    get_single_pin,
    delete_pin
)

router = APIRouter(
    prefix="",
    tags=["Message Pins"]
)


@router.post(
    "/messages/{message_id}/pin",
    response_model=MessagePinResponse
)
def create_pin(
    message_id: int,
    payload: MessagePinCreate,
    db: Session = Depends(get_db)
):
    return pin_message(
        db,
        message_id,
        payload.user_id
    )


@router.get(
    "/pinned-messages",
    response_model=list[MessagePinResponse]
)
def list_pins(
    db: Session = Depends(get_db)
):
    return get_pinned_messages(db)


@router.get(
    "/pinned-messages/{pin_id}",
    response_model=MessagePinResponse
)
def get_pin(
    pin_id: int,
    db: Session = Depends(get_db)
):
    pin = get_single_pin(
        db,
        pin_id
    )

    if not pin:
        raise HTTPException(
            status_code=404,
            detail="Pinned message not found"
        )

    return pin


@router.delete(
    "/pinned-messages/{pin_id}"
)
def remove_pin(
    pin_id: int,
    db: Session = Depends(get_db)
):
    pin = delete_pin(
        db,
        pin_id
    )

    if not pin:
        raise HTTPException(
            status_code=404,
            detail="Pinned message not found"
        )

    return {
        "message": "Pinned message removed successfully"
    }