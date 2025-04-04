# users/domain/repositories/user_repository.py

from abc import ABC, abstractmethod
from typing import Optional
from users.domain.entities.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        ...

    @abstractmethod
    def save(self, user: User, password: Optional[str] = None) -> User:
        ...
