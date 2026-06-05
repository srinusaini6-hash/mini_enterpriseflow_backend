from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.action_items.schemas import (
    ActionItemCreate,
    ConvertToTaskRequest
)

from app.action_items.service import (
    ActionItemService
)

router = APIRouter(
    prefix="/action-items",
    tags=["Action Items"]
)


@router.post("/{meeting_id}")
def create_action_item(
    meeting_id: int,
    payload: ActionItemCreate,
    db: Session = Depends(get_db)
):

    return ActionItemService.create_action_item(
        db=db,
        meeting_id=meeting_id,
        payload=payload
    )


@router.get("/{meeting_id}")
def get_action_items(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    return ActionItemService.get_action_items(
        db=db,
        meeting_id=meeting_id
    )


@router.patch("/{action_item_id}/convert")
def convert_to_task(
    action_item_id: int,
    payload: ConvertToTaskRequest,
    db: Session = Depends(get_db)
):

    return ActionItemService.convert_to_task(
        db=db,
        action_item_id=action_item_id,
        task_id=payload.task_id
    )