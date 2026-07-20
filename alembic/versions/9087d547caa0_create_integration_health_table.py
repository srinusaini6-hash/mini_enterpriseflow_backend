"""create integration_health table

Revision ID: 9087d547caa0
Revises: 1dfed2aa6b2a
Create Date: 2026-07-17 09:51:40.768942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9087d547caa0'
down_revision: Union[str, Sequence[str], None] = '1dfed2aa6b2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
