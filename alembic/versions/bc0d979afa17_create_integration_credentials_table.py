"""create integration_credentials table

Revision ID: bc0d979afa17
Revises: c4d88d001a74
Create Date: 2026-07-14 12:19:57.728991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc0d979afa17'
down_revision: Union[str, Sequence[str], None] = 'c4d88d001a74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
