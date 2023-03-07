from .models import Task

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["title_tasks"] = Task.objects.all()
        context["users_tasks"] = Task.objects.filter(owner__id=self.request.user.id)

        return context