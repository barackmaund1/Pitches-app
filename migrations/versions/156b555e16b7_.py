"""empty message

Revision ID: 156b555e16b7
Revises: fc1cedce5988
Create Date: 2020-05-04 10:39:56.803842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156b555e16b7'
down_revision = 'fc1cedce5988'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'author',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('posts', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.drop_index('ix_posts_timestamp', table_name='posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_posts_timestamp', 'posts', ['timestamp'], unique=False)
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('posts', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('posts', 'author',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###
