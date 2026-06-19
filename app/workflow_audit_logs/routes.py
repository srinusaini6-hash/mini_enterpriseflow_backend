from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_audit_logs.schemas import (
    AuditLogCreate,
    AuditLogResponse
)

from app.workflow_audit_logs.service import (
    create_audit_log,
    get_all_logs,
    get_logs_by_execution,
    get_logs_by_action
)

router = APIRouter(
    tags=["Workflow Audit Logs"]
)


@router.post(
    "/audit-logs",
    response_model=AuditLogResponse
)
def create_log(
    payload: AuditLogCreate,
    db: Session = Depends(get_db)
):
    return create_audit_log(
        db,
        payload.execution_id,
        payload.action,
        payload.performed_by,
        payload.remarks
    )


@router.get(
    "/audit-logs",
    response_model=list[AuditLogResponse]
)
def list_logs(
    db: Session = Depends(get_db)
):
    return get_all_logs(db)


@router.get(
    "/audit-logs/execution/{execution_id}",
    response_model=list[AuditLogResponse]
)
def logs_by_execution(
    execution_id: int,
    db: Session = Depends(get_db)
):
    return get_logs_by_execution(
        db,
        execution_id
    )


@router.get(
    "/audit-logs/action/{action}",
    response_model=list[AuditLogResponse]
)
def logs_by_action(
    action: str,
    db: Session = Depends(get_db)
):
    return get_logs_by_action(
        db,
        action
    )