"""Add id_usuario to producto

Revision ID: 3b6a1c9b8f4a
Revises: e32a9af44ebb
Create Date: 2025-11-10 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b6a1c9b8f4a'
down_revision: Union[str, Sequence[str], None] = 'e32a9af44ebb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # No-op: this migration duplicates an existing migration that already added id_usuario.
    # The structural change was applied by another revision; keep this migration as a noop
    # so Alembic can record it as applied without reapplying the ALTER TABLE.
    pass


def downgrade() -> None:
    # No-op downgrade (structural change handled in the other migration)
    pass
