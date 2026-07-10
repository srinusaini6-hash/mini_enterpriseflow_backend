"""create analytics_snapshots table

Revision ID: 2ced45add9e2
Revises: fe59cc7c5d8e
Create Date: 2026-07-10 17:04:21.645320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ced45add9e2'
down_revision: Union[str, Sequence[str], None] = 'fe59cc7c5d8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
