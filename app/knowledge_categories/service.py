from sqlalchemy import select

from sqlalchemy.orm import Session

from app.knowledge_categories.models import (
    KnowledgeCategory
)


def create_category(
    db: Session,
    payload
):
    category = KnowledgeCategory(
        tenant_id=payload.tenant_id,
        name=payload.name,
        description=payload.description,
        created_by=payload.created_by
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_categories(
    db: Session
):
    stmt = select(
        KnowledgeCategory
    ).where(
        KnowledgeCategory.is_active.is_(True)
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_category(
    db: Session,
    category_id: int
):
    stmt = select(
        KnowledgeCategory
    ).where(
        KnowledgeCategory.id == category_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()


def update_category(
    db: Session,
    category_id: int,
    payload
):
    category = get_category(
        db,
        category_id
    )

    if not category:
        return None

    category.name = payload.name
    category.description = payload.description
    category.is_active = payload.is_active

    db.commit()
    db.refresh(category)

    return category


def delete_category(
    db: Session,
    category_id: int
):
    category = get_category(
        db,
        category_id
    )

    if not category:
        return None

    category.is_active = False

    db.commit()
    db.refresh(category)

    return category