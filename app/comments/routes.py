from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.users.models import User

from app.comments.schemas import (
    CommentCreate,
    ReplyCreate,
    CommentResponse
)

from app.comments.services import (
    add_comment_service,
    get_comments_service,
    reply_comment_service
)

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


# ---------------- ADD COMMENT ----------------

@router.post("/")
def add_comment(
    data: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return add_comment_service(
        db,
        data,
        current_user
    )


# ---------------- GET COMMENTS ----------------

@router.get(
    "/{task_id}",
    response_model=Page[CommentResponse]
)
def get_comments(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_comments_service(
        db,
        task_id
    )


# ---------------- REPLY COMMENT ----------------

@router.post("/reply")
def reply_comment(
    data: ReplyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return reply_comment_service(
        db,
        data,
        current_user
    )