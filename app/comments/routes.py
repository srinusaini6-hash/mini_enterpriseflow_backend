from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.auth.dependencies import get_current_user

from app.users.models import User

from app.comments.models import (
    Comment,
    CommentReply
)

from app.comments.schemas import (
    CommentCreate,
    ReplyCreate
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

    comment = Comment(
        task_id=data.task_id,
        user_id=current_user.id,
        comment_text=data.comment_text
    )

    db.add(comment)

    db.commit()

    db.refresh(comment)

    return {
        "message": "Comment added successfully"
    }


# ---------------- GET COMMENTS ----------------

@router.get("/{task_id}")
def get_comments(
    task_id: int,
    db: Session = Depends(get_db)
):

    comments = db.query(Comment).filter(
        Comment.task_id == task_id
    ).all()

    return comments


# ---------------- REPLY COMMENT ----------------

@router.post("/reply")
def reply_comment(
    data: ReplyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    comment = db.query(Comment).filter(
        Comment.id == data.comment_id
    ).first()

    if not comment:

        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    reply = CommentReply(
        comment_id=data.comment_id,
        user_id=current_user.id,
        reply_text=data.reply_text
    )

    db.add(reply)

    db.commit()

    return {
        "message": "Reply added successfully"
    }