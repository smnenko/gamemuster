# Generated by Django 4.0.5 on 2022-06-21 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_remove_customuser_avatar_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(default='', upload_to='users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]