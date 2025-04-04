# users/application/use_cases/register_user.py

from users.domain.entities.user import User
from users.domain.repositories.user_repository import AbstractUserRepository


class RegisterUserUseCase:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    def execute(self, data: dict) -> User:
        user = User(
            id=None,
            email=data["email"],
            full_name=data["full_name"],
            role=data["role"],
            firm_id=data.get("firm_id"),
        )
        return self.user_repo.save(user, password=data["password"])
