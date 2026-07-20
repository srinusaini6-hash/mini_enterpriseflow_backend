"""create integration_providers table

Revision ID: dccac7893257
Revises: 14871cdda492
Create Date: 2026-07-13 16:22:49.941766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dccac7893257'
down_revision: Union[str, Sequence[str], None] = '14871cdda492'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
