"""empty message

Revision ID: 85c2437114a0
Revises: d8c792fcdaca
Create Date: 2024-10-02 21:45:54.633395

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '85c2437114a0'
down_revision = 'd8c792fcdaca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('socios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('tipo_precio', sa.String(length=100), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('periodos_espera', sa.Float(), nullable=False),
    sa.Column('incluir_peajes', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('socio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('socio',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('tipo_precio', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('precio', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('periodos_espera', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('incluir_peajes', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='socio_pkey'),
    sa.UniqueConstraint('email', name='socio_email_key')
    )
    op.drop_table('socios')
    # ### end Alembic commands ###
