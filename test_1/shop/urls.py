from . import views
from django.urls import path, include
 

urlpatterns = [
    path("", views.HomeView.as_view(), name=""),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("registration/", views.RegistrationFormView.as_view(), name="registration"),
    path("logout/", views.logout_user, name="logout"),
    path("user_profile/", views.UserProfileView.as_view(), name="user_profile"),
    path("all_tasks/", views.AllTaskView.as_view(), name="all_tasks"),
    path("create_task/", views.create_task, name="create_task"),
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
    path("exit_task/<int:pk>/", views.exit_task, name="exit_task"),
    path("page_task/<int:pk>/", views.TaskView.as_view(), name="page_task"),
    path("join_a_task/<int:pk>/", views.join_a_task, name="join_a_task"),


]
