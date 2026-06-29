from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.knowledge_comments.schemas import (
    KnowledgeCommentCreate,
    KnowledgeCommentResponse
)

from app.knowledge_comments.service import (
    create_comment,
    get_comments,
    get_comment,
    get_comments_by_article,
    delete_comment
)

router = APIRouter(
    prefix="/knowledge-comments",
    tags=["Knowledge Comments"]
)


@router.post(
    "",
    response_model=KnowledgeCommentResponse
)
def create_new_comment(
    payload: KnowledgeCommentCreate,
    db: Session = Depends(get_db)
):
    return create_comment(db, payload)


@router.get(
    "",
    response_model=list[KnowledgeCommentResponse]
)
def list_comments(
    db: Session = Depends(get_db)
):
    return get_comments(db)


@router.get(
    "/{comment_id}",
    response_model=KnowledgeCommentResponse
)
def get_single_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):
    comment = get_comment(
        db,
        comment_id
    )

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    return comment


@router.get(
    "/article/{article_id}",
    response_model=list[KnowledgeCommentResponse]
)
def comments_by_article(
    article_id: int,
    db: Session = Depends(get_db)
):
    return get_comments_by_article(
        db,
        article_id
    )


@router.delete(
    "/{comment_id}"
)
def remove_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):
    comment = delete_comment(
        db,
        comment_id
    )

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    return {
        "message": "Comment deleted successfully"
    }