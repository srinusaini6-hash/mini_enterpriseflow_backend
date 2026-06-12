from sqlalchemy.orm import Session

from .models import ReadReceipt


def mark_as_read(
    db: Session,
    message_id: int,
    user_id: int
):
    receipt = ReadReceipt(
        message_id=message_id,
        user_id=user_id
    )

    db.add(receipt)
    db.commit()
    db.refresh(receipt)

    return receipt


def get_read_receipts(
    db: Session,
    message_id: int
):
    return db.query(ReadReceipt).filter(
        ReadReceipt.message_id == message_id
    ).all()


def get_single_receipt(
    db: Session,
    receipt_id: int
):
    return db.query(ReadReceipt).filter(
        ReadReceipt.id == receipt_id
    ).first()


def delete_receipt(
    db: Session,
    receipt_id: int
):
    receipt = db.query(ReadReceipt).filter(
        ReadReceipt.id == receipt_id
    ).first()

    if receipt:
        db.delete(receipt)
        db.commit()

    return receipt