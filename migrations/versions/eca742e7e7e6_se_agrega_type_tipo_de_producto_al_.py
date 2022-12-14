"""Se agrega type, tipo de producto al modelo Message

Revision ID: eca742e7e7e6
Revises: b727a02986d1
Create Date: 2022-12-14 00:12:37.184123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eca742e7e7e6'
down_revision = 'b727a02986d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type_of', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('type_of')

    # ### end Alembic commands ###