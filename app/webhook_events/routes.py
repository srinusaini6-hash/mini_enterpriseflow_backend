from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.webhook_events.schemas import (
    WebhookEventCreate,
    WebhookEventUpdate,
    WebhookEventResponse,
)

from app.webhook_events.services import (
    create_webhook_event_service,
    get_all_webhook_events_service,
    get_webhook_event_service,
    update_webhook_event_service,
    delete_webhook_event_service,
)

router = APIRouter(
    prefix="/webhook-events",
    tags=["Webhook Events"],
)


# Create Webhook Event
@router.post(
    "",
    response_model=WebhookEventResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_webhook_event(
    webhook: WebhookEventCreate,
    db: Session = Depends(get_db),
):
    return create_webhook_event_service(
        db,
        webhook,
    )


# Get All Webhook Events
@router.get(
    "",
    response_model=list[WebhookEventResponse],
)
def get_all_webhook_events(
    db: Session = Depends(get_db),
):
    return get_all_webhook_events_service(db)


# Get Webhook Event By ID
@router.get(
    "/{webhook_id}",
    response_model=WebhookEventResponse,
)
def get_webhook_event(
    webhook_id: int,
    db: Session = Depends(get_db),
):
    return get_webhook_event_service(
        db,
        webhook_id,
    )


# Update Webhook Event
@router.put(
    "/{webhook_id}",
    response_model=WebhookEventResponse,
)
def update_webhook_event(
    webhook_id: int,
    webhook: WebhookEventUpdate,
    db: Session = Depends(get_db),
):
    return update_webhook_event_service(
        db,
        webhook_id,
        webhook,
    )


# Delete Webhook Event
@router.delete(
    "/{webhook_id}",
)
def delete_webhook_event(
    webhook_id: int,
    db: Session = Depends(get_db),
):
    return delete_webhook_event_service(
        db,
        webhook_id,
    )