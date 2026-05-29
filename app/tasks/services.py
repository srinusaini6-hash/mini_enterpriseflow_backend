from datetime import datetime

from fastapi import HTTPException

from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination import Params

from fastapi_pagination.ext.sqlalchemy import paginate

from app.tasks.models import Task

from app.notifications.services import (
    create_notification
)


VALID_STATUSES = [
    "TODO",
    "IN_PROGRESS",
    "REVIEW",
    "DONE"
]


# ---------------- CREATE TASK ----------------

def create_task_service(
    db: Session,
    task,
    current_user
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
        db=db,
        user_id=new_task.assigned_to,
        message=f"New task assigned: {new_task.title}"
    )

    return {
        "message": "Task created successfully",
        "task_id": new_task.id
    }


# ---------------- GET TASKS ----------------

def get_tasks_service(
    db: Session,
    status=None,
    priority=None,
    sort_by=None,
    params: Params = None
):

    query = select(Task).where(
        Task.is_deleted == False
    )

    # FILTER STATUS
    if status:

        query = query.where(
            Task.status == status
        )

    # FILTER PRIORITY
    if priority:

        query = query.where(
            Task.priority == priority
        )

    # SORTING
    if sort_by == "title":

        query = query.order_by(
            Task.title
        )

    elif sort_by == "priority":

        query = query.order_by(
            Task.priority
        )

    else:

        query = query.order_by(
            Task.id
        )

    return paginate(
        db,
        query,
        params
    )


# ---------------- UPDATE TASK ----------------

def update_task_service(
    db: Session,
    task_id: int,
    task,
    current_user
):

    existing_task = db.execute(
        select(Task).where(
            Task.id == task_id,
            Task.is_deleted == False
        )
    ).scalars().first()

    if not existing_task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # VALIDATE STATUS
    if (
        task.status
        and task.status not in VALID_STATUSES
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    # AUTHORIZATION
    if (
        current_user.role != "admin"
        and existing_task.assigned_to != current_user.id
    ):

        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    # UPDATE VALUES
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.priority = task.priority
    existing_task.status = task.status

    db.commit()

    db.refresh(existing_task)

    return {
        "message": "Task updated successfully"
    }


# ---------------- SOFT DELETE TASK ----------------

def soft_delete_task_service(
    db: Session,
    task_id: int,
    current_user
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Only admin can delete tasks"
        )

    task = db.execute(
        select(Task).where(
            Task.id == task_id
        )
    ).scalars().first()

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


# ---------------- RESTORE TASK ----------------

def restore_task_service(
    db: Session,
    task_id: int,
    current_user
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Only admin can restore tasks"
        )

    task = db.execute(
        select(Task).where(
            Task.id == task_id
        )
    ).scalars().first()

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