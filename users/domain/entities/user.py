# users/domain/entities/user.py

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: Optional[int]
    email: str
    full_name: str
    role: str
    firm_id: Optional[int]
    is_active: bool = True
    is_superuser: bool = False
    is_staff: bool = False
    date_joined: Optional[datetime] = None
