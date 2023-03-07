from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods


class HomeView(ListView):
    model = Task
    template_name = "shop/ToDoHome.html"
    extra_context = {"title":"Главная страница"}


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    extra_context = {"title":"Авторизация"}


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    extra_context = {"title":"Регистрация"}

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
    template_name = "shop/user_profile.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users_tasks"] = Task.objects.filter(owner__id=self.request.user.id)
        context["title"] = "Профиль"

        return context



class AllTaskView(ListView):
    model = Task
    template_name = "shop/all_tasks.html"
    context_object_name = "all_tasks"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_tasks"] = Task.objects.all()
        context["users_tasks"] = Task.objects.filter(owner__id=self.request.user.id)
        context["title"] = "Все задачи"

        return context


@require_http_methods(['POST'])
def create_task(request):
    title = request.POST['title']
    description = request.POST['description']
    owner2 = request.user.id
    task = Task(title = title, description = description)
    task.save()
    task.owner.add(owner2)
    return redirect('user_profile')


def delete_task(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('user_profile')

def exit_task(request, pk):
    task = Task.objects.get(id = pk)
    task.owner.remove(request.user)
    return redirect('user_profile')


class TaskView(ListView):
    model = Task
    template_name = "shop/task_page.html"
    context_object_name = "one_task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.get(id = pk)
        context["users_tasks"] = Task.objects.filter(owner__id=self.request.user.id)

        return context