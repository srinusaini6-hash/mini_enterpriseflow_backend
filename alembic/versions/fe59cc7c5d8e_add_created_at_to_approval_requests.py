"""add created_at to approval_requests

Revision ID: fe59cc7c5d8e
Revises: af382a4689b6
Create Date: 2026-07-09 20:37:30.262065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe59cc7c5d8e'
down_revision: Union[str, Sequence[str], None] = 'af382a4689b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
