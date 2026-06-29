from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.knowledge_tags.schemas import (
    KnowledgeTagCreate,
    KnowledgeTagResponse
)

from app.knowledge_tags.service import (
    create_tag,
    get_tags,
    get_tag,
    get_tags_by_article,
    delete_tag
)

router = APIRouter(
    prefix="/knowledge-tags",
    tags=["Knowledge Tags"]
)


@router.post(
    "",
    response_model=KnowledgeTagResponse
)
def create_new_tag(
    payload: KnowledgeTagCreate,
    db: Session = Depends(get_db)
):
    return create_tag(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[KnowledgeTagResponse]
)
def list_tags(
    db: Session = Depends(get_db)
):
    return get_tags(db)


@router.get(
    "/{tag_id}",
    response_model=KnowledgeTagResponse
)
def get_single_tag(
    tag_id: int,
    db: Session = Depends(get_db)
):
    tag = get_tag(
        db,
        tag_id
    )

    if not tag:
        raise HTTPException(
            status_code=404,
            detail="Tag not found"
        )

    return tag


@router.get(
    "/article/{article_id}",
    response_model=list[KnowledgeTagResponse]
)
def list_tags_by_article(
    article_id: int,
    db: Session = Depends(get_db)
):
    return get_tags_by_article(
        db,
        article_id
    )


@router.delete(
    "/{tag_id}"
)
def remove_tag(
    tag_id: int,
    db: Session = Depends(get_db)
):
    tag = delete_tag(
        db,
        tag_id
    )

    if not tag:
        raise HTTPException(
            status_code=404,
            detail="Tag not found"
        )

    return {
        "message": "Tag deleted successfully"
    }