from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workspace_members.schemas import (
    WorkspaceMemberCreate,
    WorkspaceMemberResponse
)

from app.workspace_members.service import (
    add_member,
    get_members,
    remove_member
)

router = APIRouter(
    prefix="/workspaces",
    tags=["Workspace Members"]
)


@router.post("/{workspace_id}/members",
             response_model=WorkspaceMemberResponse)
def create_member(
        workspace_id: int,
        payload: WorkspaceMemberCreate,
        db: Session = Depends(get_db)
):
    return add_member(
        db,
        workspace_id,
        payload.user_id,
        payload.role
    )


@router.get("/{workspace_id}/members",
            response_model=list[WorkspaceMemberResponse])
def list_members(
        workspace_id: int,
        db: Session = Depends(get_db)
):
    return get_members(db, workspace_id)


@router.delete("/{workspace_id}/members/{user_id}")
def delete_member(
        workspace_id: int,
        user_id: int,
        db: Session = Depends(get_db)
):
    return remove_member(
        db,
        workspace_id,
        user_id
    )