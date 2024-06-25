"""Add description col in uploads table

Revision ID: bfb17969c4ed
Revises: c3dc42618662
Create Date: 2024-06-22 15:57:45.897306

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'bfb17969c4ed'
down_revision = 'c3dc42618662'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upload', sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.execute('UPDATE upload SET description = name WHERE description IS NULL')
    op.alter_column('upload', 'description', nullable=False)
    op.drop_column('upload', 'path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upload', sa.Column('path', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('upload', 'description')
    # ### end Alembic commands ###
