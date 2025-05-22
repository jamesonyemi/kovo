"""modified enum list

Revision ID: 3315122c9444
Revises: bc0c5253b167
Create Date: 2025-05-22 09:59:10.516545

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3315122c9444'
down_revision = 'bc0c5253b167'
branch_labels = None
depends_on = None


def upgrade():
    # 1. Create new ENUM types
    op.create_enum('project_status', 'planning', 'in_progress', 'completed', 'cancelled', 'delayed', 'overdue', 'on_hold', 'postponed')
    op.create_enum('task_status', 'pending', 'in_progress', 'completed', 'cancelled')

    # 2. Modify `project` table
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('status', sa.Enum('planning', 'in_progress', 'completed', 'cancelled', 'delayed', 'overdue', 'on_hold', 'postponed', name='project_status'), nullable=False)
        )

    # 3. Modify `task` table
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column(
            'status',
            existing_type=postgresql.ENUM('planning', 'in_progress', 'completed', name='task_status', create_type=False),
            type_=sa.Enum('pending', 'in_progress', 'completed', 'cancelled', name='task_status'),
            existing_nullable=True
        )


    # ### end Alembic commands ###


def downgrade():
    # 1. Revert `task` enum back to old definition
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column(
            'status',
            existing_type=sa.Enum('pending', 'in_progress', 'completed', 'cancelled', name='task_status'),
            type_=postgresql.ENUM('planning', 'in_progress', 'completed', name='task_status', create_type=False),
            existing_nullable=True
        )

    # 2. Drop added column from `project` table
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('status')

    # 3. Drop the ENUM types from PostgreSQL
    op.execute('DROP TYPE IF EXISTS project_status')
    op.execute('DROP TYPE IF EXISTS task_status')


    # ### end Alembic commands ###
