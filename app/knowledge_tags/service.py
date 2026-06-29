from sqlalchemy import select
from sqlalchemy.orm import Session

from app.knowledge_tags.models import (
    KnowledgeTag
)


def create_tag(
    db: Session,
    payload
):
    tag = KnowledgeTag(
        article_id=payload.article_id,
        tag_name=payload.tag_name
    )

    db.add(tag)
    db.commit()
    db.refresh(tag)

    return tag


def get_tags(
    db: Session
):
    stmt = select(KnowledgeTag)

    result = db.execute(stmt)

    return result.scalars().all()


def get_tag(
    db: Session,
    tag_id: int
):
    stmt = select(
        KnowledgeTag
    ).where(
        KnowledgeTag.id == tag_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()


def get_tags_by_article(
    db: Session,
    article_id: int
):
    stmt = select(
        KnowledgeTag
    ).where(
        KnowledgeTag.article_id == article_id
    )

    result = db.execute(stmt)

    return result.scalars().all()


def delete_tag(
    db: Session,
    tag_id: int
):
    tag = get_tag(
        db,
        tag_id
    )

    if not tag:
        return None

    db.delete(tag)

    db.commit()

    return True