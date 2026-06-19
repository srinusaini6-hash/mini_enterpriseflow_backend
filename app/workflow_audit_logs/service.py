from sqlalchemy.orm import Session

from app.workflow_audit_logs.models import (
    WorkflowAuditLog
)


def create_audit_log(
    db: Session,
    execution_id: int,
    action: str,
    performed_by: str,
    remarks: str = None
):
    log = WorkflowAuditLog(
        execution_id=execution_id,
        action=action,
        performed_by=performed_by,
        remarks=remarks
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log


def get_all_logs(db: Session):
    return db.query(
        WorkflowAuditLog
    ).all()


def get_logs_by_execution(
    db: Session,
    execution_id: int
):
    return db.query(
        WorkflowAuditLog
    ).filter(
        WorkflowAuditLog.execution_id == execution_id
    ).all()


def get_logs_by_action(
    db: Session,
    action: str
):
    return db.query(
        WorkflowAuditLog
    ).filter(
        WorkflowAuditLog.action == action
    ).all()