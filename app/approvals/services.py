from fastapi import HTTPException

from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.approvals.models import (
    ApprovalRequest,
    ApprovalHistory
)


VALID_STATUSES = [
    "PENDING",
    "APPROVED",
    "REJECTED",
    "ESCALATED",
    "FINAL_APPROVED"
]


# ---------------- SUBMIT REQUEST ----------------

def submit_request_service(
    request,
    db: Session,
    current_user
):

    new_request = ApprovalRequest(
        request_type=request.request_type,
        reason=request.reason,
        amount=request.amount,
        submitted_by=current_user.id,
        current_approver="manager",
        status="PENDING"
    )

    db.add(new_request)

    db.commit()

    db.refresh(new_request)

    return {
        "message": "Request submitted successfully",
        "request_id": new_request.id
    }


# ---------------- APPROVE REQUEST ----------------

def approve_request_service(
    request_id: int,
    action,
    db: Session,
    current_user
):

    existing_request = db.execute(
        select(ApprovalRequest).where(
            ApprovalRequest.id == request_id
        )
    ).scalars().first()

    if not existing_request:

        raise HTTPException(
            status_code=404,
            detail="Request not found"
        )

    # MANAGER APPROVAL
    if current_user.role == "manager":

        if existing_request.amount > 5000:

            existing_request.current_approver = "admin"

            existing_request.status = "ESCALATED"

        else:

            existing_request.status = "APPROVED"

    # ADMIN APPROVAL
    elif current_user.role == "admin":

        existing_request.status = "FINAL_APPROVED"

    else:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    history = ApprovalHistory(
        request_id=existing_request.id,
        action="APPROVED",
        comment=action.comment,
        action_by=current_user.id
    )

    db.add(history)

    db.commit()

    db.refresh(existing_request)

    return {
        "message": "Request approved successfully",
        "status": existing_request.status
    }


# ---------------- REJECT REQUEST ----------------

def reject_request_service(
    request_id: int,
    action,
    db: Session,
    current_user
):

    existing_request = db.execute(
        select(ApprovalRequest).where(
            ApprovalRequest.id == request_id
        )
    ).scalars().first()

    if not existing_request:

        raise HTTPException(
            status_code=404,
            detail="Request not found"
        )

    if current_user.role not in ["manager", "admin"]:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    existing_request.status = "REJECTED"

    history = ApprovalHistory(
        request_id=existing_request.id,
        action="REJECTED",
        comment=action.comment,
        action_by=current_user.id
    )

    db.add(history)

    db.commit()

    db.refresh(existing_request)

    return {
        "message": "Request rejected successfully"
    }


# ---------------- GET REQUESTS ----------------

def get_requests_service(
    db: Session
):

    query = select(ApprovalRequest)

    return paginate(
        db,
        query
    )