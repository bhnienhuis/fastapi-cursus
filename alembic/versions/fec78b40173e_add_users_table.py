"""add users table

Revision ID: fec78b40173e
Revises: 4d60ef4d26d5
Create Date: 2022-11-09 15:16:03.184553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fec78b40173e'
down_revision = '4d60ef4d26d5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
