from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.knowledge_articles.schemas import (
    KnowledgeArticleCreate,
    KnowledgeArticleUpdate,
    KnowledgeArticleResponse
)

from app.knowledge_articles.service import (
    create_article,
    get_articles,
    get_article,
    update_article,
    delete_article,
    get_articles_by_category,
    get_published_articles
)

router = APIRouter(
    prefix="/knowledge-articles",
    tags=["Knowledge Articles"]
)


@router.post(
    "",
    response_model=KnowledgeArticleResponse
)
def create_new_article(
    payload: KnowledgeArticleCreate,
    db: Session = Depends(get_db)
):
    return create_article(db, payload)


@router.get(
    "",
    response_model=list[KnowledgeArticleResponse]
)
def list_articles(
    db: Session = Depends(get_db)
):
    return get_articles(db)


@router.get(
    "/published",
    response_model=list[KnowledgeArticleResponse]
)
def published_articles(
    db: Session = Depends(get_db)
):
    return get_published_articles(db)


@router.get(
    "/category/{category_id}",
    response_model=list[KnowledgeArticleResponse]
)
def articles_by_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return get_articles_by_category(
        db,
        category_id
    )


@router.get(
    "/{article_id}",
    response_model=KnowledgeArticleResponse
)
def get_single_article(
    article_id: int,
    db: Session = Depends(get_db)
):
    article = get_article(
        db,
        article_id
    )

    if not article:
        raise HTTPException(
            status_code=404,
            detail="Article not found"
        )

    return article


@router.put(
    "/{article_id}",
    response_model=KnowledgeArticleResponse
)
def update_existing_article(
    article_id: int,
    payload: KnowledgeArticleUpdate,
    db: Session = Depends(get_db)
):
    article = update_article(
        db,
        article_id,
        payload
    )

    if not article:
        raise HTTPException(
            status_code=404,
            detail="Article not found"
        )

    return article


@router.delete(
    "/{article_id}"
)
def delete_existing_article(
    article_id: int,
    db: Session = Depends(get_db)
):
    article = delete_article(
        db,
        article_id
    )

    if not article:
        raise HTTPException(
            status_code=404,
            detail="Article not found"
        )

    return {
        "message": "Article deleted successfully"
    }