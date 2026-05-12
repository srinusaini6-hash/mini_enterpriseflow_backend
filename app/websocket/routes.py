from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect
)

from app.websocket.manager import manager


router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"]
)


# ---------------- WEBSOCKET CONNECTION ----------------
@router.websocket("/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: int
):

    # Connect User
    await manager.connect(
        user_id,
        websocket
    )

    try:

        while True:

            # Receive message from client
            data = await websocket.receive_text()

            print(f"Message from User {user_id}: {data}")

            # Send response back
            await websocket.send_text(
                f"Real-time message received: {data}"
            )

    except WebSocketDisconnect:

        # Disconnect user
        manager.disconnect(user_id)

        print(f"User {user_id} disconnected")