# users/interfaces/api/urls.py

from django.urls import path
from users.interfaces.api.views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
]
