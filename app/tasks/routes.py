from fastapi import (
    APIRouter,
    Depends,
    Query
)

from sqlalchemy.orm import Session

from fastapi_pagination import (
    Page,
    Params
)

from app.database.database import get_db

from app.tasks.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

from app.auth.dependencies import (
    get_current_user
)

from app.users.models import User

from app.tasks.services import (
    create_task_service,
    get_tasks_service,
    update_task_service,
    soft_delete_task_service,
    restore_task_service
)


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# ------------------- CREATE TASK -------------------

@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_task_service(
        db,
        task,
        current_user
    )


# ------------------- GET TASKS -------------------

@router.get(
    "/",
    response_model=Page[TaskResponse]
)
def get_tasks(

    status: str = Query(None),

    priority: str = Query(None),

    sort_by: str = Query("id"),

    params: Params = Depends(),

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)
):

    return get_tasks_service(
        db,
        status,
        priority,
        sort_by,
        params
    )


# ------------------- UPDATE TASK -------------------

@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return update_task_service(
        db,
        task_id,
        task,
        current_user
    )


# ------------------- SOFT DELETE TASK -------------------

@router.delete("/{task_id}")
def soft_delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return soft_delete_task_service(
        db,
        task_id,
        current_user
    )


# ------------------- RESTORE TASK -------------------

@router.put("/restore/{task_id}")
def restore_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return restore_task_service(
        db,
        task_id,
        current_user
    )