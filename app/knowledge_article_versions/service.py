from sqlalchemy.orm import Session

from app.knowledge_article_versions.models import (
    KnowledgeArticleVersion
)

from app.knowledge_article_versions.schemas import (
    KnowledgeArticleVersionCreate
)


def create_version(
    db: Session,
    payload: KnowledgeArticleVersionCreate
):
    version = KnowledgeArticleVersion(
        article_id=payload.article_id,
        version_number=payload.version_number,
        content=payload.content
    )

    db.add(version)
    db.commit()
    db.refresh(version)

    return version


def get_versions(db: Session):
    return db.query(
        KnowledgeArticleVersion
    ).all()


def get_version(
    db: Session,
    version_id: int
):
    return db.query(
        KnowledgeArticleVersion
    ).filter(
        KnowledgeArticleVersion.id == version_id
    ).first()


def get_versions_by_article(
    db: Session,
    article_id: int
):
    return db.query(
        KnowledgeArticleVersion
    ).filter(
        KnowledgeArticleVersion.article_id == article_id
    ).all()


def delete_version(
    db: Session,
    version_id: int
):
    version = get_version(
        db,
        version_id
    )

    if version:
        db.delete(version)
        db.commit()