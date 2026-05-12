from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.approvals.models import (
    ApprovalRequest,
    ApprovalHistory
)

from app.approvals.schemas import (
    ApprovalCreate,
    ApprovalAction
)

from app.auth.dependencies import get_current_user

from app.users.models import User


router = APIRouter(
    prefix="/approvals",
    tags=["Approvals"]
)


@router.post("/")
def submit_request(
    request: ApprovalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_request = ApprovalRequest(
        request_type=request.request_type,
        reason=request.reason,
        amount=request.amount,
        submitted_by=current_user.id,
        current_approver="manager"
    )

    db.add(new_request)

    db.commit()

    db.refresh(new_request)

    return {
        "message": "Request submitted successfully"
    }


@router.put("/approve/{request_id}")
def approve_request(
    request_id: int,
    action: ApprovalAction,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    request = db.query(ApprovalRequest).filter(
        ApprovalRequest.id == request_id
    ).first()

    if not request:

        raise HTTPException(
            status_code=404,
            detail="Request not found"
        )

    if current_user.role == "manager":

        if request.amount > 5000:

            request.current_approver = "admin"

            request.status = "ESCALATED"

        else:

            request.status = "APPROVED"

    elif current_user.role == "admin":

        request.status = "FINAL_APPROVED"

    else:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    history = ApprovalHistory(
        request_id=request.id,
        action="APPROVED",
        comment=action.comment,
        action_by=current_user.id
    )

    db.add(history)

    db.commit()

    return {
        "message": "Request approved"
    }


@router.put("/reject/{request_id}")
def reject_request(
    request_id: int,
    action: ApprovalAction,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    request = db.query(ApprovalRequest).filter(
        ApprovalRequest.id == request_id
    ).first()

    if not request:

        raise HTTPException(
            status_code=404,
            detail="Request not found"
        )

    request.status = "REJECTED"

    history = ApprovalHistory(
        request_id=request.id,
        action="REJECTED",
        comment=action.comment,
        action_by=current_user.id
    )

    db.add(history)

    db.commit()

    return {
        "message": "Request rejected"
    }


@router.get("/")
def get_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    requests = db.query(
        ApprovalRequest
    ).all()

    return requests