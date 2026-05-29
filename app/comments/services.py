from fastapi import HTTPException

from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.comments.models import (
    Comment,
    CommentReply
)


# ---------------- ADD COMMENT ----------------

def add_comment_service(
    db: Session,
    data,
    current_user
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

def get_comments_service(
    db: Session,
    task_id: int
):

    query = select(Comment).where(
        Comment.task_id == task_id
    )

    return paginate(
        db,
        query
    )


# ---------------- REPLY COMMENT ----------------

def reply_comment_service(
    db: Session,
    data,
    current_user
):

    comment = db.execute(
        select(Comment).where(
            Comment.id == data.comment_id
        )
    ).scalars().first()

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

    db.refresh(reply)

    return {
        "message": "Reply added successfully"
    }