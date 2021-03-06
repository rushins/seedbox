"""empty message

Revision ID: f08e29e85dc0
Revises: 92f518191c12
Create Date: 2017-04-28 15:48:06.677425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f08e29e85dc0'
down_revision = '92f518191c12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cluster', 'etcd_version')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cluster', sa.Column('etcd_version', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
