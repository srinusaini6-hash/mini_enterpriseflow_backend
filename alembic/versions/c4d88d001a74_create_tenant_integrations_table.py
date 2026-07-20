"""create tenant_integrations table

Revision ID: c4d88d001a74
Revises: dccac7893257
Create Date: 2026-07-13 16:56:19.495202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4d88d001a74'
down_revision: Union[str, Sequence[str], None] = 'dccac7893257'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
