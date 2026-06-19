from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_instances.schemas import (
    WorkflowExecutionStart,
    WorkflowInstanceResponse
)

from app.workflow_instances.service import (
    start_workflow,
    get_execution,
    get_pending_executions,
    get_completed_executions,
    get_rejected_executions
)

router = APIRouter(
    tags=["Workflow Executions"]
)


@router.post(
    "/workflow-executions/start",
    response_model=WorkflowInstanceResponse
)
def start_workflow_execution(
    payload: WorkflowExecutionStart,
    db: Session = Depends(get_db)
):
    return start_workflow(
        db,
        payload.workflow_template_id,
        payload.request_id
    )


@router.get(
    "/workflow-executions/pending",
    response_model=list[WorkflowInstanceResponse]
)
def pending_workflows(
    db: Session = Depends(get_db)
):
    return get_pending_executions(db)


@router.get(
    "/workflow-executions/completed",
    response_model=list[WorkflowInstanceResponse]
)
def completed_workflows(
    db: Session = Depends(get_db)
):
    return get_completed_executions(db)


@router.get(
    "/workflow-executions/rejected",
    response_model=list[WorkflowInstanceResponse]
)
def rejected_workflows(
    db: Session = Depends(get_db)
):
    return get_rejected_executions(db)


@router.get(
    "/workflow-executions/{execution_id}",
    response_model=WorkflowInstanceResponse
)
def get_workflow_execution(
    execution_id: int,
    db: Session = Depends(get_db)
):
    execution = get_execution(
        db,
        execution_id
    )

    if not execution:
        raise HTTPException(
            status_code=404,
            detail="Workflow execution not found"
        )

    return execution