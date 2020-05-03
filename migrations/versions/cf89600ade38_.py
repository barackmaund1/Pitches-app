"""empty message

Revision ID: cf89600ade38
Revises: ee51358a52af
Create Date: 2020-05-03 19:17:29.494702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf89600ade38'
down_revision = 'ee51358a52af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('category', sa.String(length=128), nullable=False))
    op.create_index(op.f('ix_posts_category'), 'posts', ['category'], unique=False)
    op.drop_index('ix_posts_Category', table_name='posts')
    op.drop_column('posts', 'Category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('Category', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.create_index('ix_posts_Category', 'posts', ['Category'], unique=False)
    op.drop_index(op.f('ix_posts_category'), table_name='posts')
    op.drop_column('posts', 'category')
    # ### end Alembic commands ###