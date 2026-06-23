from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_audit_logs.models import WorkflowAuditLog


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


def get_all_logs(
    db: Session
):
    stmt = select(WorkflowAuditLog)

    result = db.execute(stmt)

    return result.scalars().all()


def get_logs_by_execution(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowAuditLog).where(
        WorkflowAuditLog.execution_id == execution_id
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_logs_by_action(
    db: Session,
    action: str
):
    stmt = select(WorkflowAuditLog).where(
        WorkflowAuditLog.action == action
    )

    result = db.execute(stmt)

    return result.scalars().all()