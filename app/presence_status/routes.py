from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.presence_status.schemas import (
    PresenceCreate,
    PresenceResponse
)

from app.presence_status.service import (
    update_presence,
    get_all_presence
)

router = APIRouter(
    tags=["Presence Status"]
)


@router.patch(
    "/presence/status",
    response_model=PresenceResponse
)
def update_user_status(
    payload: PresenceCreate,
    db: Session = Depends(get_db)
):
    return update_presence(
        db,
        payload.tenant_id,
        payload.user_id,
        payload.status
    )


@router.get(
    "/presence",
    response_model=list[PresenceResponse]
)
def list_presence(
    db: Session = Depends(get_db)
):
    return get_all_presence(db)