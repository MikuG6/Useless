from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_close = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    owner = models.ManyToManyField(User, db_table="owner", 
                                        related_name="owners"
                                    )

    def __str__(self):
        return self.title