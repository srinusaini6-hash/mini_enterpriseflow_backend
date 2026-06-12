from fastapi import (
    FastAPI,
    HTTPException
)


from fastapi_pagination import (
    add_pagination
)

from slowapi.middleware import (
    SlowAPIMiddleware
)

from app.reactions.models import Reaction

# ---------------- DATABASE ----------------

from app.database.database import (
    engine,
    Base
)


# ---------------- EXCEPTION HANDLER ----------------

from app.core.exception_handler import (
    http_exception_handler
)


# ---------------- RATE LIMIT ----------------

from app.middleware.rate_limit import (
    limiter
)


# ---------------- IMPORT MODELS ----------------

from app.users.models import User

from app.tasks.models import Task

from app.roles.models import Role

from app.permissions.models import Permission

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

from app.sla.models import (
    SLARule,
    SLATracking
)

from app.escalations.models import (
    ApprovalEscalation
)

from app.delegations.models import (
    ApprovalDelegation
)

from app.role_permissions.models import RolePermission

from app.tenants.models import Tenant

from app.notifications.models import Notification

from app.subscriptions.models import (
    SubscriptionPlan,
    TenantSubscription
)

# ---------------- IMPORT ROUTERS ----------------
from app.users.routes import router as user_router

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

from app.tenants.routes import (
    router as tenant_router
)

from app.subscriptions.routes import (
    router as subscription_router
)

from app.tenant_subscriptions.routes import (
    router as tenant_subscription_router
)

from app.roles.routes import (
    router as role_router
)

from app.permissions.routes import (
    router as permission_router
)

from app.role_permissions.routes import (
    router as role_permission_router
)

from app.meetings.routes import router as meetings_router

from app.meeting_attendees.routes import router as meeting_attendees_router

from app.availability.router import router as availability_router

from app.meeting_notes.router import router as meeting_notes_router

from app.action_items.router import router as action_items_router

from app.reminders.routes import router as reminder_router

from app.ai_summary.routes import router as ai_summary_router

from app.workspaces.routes import router as workspace_router

from app.workspace_members.routes import router as workspace_member_router

from app.channels.routes import router as channel_router

from app.channel_members.routes import router as channel_member_router

from app.messages.routes import router as message_router

from app.reactions.routes import router as reaction_router

from app.replies.models import Reply
from app.replies.routes import router as reply_router

from app.read_receipts.models import ReadReceipt
from app.read_receipts.routes import router as read_receipt_router

from app.message_pins.models import MessagePin
from app.message_pins.routes import router as message_pin_router

from app.conversations.routes import router as conversation_router

from app.message_mentions.router import router as mention_router

from app.presence_status.models import PresenceStatus
from app.presence_status.routes import router as presence_router

from app.message_search.router import router as message_search_router
from app.messages.routes import router as message_router

from app.websocket.routes import (
    router as websocket_router
)

# ---------------- CREATE FASTAPI APP ----------------

app = FastAPI(
    title="Mini EnterpriseFlow Backend",
    version="1.0.0"
)


# ---------------- RATE LIMITER ----------------

app.state.limiter = limiter

app.add_middleware(
    SlowAPIMiddleware
)


# ---------------- EXCEPTION HANDLER ----------------

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)


# ---------------- CREATE DATABASE TABLES ----------------

Base.metadata.create_all(
    bind=engine
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

app.include_router(tenant_router)

app.include_router(subscription_router)

app.include_router(
    tenant_subscription_router
)

app.include_router(role_router)

app.include_router(permission_router)

app.include_router(role_permission_router)

app.include_router(user_router)

app.include_router(meetings_router)

app.include_router(meeting_attendees_router)

app.include_router(availability_router)

app.include_router(meeting_notes_router)

app.include_router(action_items_router)

app.include_router(reminder_router)

app.include_router(ai_summary_router)

app.include_router(workspace_router)

app.include_router(workspace_member_router)

app.include_router(channel_router)

app.include_router(channel_member_router)

app.include_router(message_router)

app.include_router(reaction_router)

app.include_router(reply_router)

app.include_router(read_receipt_router)

app.include_router(message_pin_router)

app.include_router(conversation_router)

app.include_router(mention_router)

app.include_router(presence_router)

app.include_router(message_search_router)

app.include_router(message_search_router)
app.include_router(message_router)

app.include_router(
    websocket_router
)


# ---------------- ENABLE PAGINATION ----------------

add_pagination(app)


# ---------------- ROOT API ----------------

@app.get("/")
def root():

    return {
        "message": "Mini EnterpriseFlow Backend Running"
    }