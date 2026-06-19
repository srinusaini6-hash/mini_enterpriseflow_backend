from sqlalchemy.orm import Session

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
    return db.query(
        WorkflowCondition
    ).filter(
        WorkflowCondition.workflow_template_id
        == workflow_template_id
    ).all()


def update_condition(
    db: Session,
    condition_id: int,
    payload
):
    condition = db.query(
        WorkflowCondition
    ).filter(
        WorkflowCondition.id == condition_id
    ).first()

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
    condition = db.query(
        WorkflowCondition
    ).filter(
        WorkflowCondition.id == condition_id
    ).first()

    if not condition:
        return None

    db.delete(condition)
    db.commit()

    return True