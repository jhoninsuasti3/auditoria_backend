from django.contrib import admin
from .models import CustomUser, Firm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ("email", "full_name", "role", "firm", "is_active")
    search_fields = ("email", "full_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Info", {"fields": ("full_name", "role", "firm")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "role", "firm", "password1", "password2"),
        }),
    )


admin.site.register(Firm)
