from django.urls import path
from .views import LogoutView, HomeView

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", HomeView.as_view()),
    ]
