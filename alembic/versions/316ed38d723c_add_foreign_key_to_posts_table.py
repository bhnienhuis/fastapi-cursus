"""add foreign_key to posts table

Revision ID: 316ed38d723c
Revises: fec78b40173e
Create Date: 2022-11-09 15:31:12.057337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '316ed38d723c'
down_revision = 'fec78b40173e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(constraint_name='posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint(constraint_name='posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
