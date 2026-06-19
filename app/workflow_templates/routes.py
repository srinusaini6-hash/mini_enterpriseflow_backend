from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_templates.schemas import (
    WorkflowTemplateCreate,
    WorkflowTemplateUpdate,
    WorkflowTemplateResponse
)

from app.workflow_templates.service import (
    create_workflow_template,
    get_workflow_templates,
    get_workflow_template,
    update_workflow_template,
    delete_workflow_template
)

router = APIRouter(
    prefix="/workflow-templates",
    tags=["Workflow Templates"]
)


@router.post(
    "",
    response_model=WorkflowTemplateResponse
)
def create_template(
    payload: WorkflowTemplateCreate,
    db: Session = Depends(get_db)
):
    return create_workflow_template(db, payload)


@router.get(
    "",
    response_model=list[WorkflowTemplateResponse]
)
def list_templates(
    db: Session = Depends(get_db)
):
    return get_workflow_templates(db)


@router.get(
    "/{template_id}",
    response_model=WorkflowTemplateResponse
)
def get_template(
    template_id: int,
    db: Session = Depends(get_db)
):
    workflow = get_workflow_template(
        db,
        template_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow Template not found"
        )

    return workflow


@router.put(
    "/{template_id}",
    response_model=WorkflowTemplateResponse
)
def update_template(
    template_id: int,
    payload: WorkflowTemplateUpdate,
    db: Session = Depends(get_db)
):
    workflow = update_workflow_template(
        db,
        template_id,
        payload
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow Template not found"
        )

    return workflow


@router.delete(
    "/{template_id}"
)
def delete_template(
    template_id: int,
    db: Session = Depends(get_db)
):
    workflow = delete_workflow_template(
        db,
        template_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow Template not found"
        )

    return {
        "message": "Workflow Template archived successfully"
    }