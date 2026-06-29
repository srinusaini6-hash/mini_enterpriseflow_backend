from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db

from app.knowledge_search.schemas import (
    KnowledgeSearchCreate,
    KnowledgeSearchResponse
)

from app.knowledge_search.service import (
    KnowledgeSearchService
)
router = APIRouter(
    prefix="/knowledge-search",
    tags=["Knowledge Search"]
)


@router.post(
    "",
    response_model=KnowledgeSearchResponse
)
def create_article(
    data: KnowledgeSearchCreate,
    db: Session = Depends(get_db)
):
    return KnowledgeSearchService.create(db, data)


@router.get(
    "",
    response_model=List[KnowledgeSearchResponse]
)
def get_articles(
    db: Session = Depends(get_db)
):
    return KnowledgeSearchService.get_all(db)


@router.get(
    "/{article_id}",
    response_model=KnowledgeSearchResponse
)
def get_article(
    article_id: int,
    db: Session = Depends(get_db)
):

    article = KnowledgeSearchService.get_by_id(
        db,
        article_id
    )

    if not article:
        raise HTTPException(
            status_code=404,
            detail="Article not found"
        )

    return article


@router.get(
    "/search/{keyword}",
    response_model=List[KnowledgeSearchResponse]
)
def search_article(
    keyword: str,
    db: Session = Depends(get_db)
):
    return KnowledgeSearchService.search(
        db,
        keyword
    )


@router.delete("/{article_id}")
def delete_article(
    article_id: int,
    db: Session = Depends(get_db)
):

    deleted = KnowledgeSearchService.delete(
        db,
        article_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Article not found"
        )

    return {
        "message": "Article deleted successfully"
    }