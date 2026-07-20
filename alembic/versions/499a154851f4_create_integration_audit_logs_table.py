"""create integration_audit_logs table

Revision ID: 499a154851f4
Revises: 9087d547caa0
Create Date: 2026-07-20 11:49:19.131650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '499a154851f4'
down_revision: Union[str, Sequence[str], None] = '9087d547caa0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
