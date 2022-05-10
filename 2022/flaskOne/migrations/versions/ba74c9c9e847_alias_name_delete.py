"""alias name delete

Revision ID: ba74c9c9e847
Revises: 
Create Date: 2022-05-06 23:27:42.843176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba74c9c9e847'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_reimbursement_timestamp'), 'reimbursement', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reimbursement_timestamp'), table_name='reimbursement')
    # ### end Alembic commands ###
