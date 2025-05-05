"""Create phone number for users column

Revision ID: 6ed4c4722e30
Revises: 
Create Date: 2025-05-02 23:27:00.936395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ed4c4722e30'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


"""Upgrade schema."""
def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(10), nullable=True))
"""
- Thêm một cột mới vào cơ sở dữ liệu của bạn.
- Tên bảng: 'users' - Cột mới sẽ được thêm vào bảng có tên "users".

- Định nghĩa cột mới:

    + Tên cột: 'phone_number' - Cột mới có tên là "phone_number"
    + Kiểu dữ liệu: sa.String(10) - Cột này có kiểu dữ liệu String (văn bản), giới hạn độ dài 10
    + Thuộc tính: nullable=True - Cột này được phép chứa giá trị NULL
"""


"""Downgrade schema."""
def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    
