"""Merge migration for e2701d47ba6e and 3b6a1c9b8f4a

Revision ID: mrg_e2701_3b6a1
Revises: e2701d47ba6e,3b6a1c9b8f4a
Create Date: 2025-11-10 00:30:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'mrg_e2701_3b6a1'
down_revision: Union[str, Sequence[str], None] = ('e2701d47ba6e','3b6a1c9b8f4a')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Merge migration: no schema changes, just resolves multiple heads
    pass


def downgrade() -> None:
    # Non-destructive downgrade is not implemented for merge
    pass
