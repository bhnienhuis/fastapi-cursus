"""add last few columns to posts table

Revision ID: 547807e0364b
Revises: 316ed38d723c
Create Date: 2022-11-09 15:42:52.679719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '547807e0364b'
down_revision = '316ed38d723c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
