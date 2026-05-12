from fastapi import HTTPException
import time

request_count = {}

def rate_limit(user_id: int):
    now = int(time.time())

    if user_id not in request_count:
        request_count[user_id] = []

    request_count[user_id] = [
        t for t in request_count[user_id] if now - t < 60
    ]

    if len(request_count[user_id]) > 20:
        raise HTTPException(status_code=429, detail="Too many requests")

    request_count[user_id].append(now)