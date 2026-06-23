from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_conditions.models import (
    WorkflowCondition
)


def create_condition(
    db: Session,
    workflow_template_id: int,
    payload
):
    condition = WorkflowCondition(
        workflow_template_id=workflow_template_id,
        field_name=payload.field_name,
        operator=payload.operator,
        value=payload.value
    )

    db.add(condition)
    db.commit()
    db.refresh(condition)

    return condition


def get_conditions(
    db: Session,
    workflow_template_id: int
):
    stmt = select(WorkflowCondition).where(
        WorkflowCondition.workflow_template_id
        == workflow_template_id
    )

    result = db.execute(stmt)

    return result.scalars().all()


def update_condition(
    db: Session,
    condition_id: int,
    payload
):
    stmt = select(WorkflowCondition).where(
        WorkflowCondition.id == condition_id
    )

    result = db.execute(stmt)

    condition = result.scalar_one_or_none()

    if not condition:
        return None

    condition.field_name = payload.field_name
    condition.operator = payload.operator
    condition.value = payload.value

    db.commit()
    db.refresh(condition)

    return condition


def delete_condition(
    db: Session,
    condition_id: int
):
    stmt = select(WorkflowCondition).where(
        WorkflowCondition.id == condition_id
    )

    result = db.execute(stmt)

    condition = result.scalar_one_or_none()

    if not condition:
        return None

    db.delete(condition)
    db.commit()

    return True