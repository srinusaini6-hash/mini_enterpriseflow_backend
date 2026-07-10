"""task10 analytics tables

Revision ID: 14871cdda492
Revises: 2ced45add9e2
Create Date: 2026-07-10 17:07:00.773845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14871cdda492'
down_revision: Union[str, Sequence[str], None] = '2ced45add9e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
