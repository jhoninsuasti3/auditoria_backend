from rest_framework import serializers
from users.infrastructure.db.models import CustomUser, Firm


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True, min_length=8)
    role = serializers.ChoiceField(choices=CustomUser.Role.choices)
    firm_id = serializers.PrimaryKeyRelatedField(
        queryset=Firm.objects.all(),
        required=False,
        allow_null=True
    )

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value

    def validate_password(self, value):
        if "123" in value or len(value) < 8:
            raise serializers.ValidationError("La contraseña es demasiado débil.")
        return value

    def validate(self, attrs):
        role = attrs.get("role")
        firm = attrs.get("firm_id")

        # Reglas de negocio
        if role in ["firm_admin", "auditor", "auditor_lead"] and firm is None:
            raise serializers.ValidationError("Este tipo de usuario requiere una firma asignada.")

        if role == "system_admin" and firm is not None:
            raise serializers.ValidationError("Un administrador del sistema no debe tener firma.")

        return attrs
