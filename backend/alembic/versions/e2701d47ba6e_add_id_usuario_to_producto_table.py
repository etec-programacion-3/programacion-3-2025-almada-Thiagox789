"""Add id_usuario to producto table

Revision ID: e2701d47ba6e
Revises: e32a9af44ebb
Create Date: 2025-11-10 17:15:33.310825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2701d47ba6e'
down_revision: Union[str, Sequence[str], None] = 'e32a9af44ebb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_usuario', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_producto_usuario',  # nombre explícito de la FK
            'usuario',              # tabla referenciada
            ['id_usuario'],         # columna local
            ['id_usuario']          # columna remota correcta
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_producto_usuario', type_='foreignkey')
        batch_op.drop_column('id_usuario')
