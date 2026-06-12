from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.workspace_members.models import WorkspaceMember


def add_member(db: Session, workspace_id: int, user_id: int, role: str):

    member = WorkspaceMember(
        workspace_id=workspace_id,
        user_id=user_id,
        role=role
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    return member


def get_members(db: Session, workspace_id: int):

    return db.query(WorkspaceMember).filter(
        WorkspaceMember.workspace_id == workspace_id
    ).all()


def remove_member(db: Session, workspace_id: int, user_id: int):

    member = db.query(WorkspaceMember).filter(
        WorkspaceMember.workspace_id == workspace_id,
        WorkspaceMember.user_id == user_id
    ).first()

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    db.delete(member)
    db.commit()

    return {"message": "Member removed successfully"}