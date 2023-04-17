"""status

Revision ID: 836a5f803c4d
Revises: 4d9562314bd3
Create Date: 2023-04-11 03:17:06.459499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836a5f803c4d'
down_revision = '4d9562314bd3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table('document', schema=None) as batch_op:
            batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))
    except Exception as e:
        print(e)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table('document', schema=None) as batch_op:
            batch_op.drop_column('is_active')
    except Exception as e:
        print(e)
    # ### end Alembic commands ###