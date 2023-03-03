from .views import HomeView, RegistrationFormView, logout_user, LoginUserView, UserProfileView, AllTaskView
from django.urls import path, include
 

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("registration/", RegistrationFormView.as_view(), name="registration"),
    path("logout/", logout_user, name="logout"),
    path("user_profile/", UserProfileView.as_view(), name="user_profile"),
    path("all_tasks/", AllTaskView.as_view(), name="all_tasks"),
]
