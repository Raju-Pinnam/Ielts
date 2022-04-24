from django.urls import path

from .views import UserCreationAPIView

app_name = "ielts_basics"

urlpatterns = [
    path("user_creation/", UserCreationAPIView.as_view(), name="user_creation"),
]

