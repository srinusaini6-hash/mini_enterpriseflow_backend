from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_reports.schemas import (
    WorkflowSummary,
    WorkflowReportResponse
)

from app.workflow_reports.service import (
    get_summary,
    get_by_status,
    get_by_execution
)

router = APIRouter(
    prefix="/workflow-reports",
    tags=["Workflow Reports"]
)


@router.get(
    "/summary",
    response_model=WorkflowSummary
)
def workflow_summary(
    db: Session = Depends(get_db)
):
    return get_summary(db)


@router.get(
    "/status/{status}",
    response_model=list[WorkflowReportResponse]
)
def workflows_by_status(
    status: str,
    db: Session = Depends(get_db)
):
    return get_by_status(
        db,
        status
    )


@router.get(
    "/execution/{execution_id}",
    response_model=WorkflowReportResponse
)
def workflow_by_execution(
    execution_id: int,
    db: Session = Depends(get_db)
):
    workflow = get_by_execution(
        db,
        execution_id
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    return workflow