from .views import HomeView, RegistrationFormView, logout_user, LoginUserView
from django.urls import path, include
 

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("registration/", RegistrationFormView.as_view(), name="registration"),
    path("logout/", logout_user, name="logout")
]
