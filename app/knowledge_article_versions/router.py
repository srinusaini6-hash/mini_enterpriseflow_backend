from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.knowledge_article_versions.schemas import (
    KnowledgeArticleVersionCreate,
    KnowledgeArticleVersionResponse
)

from app.knowledge_article_versions.service import (
    create_version,
    get_versions,
    get_version,
    get_versions_by_article,
    delete_version
)

router = APIRouter(
    prefix="/knowledge-versions",
    tags=["Knowledge Versions"]
)


@router.post(
    "",
    response_model=KnowledgeArticleVersionResponse
)
def create_new_version(
    payload: KnowledgeArticleVersionCreate,
    db: Session = Depends(get_db)
):
    return create_version(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[KnowledgeArticleVersionResponse]
)
def list_versions(
    db: Session = Depends(get_db)
):
    return get_versions(db)


@router.get(
    "/{version_id}",
    response_model=KnowledgeArticleVersionResponse
)
def get_single_version(
    version_id: int,
    db: Session = Depends(get_db)
):
    version = get_version(
        db,
        version_id
    )

    if not version:
        raise HTTPException(
            status_code=404,
            detail="Version not found"
        )

    return version


@router.get(
    "/article/{article_id}",
    response_model=list[KnowledgeArticleVersionResponse]
)
def versions_by_article(
    article_id: int,
    db: Session = Depends(get_db)
):
    return get_versions_by_article(
        db,
        article_id
    )


@router.delete(
    "/{version_id}"
)
def remove_version(
    version_id: int,
    db: Session = Depends(get_db)
):
    delete_version(
        db,
        version_id
    )

    return {
        "message": "Version deleted successfully"
    }