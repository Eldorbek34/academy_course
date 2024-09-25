from django.urls import path, include

from apps.users import urls as user_urls
urlpatterns = [
    path("users/", include("apps.users.urls")),
]