"""add content columns to posts table

Revision ID: 4d60ef4d26d5
Revises: 134b64740532
Create Date: 2022-11-09 15:06:45.140944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d60ef4d26d5'
down_revision = '134b64740532'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
