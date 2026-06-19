"""workflow notifications

Revision ID: 2ffb80ae8da6
Revises: f012733dc490
Create Date: 2026-06-18 18:00:14.115426

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ffb80ae8da6'
down_revision: Union[str, Sequence[str], None] = 'f012733dc490'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
