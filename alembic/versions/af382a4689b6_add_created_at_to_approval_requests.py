"""add created_at to approval_requests

Revision ID: af382a4689b6
Revises: a56e12742ecc
Create Date: 2026-07-09 20:36:15.302090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af382a4689b6'
down_revision: Union[str, Sequence[str], None] = 'a56e12742ecc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
