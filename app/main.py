from fastapi import FastAPI

from slowapi.middleware import SlowAPIMiddleware

# ---------------- DATABASE ----------------
from app.database.database import (
    engine,
    Base
)

# ---------------- MODELS ----------------
from app.users.models import User
from app.tasks.models import Task
from app.documents.models import Document
from app.attachments.models import Attachment
from app.history.models import TaskHistory

from app.comments.models import (
    Comment,
    CommentReply
)

from app.approvals.models import (
    ApprovalRequest,
    ApprovalHistory
)

from app.admin.models import (
    Department,
    AuditLog
)

# ---------------- ROUTERS ----------------
from app.auth.routes import router as auth_router

from app.tasks.routes import router as task_router

from app.notifications.routes import (
    router as notification_router
)

from app.websocket.routes import (
    router as websocket_router
)

from app.comments.routes import (
    router as comments_router
)

from app.attachments.routes import (
    router as attachment_router
)

from app.history.routes import (
    router as history_router
)

from app.saved_filters.routes import (
    router as filter_router
)

from app.exports.routes import (
    router as export_router
)

from app.background.routes import (
    router as background_router
)

from app.documents.routes import (
    router as document_router
)

from app.approvals.routes import (
    router as approval_router
)

from app.admin.routes import (
    router as admin_router
)

from app.dashboard.routes import (
    router as dashboard_router
)

from app.realtime.websocket import (
    router as ws_router
)

# ---------------- RATE LIMIT ----------------
from app.middleware.rate_limit import limiter


# ---------------- CREATE TABLES ----------------
Base.metadata.create_all(bind=engine)


# ---------------- FASTAPI APP ----------------
app = FastAPI(
    title="Mini EnterpriseFlow Backend"
)


# ---------------- RATE LIMITER ----------------
app.state.limiter = limiter

app.add_middleware(
    SlowAPIMiddleware
)


# ---------------- INCLUDE ROUTERS ----------------
app.include_router(auth_router)

app.include_router(task_router)

app.include_router(notification_router)

app.include_router(websocket_router)

app.include_router(comments_router)

app.include_router(attachment_router)

app.include_router(history_router)

app.include_router(filter_router)

app.include_router(export_router)

app.include_router(background_router)

app.include_router(document_router)

app.include_router(approval_router)

app.include_router(admin_router)

app.include_router(dashboard_router)

app.include_router(ws_router)


# ---------------- ROOT API ----------------
@app.get("/")
def root():

    return {
        "message": "Mini EnterpriseFlow Backend Running"
    }