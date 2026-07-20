"""create webhook_events table

Revision ID: 0e4cf5459d2b
Revises: bc0d979afa17
Create Date: 2026-07-15 10:40:32.020005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e4cf5459d2b'
down_revision: Union[str, Sequence[str], None] = 'bc0d979afa17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
