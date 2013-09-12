"""v0.2

Revision ID: 2ab7af991b87
Revises: None
Create Date: 2013-09-04 22:14:28.552136

"""

# revision identifiers, used by Alembic.
revision = '2ab7af991b87'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dagobah_task', sa.Column('hard_timeout', sa.Integer(),
                                            nullable=False, server_default=sa.text('0')))
    op.add_column('dagobah_task', sa.Column('soft_timeout', sa.Integer(),
                                            nullable=False, server_default=sa.text('0')))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dagobah_task', 'soft_timeout')
    op.drop_column('dagobah_task', 'hard_timeout')
    ### end Alembic commands ###