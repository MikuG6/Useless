from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_duration = models.DurationField(default=timedelta(days=2))
    is_done = models.BooleanField(default=False)
    owner = models.ManyToManyField(
        User, 
        db_table="owner", 
        related_name="owners",
    )
    is_creater = models.ManyToManyField(
        User, 
        db_table="creaters", 
        related_name="creaters",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})