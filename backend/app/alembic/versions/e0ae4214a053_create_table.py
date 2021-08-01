"""create table

Revision ID: e0ae4214a053
Revises: 
Create Date: 2021-07-31 00:05:45.846426

"""
from sqlalchemy.sql.expression import null
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0ae4214a053'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('petals',
		sa.Column('id', sa.Integer, primary_key=True, index=True),
		sa.Column('sepal_length', sa.Float, nullable=False),
		sa.Column('sepal_width', sa.Float, nullable=False),
		sa.Column('petal_length', sa.Float, nullable=False),
		sa.Column('petal_width', sa.Float, nullable=False),
		sa.Column('prediction', sa.Float, nullable=False),
	)

def downgrade():
  op.drop_table('petals')
