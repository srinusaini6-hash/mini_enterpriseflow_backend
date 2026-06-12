from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from .schemas import ReactionCreate, ReactionResponse
from .service import create_reaction, get_reactions, delete_reaction

router = APIRouter(
    tags=["Reactions"]
)


@router.post(
    "/messages/{message_id}/reactions",
    response_model=ReactionResponse
)
def add_reaction(
    message_id: int,
    payload: ReactionCreate,
    db: Session = Depends(get_db)
):
    return create_reaction(
        db,
        message_id,
        payload.user_id,
        payload.emoji
    )


@router.get(
    "/messages/{message_id}/reactions",
    response_model=list[ReactionResponse]
)
def list_reactions(
    message_id: int,
    db: Session = Depends(get_db)
):
    return get_reactions(db, message_id)


@router.delete(
    "/messages/{message_id}/reactions/{user_id}"
)
def remove_reaction(
    message_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    delete_reaction(db, message_id, user_id)

    return {
        "message": "Reaction removed successfully"
    }