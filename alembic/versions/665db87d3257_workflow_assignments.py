"""workflow assignments

Revision ID: 665db87d3257
Revises: 686dad163faa
Create Date: 2026-06-18 10:28:14.043973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '665db87d3257'
down_revision: Union[str, Sequence[str], None] = '686dad163faa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
