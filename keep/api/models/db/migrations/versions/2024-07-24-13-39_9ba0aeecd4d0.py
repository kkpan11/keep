"""For AI

Revision ID: 9ba0aeecd4d0
Revises: dcbd2873dcfd
Create Date: 2024-07-24 13:39:10.576538

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "9ba0aeecd4d0"
down_revision = "dcbd2873dcfd"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "pmimatrix",
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("fingerprint_i", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("fingerprint_j", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("pmi", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenant.id"],
        ),
        sa.PrimaryKeyConstraint("fingerprint_i", "fingerprint_j"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("pmimatrix")
    # ### end Alembic commands ###
