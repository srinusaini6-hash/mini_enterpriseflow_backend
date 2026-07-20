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

from app.workflow_templates.models import WorkflowTemplate
from app.workflow_templates.routes import router as workflow_template_router

from app.workflow_steps.models import WorkflowStep
from app.workflow_steps.routes import (
    router as workflow_step_router
)

from app.workflow_conditions.routes import (
    router as workflow_conditions_router
)

from app.workflow_instances.models import WorkflowInstance
from app.workflow_instances.workflow_instance_steps.models import WorkflowInstanceStep

from app.workflow_instances.routes import (
    router as workflow_execution_router
)

from app.workflow_actions.routes import router as workflow_actions_router

from app.workflow_assignments.routes import router as assignment_router

from app.workflow_audit_logs.routes import router as audit_log_router


from app.workflow_notifications.models import WorkflowNotification

from app.workflow_notifications.routes import (
    router as workflow_notification_router
)

from app.workflow_reports.routes import (
    router as workflow_reports_router
)

from app.workflow_dashboard.routes import (
    router as workflow_dashboard_router
)

from app.workflow_analytics.routes import (
    router as workflow_analytics_router
)

from app.knowledge_categories.models import (
    KnowledgeCategory
)

from app.knowledge_categories.routes import (
    router as knowledge_category_router
)

from app.knowledge_articles.models import KnowledgeArticle

from app.knowledge_articles.routes import (
    router as knowledge_article_router
)

from app.knowledge_articles.models import KnowledgeArticle

from app.knowledge_tags.models import KnowledgeTag

from app.knowledge_tags.routes import (
    router as knowledge_tag_router
)

from app.knowledge_attachments.models import (
    KnowledgeAttachment
)

from app.knowledge_attachments.routes import (
    router as knowledge_attachment_router
)

from app.knowledge_article_versions.router import router as knowledge_version_router

from app.knowledge_comments.router import router as knowledge_comments_router

from app.knowledge_ratings.router import (
    router as knowledge_rating_router
)

from app.knowledge_search.models import KnowledgeSearch
from app.knowledge_search.router import router as knowledge_search_router

from app.analytics.routes import router as analytics_router

from app.analytics.routes import router as analytics_router
from app.sla_analytics.routes import router as sla_analytics_router

from app.document_analytics.routes import router as document_analytics_router

from app.productivity_reports.routes import router as productivity_reports_router

from app.report_exports.routes import router as report_exports_router

from app.ai_insights.routes import router as ai_insights_router

from app.integration_providers.routes import (
    router as integration_providers_router,
)

from app.tenant_integrations.routes import (
    router as tenant_integrations_router,
)

from app.integration_credentials.routes import (
    router as integration_credentials_router,
)

from app.webhook_events.routes import (
    router as webhook_events_router,
)

from app.sync_jobs.routes import router as sync_jobs_router

from app.integration_health.routes import router as integration_health_router

from app.integration_audit_logs.routes import (
    router as integration_audit_logs_router,
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
app.include_router(message_router)

app.include_router(
    websocket_router
)

app.include_router(workflow_template_router)

app.include_router(
    workflow_step_router
)

app.include_router(
    workflow_conditions_router
)

app.include_router(
    workflow_execution_router
)

app.include_router(workflow_actions_router)

app.include_router(assignment_router)

app.include_router(audit_log_router)

app.include_router(workflow_notification_router)

app.include_router(
    workflow_reports_router
)

app.include_router(
    workflow_dashboard_router
)

app.include_router(
    workflow_analytics_router
)

app.include_router(
    knowledge_category_router
)

app.include_router(
    knowledge_article_router
)

app.include_router(
    knowledge_tag_router
)

app.include_router(
    knowledge_attachment_router
)

app.include_router(
    knowledge_version_router
)

app.include_router(
    knowledge_comments_router
)

app.include_router(
    knowledge_rating_router
)

app.include_router(
    knowledge_search_router
)

app.include_router(knowledge_search_router)

app.include_router(analytics_router)

app.include_router(analytics_router)
app.include_router(sla_analytics_router)

app.include_router(document_analytics_router)

app.include_router(productivity_reports_router)

app.include_router(report_exports_router)

app.include_router(ai_insights_router)

app.include_router(integration_providers_router)

app.include_router(
    tenant_integrations_router
)

app.include_router(
    integration_credentials_router
)

app.include_router(webhook_events_router)

app.include_router(sync_jobs_router)

app.include_router(integration_health_router)

app.include_router(integration_audit_logs_router)

# ---------------- ENABLE PAGINATION ----------------

add_pagination(app)


# ---------------- ROOT API ----------------

@app.get("/")
def root():

    return {
        "message": "Mini EnterpriseFlow Backend Running"
    }