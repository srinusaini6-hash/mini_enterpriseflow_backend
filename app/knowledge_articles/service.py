from sqlalchemy import select
from sqlalchemy.orm import Session

from app.knowledge_articles.models import (
    KnowledgeArticle
)


def create_article(
    db: Session,
    payload
):
    article = KnowledgeArticle(
        tenant_id=payload.tenant_id,
        category_id=payload.category_id,
        title=payload.title,
        content=payload.content,
        author_id=payload.author_id,
        status=payload.status,
        is_published=payload.is_published
    )

    db.add(article)
    db.commit()
    db.refresh(article)

    return article


def get_articles(
    db: Session
):
    stmt = select(KnowledgeArticle)

    result = db.execute(stmt)

    return result.scalars().all()


def get_article(
    db: Session,
    article_id: int
):
    stmt = select(
        KnowledgeArticle
    ).where(
        KnowledgeArticle.id == article_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()


def update_article(
    db: Session,
    article_id: int,
    payload
):
    article = get_article(
        db,
        article_id
    )

    if not article:
        return None

    article.title = payload.title
    article.content = payload.content
    article.status = payload.status
    article.is_published = payload.is_published

    db.commit()
    db.refresh(article)

    return article


def delete_article(
    db: Session,
    article_id: int
):
    article = get_article(
        db,
        article_id
    )

    if not article:
        return None

    db.delete(article)
    db.commit()

    return True


def get_articles_by_category(
    db: Session,
    category_id: int
):
    stmt = select(
        KnowledgeArticle
    ).where(
        KnowledgeArticle.category_id == category_id
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_published_articles(
    db: Session
):
    stmt = select(
        KnowledgeArticle
    ).where(
        KnowledgeArticle.is_published.is_(True)
    )

    result = db.execute(stmt)

    return result.scalars().all()