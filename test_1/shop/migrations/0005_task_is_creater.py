# Generated by Django 4.1.7 on 2023-03-09 14:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0004_alter_task_time_close"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_creater",
            field=models.ManyToManyField(
                db_table="creaters",
                related_name="creaters",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]