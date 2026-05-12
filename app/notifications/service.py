from app.websocket.manager import manager
from app.notifications.models import Notification
import asyncio

def create_notification(db, user_id, message):
    notification = Notification(
        user_id=user_id,
        message=message
    )

    db.add(notification)
    db.commit()

    try:
        # ✅ Correct way
        asyncio.create_task(
            manager.send_notification(user_id, message)
        )
    except RuntimeError:
        # fallback if no running loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            manager.send_notification(user_id, message)
        )