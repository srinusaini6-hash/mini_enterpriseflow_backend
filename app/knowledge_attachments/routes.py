from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.knowledge_attachments.schemas import (
    KnowledgeAttachmentCreate,
    KnowledgeAttachmentResponse
)

from app.knowledge_attachments.service import (
    create_attachment,
    get_attachments,
    get_attachment,
    get_article_attachments,
    delete_attachment
)

router = APIRouter(
    prefix="/knowledge-attachments",
    tags=["Knowledge Attachments"]
)


@router.post(
    "",
    response_model=KnowledgeAttachmentResponse
)
def create_new_attachment(
    payload: KnowledgeAttachmentCreate,
    db: Session = Depends(get_db)
):
    return create_attachment(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[KnowledgeAttachmentResponse]
)
def list_attachments(
    db: Session = Depends(get_db)
):
    return get_attachments(db)


@router.get(
    "/{attachment_id}",
    response_model=KnowledgeAttachmentResponse
)
def get_single_attachment(
    attachment_id: int,
    db: Session = Depends(get_db)
):
    attachment = get_attachment(
        db,
        attachment_id
    )

    if not attachment:
        raise HTTPException(
            status_code=404,
            detail="Attachment not found"
        )

    return attachment


@router.get(
    "/article/{article_id}",
    response_model=list[KnowledgeAttachmentResponse]
)
def list_article_attachments(
    article_id: int,
    db: Session = Depends(get_db)
):
    return get_article_attachments(
        db,
        article_id
    )


@router.delete(
    "/{attachment_id}"
)
def remove_attachment(
    attachment_id: int,
    db: Session = Depends(get_db)
):
    delete_attachment(
        db,
        attachment_id
    )

    return {
        "message": "Attachment deleted successfully"
    }