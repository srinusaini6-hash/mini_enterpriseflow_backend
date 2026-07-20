from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.integration_audit_logs.schemas import (
    IntegrationAuditLogCreate,
    IntegrationAuditLogUpdate,
    IntegrationAuditLogResponse,
)

from app.integration_audit_logs.services import (
    get_all_audit_logs_service,
    get_audit_log_by_id_service,
    create_audit_log_service,
    update_audit_log_service,
    delete_audit_log_service,
)

router = APIRouter(
    prefix="/integration-audit-logs",
    tags=["Integration Audit Logs"],
)


# Create Audit Log
@router.post(
    "",
    response_model=IntegrationAuditLogResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_audit_log(
    audit_log: IntegrationAuditLogCreate,
    db: Session = Depends(get_db),
):
    return create_audit_log_service(
        db,
        audit_log,
    )


# Get All Audit Logs
@router.get(
    "",
    response_model=list[IntegrationAuditLogResponse],
)
def get_all_audit_logs(
    db: Session = Depends(get_db),
):
    return get_all_audit_logs_service(db)


# Get Audit Log By ID
@router.get(
    "/{audit_log_id}",
    response_model=IntegrationAuditLogResponse,
)
def get_audit_log(
    audit_log_id: int,
    db: Session = Depends(get_db),
):
    audit_log = get_audit_log_by_id_service(
        db,
        audit_log_id,
    )

    if not audit_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audit log not found."
        )

    return audit_log


# Update Audit Log
@router.put(
    "/{audit_log_id}",
    response_model=IntegrationAuditLogResponse,
)
def update_audit_log(
    audit_log_id: int,
    audit_log: IntegrationAuditLogUpdate,
    db: Session = Depends(get_db),
):
    updated = update_audit_log_service(
        db,
        audit_log_id,
        audit_log,
    )

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audit log not found."
        )

    return updated


# Delete Audit Log
@router.delete(
    "/{audit_log_id}",
)
def delete_audit_log(
    audit_log_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_audit_log_service(
        db,
        audit_log_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audit log not found."
        )

    return {
        "message": "Integration audit log deleted successfully."
    }