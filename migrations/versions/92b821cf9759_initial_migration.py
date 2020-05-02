"""Initial Migration

Revision ID: 92b821cf9759
Revises: 
Create Date: 2020-05-02 00:22:43.186318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92b821cf9759'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('en_name', sa.String(length=128), nullable=True),
    sa.Column('en_url', sa.String(length=128), nullable=True),
    sa.Column('de_name', sa.String(length=128), nullable=True),
    sa.Column('de_url', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('en_title', sa.String(length=128), nullable=True),
    sa.Column('de_title', sa.String(length=128), nullable=True),
    sa.Column('en_subtitle', sa.String(length=128), nullable=True),
    sa.Column('de_subtitle', sa.String(length=128), nullable=True),
    sa.Column('en_description', sa.String(length=256), nullable=True),
    sa.Column('de_description', sa.String(length=256), nullable=True),
    sa.Column('en_body', sa.Text(), nullable=True),
    sa.Column('de_body', sa.Text(), nullable=True),
    sa.Column('en_url', sa.String(length=128), nullable=True),
    sa.Column('de_url', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    op.create_table('category_post',
    sa.Column('posts_id', sa.Integer(), nullable=True),
    sa.Column('categories_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categories_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category_post')
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_table('posts')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###