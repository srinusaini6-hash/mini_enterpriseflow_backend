from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect
)

from app.websocket.manager import manager


router = APIRouter(
    tags=["WebSocket Chat"]
)


@router.websocket("/ws/chat/{channel_id}")
async def websocket_chat(
    websocket: WebSocket,
    channel_id: int
):

    await manager.connect(
        channel_id,
        websocket
    )

    try:

        while True:

            data = await websocket.receive_text()

            await manager.broadcast(
                channel_id,
                data
            )

    except WebSocketDisconnect:

        manager.disconnect(
            channel_id,
            websocket
        )