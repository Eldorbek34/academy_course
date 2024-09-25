from apps.users.api_endpoints.loginRequest import LoginRequestAPIView
from django.urls import path
urlpatterns = [
    path("login-request/", LoginRequestAPIView.as_view())
]