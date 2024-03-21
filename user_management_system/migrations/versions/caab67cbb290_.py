"""empty message

Revision ID: caab67cbb290
Revises: e827978e024d
Create Date: 2020-04-09 16:55:48.391160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caab67cbb290'
down_revision = 'e827978e024d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_details')
    op.drop_table('groups')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('group_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('group_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('last_updated_at', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('group_type', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('function_id', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('group_id', name=u'groups_pkey'),
    sa.UniqueConstraint('group_name', name=u'groups_group_name_key')
    )
    op.create_table('user_details',
    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('login_id', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('department', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('u_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('role_type', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_on', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.VARCHAR(length=700), autoincrement=False, nullable=True),
    sa.Column('personnel_id', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('external_status', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name=u'user_details_pkey'),
    sa.UniqueConstraint('login_id', name=u'user_details_login_id_key'),
    sa.UniqueConstraint('personnel_id', name=u'user_details_personnel_id_key')
    )
    # ### end Alembic commands ###