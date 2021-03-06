"""removed 2 columns from post model

Revision ID: fd07663002fd
Revises: e812a221262e
Create Date: 2021-04-26 14:00:12.782116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd07663002fd'
down_revision = 'e812a221262e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    op.drop_column('post', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
