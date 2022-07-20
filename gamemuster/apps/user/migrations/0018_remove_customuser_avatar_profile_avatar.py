# Generated by Django 4.0.5 on 2022-06-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_profile_remove_customuser_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='', upload_to='users'),
            preserve_default=False,
        ),
    ]