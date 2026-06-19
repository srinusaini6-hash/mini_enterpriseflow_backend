from sqlalchemy.orm import Session

from app.workflow_templates.models import WorkflowTemplate


def create_workflow_template(
    db: Session,
    payload
):
    workflow = WorkflowTemplate(
        tenant_id=payload.tenant_id,
        name=payload.name,
        description=payload.description,
        module_name=payload.module_name
    )

    db.add(workflow)
    db.commit()
    db.refresh(workflow)

    return workflow


def get_workflow_templates(
    db: Session
):
    return db.query(
        WorkflowTemplate
    ).all()


def get_workflow_template(
    db: Session,
    template_id: int
):
    return db.query(
        WorkflowTemplate
    ).filter(
        WorkflowTemplate.id == template_id
    ).first()


def update_workflow_template(
    db: Session,
    template_id: int,
    payload
):
    workflow = db.query(
        WorkflowTemplate
    ).filter(
        WorkflowTemplate.id == template_id
    ).first()

    if not workflow:
        return None

    workflow.tenant_id = payload.tenant_id
    workflow.name = payload.name
    workflow.description = payload.description
    workflow.module_name = payload.module_name
    workflow.is_active = payload.is_active

    db.commit()
    db.refresh(workflow)

    return workflow


def delete_workflow_template(
    db: Session,
    template_id: int
):
    workflow = db.query(
        WorkflowTemplate
    ).filter(
        WorkflowTemplate.id == template_id
    ).first()

    if not workflow:
        return None

    workflow.is_active = False

    db.commit()
    db.refresh(workflow)

    return workflow