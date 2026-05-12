from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.saved_filters.models import SavedFilter

from app.auth.dependencies import get_current_user

from app.users.models import User


router = APIRouter(
    prefix="/filters",
    tags=["Saved Filters"]
)


# ---------------- CREATE FILTER ----------------
@router.post("/")
def create_filter(
    filter_name: str,
    filter_data: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_filter = SavedFilter(
        user_id=current_user.id,
        filter_name=filter_name,
        filter_data=filter_data
    )

    db.add(new_filter)

    db.commit()

    db.refresh(new_filter)

    return {
        "message": "Filter saved successfully"
    }


# ---------------- GET FILTERS ----------------
@router.get("/")
def get_filters(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    filters = db.query(SavedFilter).filter(
        SavedFilter.user_id == current_user.id
    ).all()

    return filters


# ---------------- DELETE FILTER ----------------
@router.delete("/{filter_id}")
def delete_filter(
    filter_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    saved_filter = db.query(SavedFilter).filter(
        SavedFilter.id == filter_id
    ).first()

    if not saved_filter:
        raise HTTPException(
            status_code=404,
            detail="Filter not found"
        )

    db.delete(saved_filter)

    db.commit()

    return {
        "message": "Filter deleted successfully"
    }