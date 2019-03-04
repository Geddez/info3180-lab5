"""empty message

Revision ID: 667704c81b7c
Revises: 6748a6626e14
Create Date: 2019-02-27 16:35:38.942308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '667704c81b7c'
down_revision = '6748a6626e14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
