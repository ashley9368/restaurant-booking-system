from django.urls import path
from django.contrib.auth.views import LogoutView # Import LogoutView
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page='homepage'), name="logout")
]