from typing import List

from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.channel_members.schemas import (
    ChannelMemberCreate,
    ChannelMemberResponse
)

from app.channel_members.service import (
    add_member,
    list_members,
    remove_member
)

router = APIRouter(
    prefix="/channels",
    tags=["Channel Members"]
)


@router.post(
    "/{channel_id}/members",
    response_model=ChannelMemberResponse
)
def create_member(
    channel_id: int,
    payload: ChannelMemberCreate,
    db: Session = Depends(get_db)
):

    return add_member(
        db,
        channel_id,
        payload.user_id
    )


@router.get(
    "/{channel_id}/members",
    response_model=List[ChannelMemberResponse]
)
def get_members(
    channel_id: int,
    db: Session = Depends(get_db)
):

    return list_members(
        db,
        channel_id
    )


@router.delete(
    "/{channel_id}/members/{user_id}"
)
def delete_member(
    channel_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):

    return remove_member(
        db,
        channel_id,
        user_id
    )