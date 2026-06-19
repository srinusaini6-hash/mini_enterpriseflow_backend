"""workflow audit logs

Revision ID: f012733dc490
Revises: 665db87d3257
Create Date: 2026-06-18 11:08:22.319270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f012733dc490'
down_revision: Union[str, Sequence[str], None] = '665db87d3257'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
