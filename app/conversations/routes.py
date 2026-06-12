from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from .schemas import (
    ConversationCreate,
    ConversationResponse,
    MemberCreate,
    MemberResponse
)

from .service import (
    create_conversation,
    get_conversations,
    get_conversation,
    add_member,
    get_members,
    remove_member
)

router = APIRouter(
    prefix="",
    tags=["Conversations"]
)


@router.post(
    "/conversations",
    response_model=ConversationResponse
)
def create_new_conversation(
    data: ConversationCreate,
    db: Session = Depends(get_db)
):
    return create_conversation(db, data)


@router.get(
    "/conversations",
    response_model=list[ConversationResponse]
)
def list_conversations(
    db: Session = Depends(get_db)
):
    return get_conversations(db)


@router.get(
    "/conversations/{conversation_id}",
    response_model=ConversationResponse
)
def get_single_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    obj = get_conversation(
        db,
        conversation_id
    )

    if not obj:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return obj


@router.post(
    "/conversations/{conversation_id}/members",
    response_model=MemberResponse
)
def add_conversation_member(
    conversation_id: int,
    data: MemberCreate,
    db: Session = Depends(get_db)
):
    return add_member(
        db,
        conversation_id,
        data.user_id
    )


@router.get(
    "/conversations/{conversation_id}/members",
    response_model=list[MemberResponse]
)
def list_conversation_members(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    return get_members(
        db,
        conversation_id
    )


@router.delete(
    "/conversations/{conversation_id}/members/{user_id}"
)
def delete_member(
    conversation_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    remove_member(
        db,
        conversation_id,
        user_id
    )

    return {
        "message": "Member removed successfully"
    }