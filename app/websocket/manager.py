from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):

        self.active_connections = {}


    # ---------------- CONNECT ----------------
    async def connect(
        self,
        user_id: int,
        websocket: WebSocket
    ):

        await websocket.accept()

        self.active_connections[user_id] = websocket

        print(f"User {user_id} connected")


    # ---------------- DISCONNECT ----------------
    def disconnect(
        self,
        user_id: int
    ):

        if user_id in self.active_connections:

            del self.active_connections[user_id]

            print(f"User {user_id} disconnected")


    # ---------------- SEND PERSONAL MESSAGE ----------------
    async def send_personal_message(
        self,
        user_id: int,
        message: str
    ):

        websocket = self.active_connections.get(user_id)

        if websocket:

            await websocket.send_text(message)


# Create manager object
manager = ConnectionManager()