from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.active_connections = {}

    async def connect(
        self,
        channel_id: int,
        websocket: WebSocket
    ):
        await websocket.accept()

        if channel_id not in self.active_connections:
            self.active_connections[channel_id] = []

        self.active_connections[channel_id].append(
            websocket
        )

    def disconnect(
        self,
        channel_id: int,
        websocket: WebSocket
    ):
        self.active_connections[channel_id].remove(
            websocket
        )

    async def broadcast(
        self,
        channel_id: int,
        message: str
    ):
        for connection in self.active_connections.get(
            channel_id,
            []
        ):
            await connection.send_text(message)


manager = ConnectionManager()