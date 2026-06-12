from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workspaces.schemas import (
    WorkspaceCreate,
    WorkspaceUpdate
)

from app.workspaces.service import (
    WorkspaceService
)

router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"]
)


@router.post("/")
def create_workspace(
    payload: WorkspaceCreate,
    db: Session = Depends(get_db)
):
    return WorkspaceService.create_workspace(
        db,
        payload
    )


@router.get("/")
def list_workspaces(
    db: Session = Depends(get_db)
):
    return WorkspaceService.list_workspaces(db)


@router.get("/{workspace_id}")
def get_workspace(
    workspace_id: int,
    db: Session = Depends(get_db)
):
    return WorkspaceService.get_workspace(
        db,
        workspace_id
    )


@router.put("/{workspace_id}")
def update_workspace(
    workspace_id: int,
    payload: WorkspaceUpdate,
    db: Session = Depends(get_db)
):
    return WorkspaceService.update_workspace(
        db,
        workspace_id,
        payload
    )


@router.patch("/{workspace_id}/archive")
def archive_workspace(
    workspace_id: int,
    db: Session = Depends(get_db)
):
    return WorkspaceService.archive_workspace(
        db,
        workspace_id
    )


@router.patch("/{workspace_id}/restore")
def restore_workspace(
    workspace_id: int,
    db: Session = Depends(get_db)
):
    return WorkspaceService.restore_workspace(
        db,
        workspace_id
    )