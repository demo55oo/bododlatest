# Generated by Django 4.1.1 on 2022-09-27 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('NA', 'not_to_mention')], max_length=2, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default=None, max_length=1000, null=True, upload_to=user.models.upload_img_to)),
                ('address', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
