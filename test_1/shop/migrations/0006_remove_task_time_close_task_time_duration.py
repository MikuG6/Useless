# Generated by Django 4.1.7 on 2023-03-09 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_task_is_creater"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="time_close",
        ),
        migrations.AddField(
            model_name="task",
            name="time_duration",
            field=models.DurationField(default=datetime.timedelta(days=2)),
        ),
    ]
