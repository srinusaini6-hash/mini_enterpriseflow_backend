from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.history.models import TaskHistory

from app.auth.dependencies import get_current_user
from app.users.models import User


router = APIRouter(
    prefix="/history",
    tags=["History"]
)


# ---------------- GET TASK HISTORY ----------------
@router.get("/{task_id}")
def get_task_history(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    history = db.query(TaskHistory).filter(
        TaskHistory.task_id == task_id
    ).order_by(
        TaskHistory.changed_at.desc()
    ).all()

    return history


# ---------------- CREATE HISTORY ----------------
@router.post("/")
def create_history(
    task_id: int,
    field_name: str,
    old_value: str,
    new_value: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    history = TaskHistory(
        task_id=task_id,
        changed_by=current_user.id,
        field_name=field_name,
        old_value=old_value,
        new_value=new_value
    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return {
        "message": "Task history created successfully"
    }


# ---------------- UPDATE HISTORY ----------------
@router.put("/{history_id}")
def update_history(
    history_id: int,
    field_name: str,
    old_value: str,
    new_value: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    history = db.query(TaskHistory).filter(
        TaskHistory.id == history_id
    ).first()

    if not history:
        raise HTTPException(
            status_code=404,
            detail="History not found"
        )

    history.field_name = field_name
    history.old_value = old_value
    history.new_value = new_value

    db.commit()

    return {
        "message": "History updated successfully"
    }


# ---------------- DELETE HISTORY ----------------
@router.delete("/{history_id}")
def delete_history(
    history_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    history = db.query(TaskHistory).filter(
        TaskHistory.id == history_id
    ).first()

    if not history:
        raise HTTPException(
            status_code=404,
            detail="History not found"
        )

    db.delete(history)

    db.commit()

    return {
        "message": "History deleted successfully"
    }