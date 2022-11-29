# Generated by Django 4.1.1 on 2022-10-01 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='grade',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='value',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default=None, max_length=1000, null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='LevelManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levels', models.IntegerField(default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_level', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]