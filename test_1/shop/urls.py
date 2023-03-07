from .views import HomeView, RegistrationFormView, logout_user, LoginUserView, UserProfileView, AllTaskView, create_task, delete_task, TaskView, exit_task
from django.urls import path, include
 

urlpatterns = [
    path("", HomeView.as_view(), name=""),
    path("login/", LoginUserView.as_view(), name="login"),
    path("registration/", RegistrationFormView.as_view(), name="registration"),
    path("logout/", logout_user, name="logout"),
    path("user_profile/", UserProfileView.as_view(), name="user_profile"),
    path("all_tasks/", AllTaskView.as_view(), name="all_tasks"),
    path("create_task/", create_task, name="create_task"),
    path("delete_task/<int:pk>/", delete_task, name="delete_task"),
    path("exit_task/<int:pk>/", exit_task, name="exit_task"),
    path("page_task/<int:pk>/", TaskView.as_view(), name="page_task"),
]
