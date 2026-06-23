from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.knowledge_categories.schemas import (
    KnowledgeCategoryCreate,
    KnowledgeCategoryUpdate,
    KnowledgeCategoryResponse
)

from app.knowledge_categories.service import (
    create_category,
    get_categories,
    get_category,
    update_category,
    delete_category
)

router = APIRouter(
    prefix="/knowledge/categories",
    tags=["Knowledge Categories"]
)


@router.post(
    "",
    response_model=KnowledgeCategoryResponse
)
def create_category_api(
    payload: KnowledgeCategoryCreate,
    db: Session = Depends(get_db)
):
    return create_category(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[KnowledgeCategoryResponse]
)
def list_categories(
    db: Session = Depends(get_db)
):
    return get_categories(db)


@router.get(
    "/{category_id}",
    response_model=KnowledgeCategoryResponse
)
def get_category_api(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = get_category(
        db,
        category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.put(
    "/{category_id}",
    response_model=KnowledgeCategoryResponse
)
def update_category_api(
    category_id: int,
    payload: KnowledgeCategoryUpdate,
    db: Session = Depends(get_db)
):
    category = update_category(
        db,
        category_id,
        payload
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.delete(
    "/{category_id}"
)
def delete_category_api(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = delete_category(
        db,
        category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message": "Category disabled successfully"
    }