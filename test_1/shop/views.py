from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
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
    template_name = "registration/registration.html"
    extra_context = {"title":"Регистрация"}

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
        context["users_tasks"] = self.queryset
        context["title"] = "Профиль: {}".format(self.request.user)

        return context

    def get_queryset(self):
        self.queryset = Task.objects.filter(owner__id=self.request.user.id)
        return self.queryset


class AllTaskView(ListView):
    model = Task
    template_name = "shop/all_tasks.html"
    context_object_name = "all_tasks"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_tasks"] = Task.objects.all()
        context["users_tasks"] = Task.objects.filter(
            owner__id=self.request.user.id
        )
        context["title"] = "Все задачи"

        return context


@require_http_methods(['POST'])
def create_task(request):
    title = request.POST['title']
    description = request.POST['description']
    task = Task(title = title, description = description)
    task.save()
    task.owner.add(request.user.id)
    task.is_creater.add(request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_task(request, pk):
    if (task := Task.objects.get(id = pk)) in Task.objects.filter(
        is_creater__id=request.user.id
    ):
        task.delete()
        return redirect("all_tasks")
    else:
        return HttpResponse("Вы не являетесь создателем задачи")


def exit_task(request, pk):
    task = Task.objects.get(id = pk)
    task.owner.remove(request.user)
    return redirect("all_tasks")


def join_a_task(request, pk):
    task = Task.objects.get(id = pk)
    task.owner.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class TaskView(DetailView):
    model = Task
    template_name = "shop/task_page.html"
    context_object_name = "one_task"
