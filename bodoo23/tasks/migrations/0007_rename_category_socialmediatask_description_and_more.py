# Generated by Django 4.1.1 on 2022-11-14 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_task_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmediatask',
            old_name='category',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='surveytask',
            old_name='category',
            new_name='description',
        ),
    ]
