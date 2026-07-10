"""create analytics and ai insights tables

Revision ID: a56e12742ecc
Revises: 28ec2ba1d836
Create Date: 2026-07-09 18:23:56.094331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a56e12742ecc'
down_revision: Union[str, Sequence[str], None] = '28ec2ba1d836'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
