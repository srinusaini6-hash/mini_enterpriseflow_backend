from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from .schemas import (
    ReadReceiptCreate,
    ReadReceiptResponse
)

from .service import (
    mark_as_read,
    get_read_receipts,
    get_single_receipt,
    delete_receipt
)

router = APIRouter(
    prefix="",
    tags=["Read Receipts"]
)


@router.post(
    "/messages/{message_id}/read",
    response_model=ReadReceiptResponse
)
def create_read_receipt(
    message_id: int,
    payload: ReadReceiptCreate,
    db: Session = Depends(get_db)
):
    return mark_as_read(
        db,
        message_id,
        payload.user_id
    )


@router.get(
    "/messages/{message_id}/read-receipts",
    response_model=list[ReadReceiptResponse]
)
def list_read_receipts(
    message_id: int,
    db: Session = Depends(get_db)
):
    return get_read_receipts(
        db,
        message_id
    )


@router.get(
    "/read-receipts/{receipt_id}",
    response_model=ReadReceiptResponse
)
def get_receipt(
    receipt_id: int,
    db: Session = Depends(get_db)
):
    receipt = get_single_receipt(
        db,
        receipt_id
    )

    if not receipt:
        raise HTTPException(
            status_code=404,
            detail="Read receipt not found"
        )

    return receipt


@router.delete(
    "/read-receipts/{receipt_id}"
)
def remove_receipt(
    receipt_id: int,
    db: Session = Depends(get_db)
):
    receipt = delete_receipt(
        db,
        receipt_id
    )

    if not receipt:
        raise HTTPException(
            status_code=404,
            detail="Read receipt not found"
        )

    return {
        "message": "Read receipt deleted successfully"
    }