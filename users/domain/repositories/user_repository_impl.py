from users.domain.repositories.user_repository import AbstractUserRepository
from users.domain.entities.user import User as UserEntity
from users.infrastructure.db.models import CustomUser


class DjangoUserRepository(AbstractUserRepository):
    def get_by_email(self, email: str) -> UserEntity | None:
        try:
            instance = CustomUser.objects.get(email=email)
            return self._to_entity(instance)
        except CustomUser.DoesNotExist:
            return None

    def save(self, user: UserEntity, password: str = None) -> UserEntity:
        instance = CustomUser(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            role=user.role,
            firm_id=user.firm_id,
            is_active=user.is_active,
            is_staff=user.is_staff,
            is_superuser=user.is_superuser,
        )
        if password:
            instance.set_password(password)
        instance.save()
        return self._to_entity(instance)

    def _to_entity(self, instance: CustomUser) -> UserEntity:
        return UserEntity(
            id=instance.id,
            email=instance.email,
            full_name=instance.full_name,
            role=instance.role,
            firm_id=instance.firm.id if instance.firm else None,
            is_active=instance.is_active,
            is_superuser=instance.is_superuser,
            is_staff=instance.is_staff,
            date_joined=instance.date_joined,
        )
