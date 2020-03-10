"""Add borderless_account_id to BankAccount

Revision ID: 57e7d42b95bb
Revises: fa044cbcbf79
Create Date: 2020-03-10 16:24:41.580504

"""

# revision identifiers, used by Alembic.
revision = '57e7d42b95bb'
down_revision = 'fa044cbcbf79'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bank_account', sa.Column('borderless_account_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bank_account', 'borderless_account_id')
    # ### end Alembic commands ###
