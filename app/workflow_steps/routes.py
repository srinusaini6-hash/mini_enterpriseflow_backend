from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_steps.schemas import (
    WorkflowStepCreate,
    WorkflowStepUpdate,
    WorkflowStepResponse
)

from app.workflow_steps.service import (
    create_workflow_step,
    get_workflow_steps,
    update_workflow_step,
    delete_workflow_step
)

router = APIRouter(
    tags=["Workflow Steps"]
)


@router.post(
    "/workflow-templates/{template_id}/steps",
    response_model=WorkflowStepResponse
)
def create_step(
    template_id: int,
    payload: WorkflowStepCreate,
    db: Session = Depends(get_db)
):
    return create_workflow_step(
        db,
        template_id,
        payload
    )


@router.get(
    "/workflow-templates/{template_id}/steps",
    response_model=list[WorkflowStepResponse]
)
def list_steps(
    template_id: int,
    db: Session = Depends(get_db)
):
    return get_workflow_steps(
        db,
        template_id
    )


@router.put(
    "/workflow-steps/{step_id}",
    response_model=WorkflowStepResponse
)
def update_step(
    step_id: int,
    payload: WorkflowStepUpdate,
    db: Session = Depends(get_db)
):
    step = update_workflow_step(
        db,
        step_id,
        payload
    )

    if not step:
        raise HTTPException(
            status_code=404,
            detail="Workflow Step not found"
        )

    return step


@router.delete(
    "/workflow-steps/{step_id}"
)
def delete_step(
    step_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_workflow_step(
        db,
        step_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Workflow Step not found"
        )

    return {
        "message": "Workflow Step deleted successfully"
    }