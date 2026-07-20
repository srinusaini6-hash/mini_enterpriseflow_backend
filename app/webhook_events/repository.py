from sqlalchemy.orm import Session

from app.webhook_events.models import WebhookEvent
from app.webhook_events.schemas import (
    WebhookEventCreate,
    WebhookEventUpdate,
)


def create_webhook_event(
    db: Session,
    webhook: WebhookEventCreate
):
    db_webhook = WebhookEvent(
        **webhook.model_dump()
    )

    db.add(db_webhook)
    db.commit()
    db.refresh(db_webhook)

    return db_webhook


def get_all_webhook_events(
    db: Session
):
    return (
        db.query(WebhookEvent)
        .all()
    )


def get_webhook_event_by_id(
    db: Session,
    webhook_id: int
):
    return (
        db.query(WebhookEvent)
        .filter(WebhookEvent.id == webhook_id)
        .first()
    )


def update_webhook_event(
    db: Session,
    webhook_id: int,
    webhook: WebhookEventUpdate
):
    db_webhook = (
        db.query(WebhookEvent)
        .filter(WebhookEvent.id == webhook_id)
        .first()
    )

    if not db_webhook:
        return None

    update_data = webhook.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_webhook,
            key,
            value
        )

    db.commit()
    db.refresh(db_webhook)

    return db_webhook


def delete_webhook_event(
    db: Session,
    webhook_id: int
):
    db_webhook = (
        db.query(WebhookEvent)
        .filter(WebhookEvent.id == webhook_id)
        .first()
    )

    if not db_webhook:
        return None

    db.delete(db_webhook)
    db.commit()

    return db_webhook