# users/interfaces/api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.infrastructure.serializers.user_serializer import UserRegisterSerializer
from users.infrastructure.db.repositories.user_repository_impl import DjangoUserRepository
from users.application.use_cases.register_user import RegisterUserUseCase


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.validated_data
        user_repo = DjangoUserRepository()
        use_case = RegisterUserUseCase(user_repo)

        created_user = use_case.execute(user_data)
        return Response({
            "id": created_user.id,
            "email": created_user.email,
            "full_name": created_user.full_name,
            "role": created_user.role,
            "firm_id": created_user.firm_id,
        }, status=status.HTTP_201_CREATED)
