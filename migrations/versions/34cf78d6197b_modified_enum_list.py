"""modified enum list

Revision ID: 34cf78d6197b
Revises: 3315122c9444
Create Date: 2025-05-22 10:27:30.385592
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '34cf78d6197b'
down_revision = '3315122c9444'
branch_labels = None
depends_on = None


def upgrade():
    # Define ENUM types
    project_status_enum = postgresql.ENUM(
        'planning', 'in_progress', 'completed', 'cancelled', 'delayed', 'overdue', 'on_hold', 'postponed',
        name='project_status'
    )
    task_status_enum = postgresql.ENUM(
        'pending', 'in_progress', 'completed', 'cancelled',
        name='task_status'
    )

    # Create ENUM types in DB
    project_status_enum.create(op.get_bind(), checkfirst=True)
    task_status_enum.create(op.get_bind(), checkfirst=True)

    # Add 'status' column to 'project' using new enum
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', project_status_enum, nullable=False))

    # Alter 'status' column in 'task' to use new enum with cast
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column(
            'status',
            existing_type=postgresql.ENUM('planning', 'in_progress', 'completed', name='task_status', create_type=False),
            type_=task_status_enum,
            existing_nullable=True,
            postgresql_using="status::text::task_status"
        )


def downgrade():
    # Define the same ENUM types for reversal
    task_status_enum = postgresql.ENUM(
        'pending', 'in_progress', 'completed', 'cancelled',
        name='task_status'
    )
    project_status_enum = postgresql.ENUM(
        'planning', 'in_progress', 'completed', 'cancelled', 'delayed', 'overdue', 'on_hold', 'postponed',
        name='project_status'
    )

    # Revert task.status to previous enum using cast
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column(
            'status',
            existing_type=task_status_enum,
            type_=postgresql.ENUM('planning', 'in_progress', 'completed', name='task_status', create_type=False),
            existing_nullable=True,
            postgresql_using="status::text::task_status"
        )

    # Drop 'status' column from 'project'
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('status')

    # Drop ENUM types
    task_status_enum.drop(op.get_bind(), checkfirst=True)
    project_status_enum.drop(op.get_bind(), checkfirst=True)
