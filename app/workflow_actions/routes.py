from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_actions.service import (
    approve_workflow,
    reject_workflow,
    hold_workflow,
    resume_workflow,
    cancel_workflow
)

router = APIRouter(
    tags=["Workflow Actions"]
)


@router.post(
    "/workflow-executions/{execution_id}/approve"
)
def approve_workflow_action(
    execution_id: int,
    db: Session = Depends(get_db)
):
    workflow = approve_workflow(
        db,
        execution_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow execution not found"
        )

    return {
        "message": "Workflow approved successfully"
    }


@router.post(
    "/workflow-executions/{execution_id}/reject"
)
def reject_workflow_action(
    execution_id: int,
    db: Session = Depends(get_db)
):
    workflow = reject_workflow(
        db,
        execution_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow execution not found"
        )

    return {
        "message": "Workflow rejected successfully"
    }


@router.post(
    "/workflow-executions/{execution_id}/hold"
)
def hold_workflow_action(
    execution_id: int,
    db: Session = Depends(get_db)
):
    workflow = hold_workflow(
        db,
        execution_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow execution not found"
        )

    return {
        "message": "Workflow put on hold successfully"
    }


@router.post(
    "/workflow-executions/{execution_id}/resume"
)
def resume_workflow_action(
    execution_id: int,
    db: Session = Depends(get_db)
):
    workflow = resume_workflow(
        db,
        execution_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow execution not found"
        )

    return {
        "message": "Workflow resumed successfully"
    }


@router.post(
    "/workflow-executions/{execution_id}/cancel"
)
def cancel_workflow_action(
    execution_id: int,
    db: Session = Depends(get_db)
):
    workflow = cancel_workflow(
        db,
        execution_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow execution not found"
        )

    return {
        "message": "Workflow cancelled successfully"
    }