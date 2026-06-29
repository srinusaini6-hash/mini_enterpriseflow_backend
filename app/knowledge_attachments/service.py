from sqlalchemy import select

from sqlalchemy.orm import Session

from app.knowledge_attachments.models import (
    KnowledgeAttachment
)


def create_attachment(
    db: Session,
    payload
):
    attachment = KnowledgeAttachment(
        article_id=payload.article_id,
        file_name=payload.file_name,
        file_path=payload.file_path
    )

    db.add(attachment)
    db.commit()
    db.refresh(attachment)

    return attachment


def get_attachments(
    db: Session
):
    stmt = select(
        KnowledgeAttachment
    )

    return db.execute(
        stmt
    ).scalars().all()


def get_attachment(
    db: Session,
    attachment_id: int
):
    stmt = select(
        KnowledgeAttachment
    ).where(
        KnowledgeAttachment.id == attachment_id
    )

    return db.execute(
        stmt
    ).scalar_one_or_none()


def get_article_attachments(
    db: Session,
    article_id: int
):
    stmt = select(
        KnowledgeAttachment
    ).where(
        KnowledgeAttachment.article_id == article_id
    )

    return db.execute(
        stmt
    ).scalars().all()


def delete_attachment(
    db: Session,
    attachment_id: int
):
    attachment = get_attachment(
        db,
        attachment_id
    )

    if not attachment:
        return None

    db.delete(attachment)
    db.commit()

    return attachment