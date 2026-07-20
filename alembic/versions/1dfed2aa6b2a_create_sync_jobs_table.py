"""create sync_jobs table

Revision ID: 1dfed2aa6b2a
Revises: 0e4cf5459d2b
Create Date: 2026-07-16 17:02:05.206313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1dfed2aa6b2a'
down_revision: Union[str, Sequence[str], None] = '0e4cf5459d2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
