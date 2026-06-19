from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_conditions.schemas import (
    WorkflowConditionCreate,
    WorkflowConditionUpdate,
    WorkflowConditionResponse
)

from app.workflow_conditions.service import (
    create_condition,
    get_conditions,
    update_condition,
    delete_condition
)

router = APIRouter(
    tags=["Workflow Conditions"]
)


@router.post(
    "/workflow-templates/{template_id}/conditions",
    response_model=WorkflowConditionResponse
)
def create_workflow_condition(
    template_id: int,
    payload: WorkflowConditionCreate,
    db: Session = Depends(get_db)
):
    return create_condition(
        db,
        template_id,
        payload
    )


@router.get(
    "/workflow-templates/{template_id}/conditions",
    response_model=list[WorkflowConditionResponse]
)
def list_conditions(
    template_id: int,
    db: Session = Depends(get_db)
):
    return get_conditions(
        db,
        template_id
    )


@router.put(
    "/workflow-conditions/{condition_id}",
    response_model=WorkflowConditionResponse
)
def update_workflow_condition(
    condition_id: int,
    payload: WorkflowConditionUpdate,
    db: Session = Depends(get_db)
):
    condition = update_condition(
        db,
        condition_id,
        payload
    )

    if not condition:
        raise HTTPException(
            status_code=404,
            detail="Workflow Condition not found"
        )

    return condition


@router.delete(
    "/workflow-conditions/{condition_id}"
)
def delete_workflow_condition(
    condition_id: int,
    db: Session = Depends(get_db)
):
    condition = delete_condition(
        db,
        condition_id
    )

    if not condition:
        raise HTTPException(
            status_code=404,
            detail="Workflow Condition not found"
        )

    return {
        "message":
        "Workflow Condition deleted successfully"
    }