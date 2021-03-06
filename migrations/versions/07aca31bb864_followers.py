"""followers

Revision ID: 07aca31bb864
Revises: 8e8ed35c6beb
Create Date: 2021-02-07 16:22:45.111586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07aca31bb864'
down_revision = '8e8ed35c6beb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
