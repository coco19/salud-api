# -*- coding: utf-8 -*-

"""Eliminación de epicrisis

Revision ID: a450730df33
Revises: 31a5c7944154
Create Date: 2015-10-07 22:53:10.956003

"""

# revision identifiers, used by Alembic.
revision = 'a450730df33'
down_revision = '31a5c7944154'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('epicrisis')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('epicrisis',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('image_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'epicrisis_pkey')
    )
    ### end Alembic commands ###