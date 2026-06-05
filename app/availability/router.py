from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.availability.schemas import (
    AvailabilityCheckRequest
)

from app.availability.service import (
    AvailabilityService
)

router = APIRouter(
    prefix="/availability",
    tags=["Availability"]
)


@router.post("/check")
def check_availability(
    payload: AvailabilityCheckRequest,
    db: Session = Depends(get_db)
):

    return AvailabilityService.check_availability(
        db=db,
        user_ids=payload.user_ids,
        start_time=payload.start_time,
        end_time=payload.end_time
    )