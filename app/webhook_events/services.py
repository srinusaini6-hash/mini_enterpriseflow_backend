from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.webhook_events.repository import (
    create_webhook_event,
    get_all_webhook_events,
    get_webhook_event_by_id,
    update_webhook_event,
    delete_webhook_event,
)

from app.webhook_events.schemas import (
    WebhookEventCreate,
    WebhookEventUpdate,
)

from app.tenant_integrations.models import TenantIntegration


def create_webhook_event_service(
    db: Session,
    webhook: WebhookEventCreate,
):
    integration = (
        db.query(TenantIntegration)
        .filter(
            TenantIntegration.id == webhook.integration_id
        )
        .first()
    )

    if not integration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant integration not found."
        )

    return create_webhook_event(
        db,
        webhook,
    )


def get_all_webhook_events_service(
    db: Session,
):
    return get_all_webhook_events(db)


def get_webhook_event_service(
    db: Session,
    webhook_id: int,
):
    webhook = get_webhook_event_by_id(
        db,
        webhook_id,
    )

    if not webhook:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Webhook event not found."
        )

    return webhook


def update_webhook_event_service(
    db: Session,
    webhook_id: int,
    webhook: WebhookEventUpdate,
):
    updated = update_webhook_event(
        db,
        webhook_id,
        webhook,
    )

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Webhook event not found."
        )

    return updated


def delete_webhook_event_service(
    db: Session,
    webhook_id: int,
):
    deleted = delete_webhook_event(
        db,
        webhook_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Webhook event not found."
        )

    return {
        "message": "Webhook event deleted successfully."
    }