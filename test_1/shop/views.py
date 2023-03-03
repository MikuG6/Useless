from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login


class HomeView(ListView):
    model = Task
    template_name = "shop/ToDoHome.html"

class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = ""


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    success_url = "/home"

    template_name = "registration/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('/login')


class UserProfileView(ListView):
    model = Task
    template_name = "user_profile.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_tasks"] = Task.objects.all()
        # context["owner"] = Task.owner.user_id()

        return context