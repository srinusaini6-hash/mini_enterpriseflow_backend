from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from app.database.database import Base

# Existing Models
from app.users.models import User
from app.tasks.models import Task
from app.attachments.models import Attachment
from app.comments.models import Comment, CommentReply
from app.approvals.models import ApprovalRequest, ApprovalHistory
from app.admin.models import Department, AuditLog
from app.sla.models import SLARule, SLATracking
from app.escalations.models import ApprovalEscalation
from app.delegations.models import ApprovalDelegation
from app.tenants.models import Tenant

# Task 10 Models
from app.analytics.models import AnalyticsSnapshot

# Uncomment ONLY after AIInsight model is created
# from app.ai_insights.models import AIInsight


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata