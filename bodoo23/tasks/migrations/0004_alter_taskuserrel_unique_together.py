# Generated by Django 3.2.15 on 2022-09-26 06:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_socialmediatask'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='taskuserrel',
            unique_together={('user', 'task')},
        ),
    ]
