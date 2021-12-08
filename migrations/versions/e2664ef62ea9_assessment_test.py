"""assessment test

Revision ID: e2664ef62ea9
Revises: 36e58b3a3c9b
Create Date: 2021-10-25 19:15:01.430357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2664ef62ea9'
down_revision = '36e58b3a3c9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assessment_code'), 'assessment', ['code'], unique=False)
    op.create_index(op.f('ix_assessment_description'), 'assessment', ['description'], unique=False)
    op.create_index(op.f('ix_assessment_title'), 'assessment', ['title'], unique=False)
    op.drop_index('ix_property_address', table_name='property')
    op.drop_table('property')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('address', sa.VARCHAR(length=500), nullable=True),
    sa.Column('start_date', sa.DATETIME(), nullable=True),
    sa.Column('duration', sa.INTEGER(), nullable=True),
    sa.Column('rent', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_property_address', 'property', ['address'], unique=False)
    op.drop_index(op.f('ix_assessment_title'), table_name='assessment')
    op.drop_index(op.f('ix_assessment_description'), table_name='assessment')
    op.drop_index(op.f('ix_assessment_code'), table_name='assessment')
    op.drop_table('assessment')
    # ### end Alembic commands ###
