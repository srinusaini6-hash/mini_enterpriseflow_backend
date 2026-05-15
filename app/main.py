from fastapi import FastAPI

from slowapi.middleware import (
    SlowAPIMiddleware
)

# ---------------- DATABASE ----------------
from app.database.database import (
    engine,
    Base
)

# ---------------- MODELS ----------------
from app.users.models import User

from app.tasks.models import Task

from app.attachments.models import Attachment

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

# ---------------- SLA MODELS ----------------
from app.sla.models import (
    SLARule,
    SLATracking
)

# ---------------- ESCALATION MODELS ----------------
from app.escalations.models import (
    ApprovalEscalation
)

# ---------------- DELEGATION MODELS ----------------
from app.delegations.models import (
    ApprovalDelegation
)

# ---------------- ROUTERS ----------------
from app.auth.routes import (
    router as auth_router
)

from app.tasks.routes import (
    router as task_router
)

from app.notifications.routes import (
    router as notification_router
)

from app.comments.routes import (
    router as comments_router
)

from app.attachments.routes import (
    router as attachment_router
)

from app.approvals.routes import (
    router as approval_router
)

from app.admin.routes import (
    router as admin_router
)

from app.sla.routes import (
    router as sla_router
)

from app.escalations.routes import (
    router as escalation_router
)

from app.delegations.routes import (
    router as delegation_router
)

from app.audit.routes import (
    router as audit_router
)

# ---------------- RATE LIMIT ----------------
from app.middleware.rate_limit import (
    limiter
)

# ---------------- CREATE TABLES ----------------
Base.metadata.create_all(
    bind=engine
)

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

app.include_router(comments_router)

app.include_router(attachment_router)

app.include_router(approval_router)

app.include_router(admin_router)

app.include_router(sla_router)

app.include_router(escalation_router)

app.include_router(delegation_router)

app.include_router(audit_router)

# ---------------- ROOT API ----------------
@app.get("/")
def root():

    return {
        "message": "Mini EnterpriseFlow Backend Running"
    }