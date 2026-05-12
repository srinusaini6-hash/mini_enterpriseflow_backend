from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)
from app.utils.pagination import paginate

from sqlalchemy.orm import Session

from datetime import datetime

from app.database.database import get_db

from app.tasks.models import Task

from app.tasks.schemas import (
    TaskCreate,
    TaskUpdate
)

from app.auth.dependencies import get_current_user

from app.users.models import User

from app.notifications.service import create_notification

from app.history.service import create_history


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


VALID_STATUSES = [
    "TODO",
    "IN_PROGRESS",
    "REVIEW",
    "DONE"
]


# ------------------- CREATE TASK -------------------
@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        assigned_to=task.assigned_to,
        created_by=current_user.id,
        status="TODO"
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    create_notification(
        db,
        new_task.assigned_to,
        f"New task assigned: {new_task.title}"
    )

    return {
        "message": "Task created successfully"
    }


# ------------------- GET TASKS -------------------
@router.get("/")
def get_tasks(

    status: str = Query(None),
    priority: str = Query(None),
    sort_by: str = Query("id"),

    page: int = Query(1),
    limit: int = Query(5),

    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    query = db.query(Task).filter(
        Task.is_deleted == False
    )

    # ---------- FILTER STATUS ----------
    if status:
        query = query.filter(
            Task.status == status
        )

    # ---------- FILTER PRIORITY ----------
    if priority:
        query = query.filter(
            Task.priority == priority
        )

    # ---------- SORTING ----------
    if sort_by == "title":
        query = query.order_by(Task.title)

    elif sort_by == "priority":
        query = query.order_by(Task.priority)

    else:
        query = query.order_by(Task.id)

    return paginate(
        query,
        page,
        limit
    )

# ------------------- UPDATE TASK -------------------
@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    existing_task = db.query(Task).filter(
        Task.id == task_id,
        Task.is_deleted == False
    ).first()

    if not existing_task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.status and task.status not in VALID_STATUSES:

        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    if (
        current_user.role != "admin"
        and existing_task.assigned_to != current_user.id
    ):

        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    # ---------- STORE OLD VALUES ----------
    old_status = existing_task.status
    old_priority = existing_task.priority

    # ---------- UPDATE VALUES ----------
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.priority = task.priority
    existing_task.status = task.status

    # ---------- HISTORY TRACKING ----------
    if old_status != task.status:

        create_history(
            db,
            existing_task.id,
            current_user.id,
            "status",
            old_status,
            task.status
        )

    if old_priority != task.priority:

        create_history(
            db,
            existing_task.id,
            current_user.id,
            "priority",
            old_priority,
            task.priority
        )

    db.commit()

    return {
        "message": "Task updated successfully"
    }


# ------------------- SOFT DELETE TASK -------------------
@router.delete("/{task_id}")
def soft_delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Only admin can delete tasks"
        )

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.is_deleted = True

    task.deleted_at = datetime.utcnow()

    db.commit()

    return {
        "message": "Task soft deleted successfully"
    }


# ------------------- RESTORE TASK -------------------
@router.put("/restore/{task_id}")
def restore_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Only admin can restore tasks"
        )

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.is_deleted = False

    task.deleted_at = None

    db.commit()

    return {
        "message": "Task restored successfully"
    }