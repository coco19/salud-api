# -*- coding: utf-8 -*-

"""Creación de permisos para análisis

Revision ID: 1bd92883a744
Revises: a450730df33
Create Date: 2015-10-15 00:35:06.392273

"""

# revision identifiers, used by Alembic.
revision = '1bd92883a744'
down_revision = 'a450730df33'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permission_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('can_view_analysis_files', sa.Boolean(), nullable=True),
    sa.Column('can_view_measurements', sa.Boolean(), nullable=True),
    sa.Column('can_edit_analysis_files', sa.Boolean(), nullable=True),
    sa.Column('can_edit_measurements', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('analysis_id', sa.Integer(), nullable=True),
    sa.Column('permission_type_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['analysis_id'], ['analysis.id'], ),
    sa.ForeignKeyConstraint(['permission_type_id'], ['permission_type.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permission')
    op.drop_table('permission_type')
    ### end Alembic commands ###