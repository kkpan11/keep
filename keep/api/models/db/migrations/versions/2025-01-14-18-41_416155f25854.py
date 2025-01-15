"""Add workflowexecution.started index

Revision ID: 416155f25854
Revises: 1c117f1accff
Create Date: 2025-01-14 18:41:45.817371

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "416155f25854"
down_revision = "1c117f1accff"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table("workflowexecution", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_workflowexecution_started"), ["started"], unique=False
        )


def downgrade() -> None:
    with op.batch_alter_table("workflowexecution", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_workflowexecution_started"))