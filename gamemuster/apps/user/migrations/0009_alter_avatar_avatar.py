# Generated by Django 4.0.4 on 2022-05-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_customuser_email_alter_customuser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(default='users/default.png', upload_to='users'),
        ),
    ]