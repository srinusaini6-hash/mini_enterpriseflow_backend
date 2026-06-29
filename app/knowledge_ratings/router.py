from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.knowledge_ratings.schemas import (
    KnowledgeRatingCreate,
    KnowledgeRatingResponse
)

from app.knowledge_ratings.service import (
    create_rating,
    get_ratings,
    get_rating,
    get_ratings_by_article,
    delete_rating
)


router = APIRouter(
    prefix="/knowledge-ratings",
    tags=["Knowledge Ratings"]
)


@router.post(
    "",
    response_model=KnowledgeRatingResponse
)
def create_new_rating(
    payload: KnowledgeRatingCreate,
    db: Session = Depends(get_db)
):
    return create_rating(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[KnowledgeRatingResponse]
)
def list_ratings(
    db: Session = Depends(get_db)
):
    return get_ratings(db)


@router.get(
    "/{rating_id}",
    response_model=KnowledgeRatingResponse
)
def get_single_rating(
    rating_id: int,
    db: Session = Depends(get_db)
):
    rating = get_rating(
        db,
        rating_id
    )

    if not rating:
        raise HTTPException(
            status_code=404,
            detail="Rating not found"
        )

    return rating


@router.get(
    "/article/{article_id}",
    response_model=list[KnowledgeRatingResponse]
)
def ratings_by_article(
    article_id: int,
    db: Session = Depends(get_db)
):
    return get_ratings_by_article(
        db,
        article_id
    )


@router.delete(
    "/{rating_id}"
)
def remove_rating(
    rating_id: int,
    db: Session = Depends(get_db)
):
    delete_rating(
        db,
        rating_id
    )

    return {
        "message": "Rating deleted successfully"
    }