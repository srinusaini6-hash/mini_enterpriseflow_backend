from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.users.models import User

from app.approvals.schemas import (
    ApprovalCreate,
    ApprovalAction,
    ApprovalResponse
)

from app.approvals.services import (
    submit_request_service,
    approve_request_service,
    reject_request_service,
    get_requests_service
)


router = APIRouter(
    prefix="/approvals",
    tags=["Approvals"]
)


# ---------------- SUBMIT REQUEST ----------------

@router.post("/")
def submit_request(
    request: ApprovalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return submit_request_service(
        request,
        db,
        current_user
    )


# ---------------- APPROVE REQUEST ----------------

@router.put("/approve/{request_id}")
def approve_request(
    request_id: int,
    action: ApprovalAction,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return approve_request_service(
        request_id,
        action,
        db,
        current_user
    )


# ---------------- REJECT REQUEST ----------------

@router.put("/reject/{request_id}")
def reject_request(
    request_id: int,
    action: ApprovalAction,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return reject_request_service(
        request_id,
        action,
        db,
        current_user
    )


# ---------------- GET REQUESTS ----------------

@router.get(
    "/",
    response_model=Page[ApprovalResponse]
)
def get_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_requests_service(
        db
    )