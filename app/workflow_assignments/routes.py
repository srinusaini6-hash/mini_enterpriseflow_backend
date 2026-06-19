from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_assignments.schemas import (
    ReassignRequest,
    WorkflowAssignmentResponse
)

from app.workflow_assignments.service import (
    get_assignees,
    reassign_workflow,
    get_history
)

router = APIRouter(
    tags=["Workflow Assignments"]
)


@router.get(
    "/workflow-executions/{execution_id}/assignees",
    response_model=list[WorkflowAssignmentResponse]
)
def list_assignees(
    execution_id: int,
    db: Session = Depends(get_db)
):
    return get_assignees(
        db,
        execution_id
    )


@router.post(
    "/workflow-executions/{execution_id}/reassign",
    response_model=WorkflowAssignmentResponse
)
def reassign(
    execution_id: int,
    payload: ReassignRequest,
    db: Session = Depends(get_db)
):
    assignment = reassign_workflow(
        db,
        execution_id,
        payload.assigned_to,
        payload.assigned_by
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Workflow execution not found"
        )

    return assignment


@router.get(
    "/workflow-executions/{execution_id}/history",
    response_model=list[WorkflowAssignmentResponse]
)
def workflow_history(
    execution_id: int,
    db: Session = Depends(get_db)
):
    return get_history(
        db,
        execution_id
    )