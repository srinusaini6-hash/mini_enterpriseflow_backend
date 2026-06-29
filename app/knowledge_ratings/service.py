from sqlalchemy.orm import Session

from app.knowledge_ratings.model import (
    KnowledgeRating
)

from app.knowledge_ratings.schemas import (
    KnowledgeRatingCreate
)


def create_rating(
    db: Session,
    payload: KnowledgeRatingCreate
):
    rating = KnowledgeRating(
        **payload.dict()
    )

    db.add(rating)
    db.commit()
    db.refresh(rating)

    return rating


def get_ratings(
    db: Session
):
    return db.query(
        KnowledgeRating
    ).all()


def get_rating(
    db: Session,
    rating_id: int
):
    return db.query(
        KnowledgeRating
    ).filter(
        KnowledgeRating.id == rating_id
    ).first()


def get_ratings_by_article(
    db: Session,
    article_id: int
):
    return db.query(
        KnowledgeRating
    ).filter(
        KnowledgeRating.article_id == article_id
    ).all()


def delete_rating(
    db: Session,
    rating_id: int
):
    rating = get_rating(
        db,
        rating_id
    )

    if rating:
        db.delete(rating)
        db.commit()