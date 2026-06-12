from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.channels.service import (
    get_workspace_channels,
    get_channel_by_id,
    update_channel,
    archive_channel,
    restore_channel
)
from app.channels.schemas import (
    ChannelCreate,
    ChannelUpdate,
    ChannelResponse
)

from app.channels.schemas import ChannelUpdate

router = APIRouter(
    tags=["Channels"]
)

@router.post("/channels/{workspace_id}")
def create_new_channel(
    workspace_id: int,
    payload: ChannelCreate,
    db: Session = Depends(get_db)
):
    ...

@router.get("/workspaces/{workspace_id}/channels")
def list_workspace_channels(
    workspace_id: int,
    db: Session = Depends(get_db)
):
    return get_workspace_channels(db, workspace_id)


@router.get("/channels/{id}")
def get_channel(
    id: int,
    db: Session = Depends(get_db)
):
    channel = get_channel_by_id(db, id)

    if not channel:
        raise HTTPException(
            status_code=404,
            detail="Channel not found"
        )

    return channel


@router.put("/channels/{id}")
def update_existing_channel(
    id: int,
    data: ChannelUpdate,
    db: Session = Depends(get_db)
):
    channel = update_channel(db, id, data)

    if not channel:
        raise HTTPException(
            status_code=404,
            detail="Channel not found"
        )

    return channel


@router.patch("/channels/{id}/archive")
def archive_existing_channel(
    id: int,
    db: Session = Depends(get_db)
):
    result = archive_channel(db, id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Channel not found"
        )

    return result


@router.patch("/channels/{id}/restore")
def restore_existing_channel(
    id: int,
    db: Session = Depends(get_db)
):
    result = restore_channel(db, id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Channel not found"
        )

    return result