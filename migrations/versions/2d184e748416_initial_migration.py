"""Initial Migration

Revision ID: 2d184e748416
Revises: 0daedb1edd35
Create Date: 2021-04-28 07:33:04.954891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d184e748416'
down_revision = '0daedb1edd35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=True))
    op.alter_column('pitches', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_pitches_category'), 'pitches', ['category'], unique=False)
    op.create_index(op.f('ix_pitches_name'), 'pitches', ['name'], unique=False)
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    op.drop_index(op.f('ix_pitches_name'), table_name='pitches')
    op.drop_index(op.f('ix_pitches_category'), table_name='pitches')
    op.alter_column('pitches', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###