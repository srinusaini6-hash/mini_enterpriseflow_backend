from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

from app.database.database import Base

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

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata