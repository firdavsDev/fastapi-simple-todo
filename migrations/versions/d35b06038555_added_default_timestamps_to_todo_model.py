"""Added default timestamps to Todo model

Revision ID: d35b06038555
Revises: 80f237a3a0e9
Create Date: 2025-04-03 10:27:45.819854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd35b06038555'
down_revision: Union[str, None] = '80f237a3a0e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_todos_id', table_name='todos')
    op.drop_table('todos')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('completed', sa.BOOLEAN(), nullable=True),
    sa.Column('created_at', sa.VARCHAR(), nullable=False),
    sa.Column('updated_at', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_todos_id', 'todos', ['id'], unique=False)
    # ### end Alembic commands ###
