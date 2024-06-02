from django.contrib.auth.views import LogoutView
from django.urls import path

from bxauth import views

urlpatterns = [
    path("", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
