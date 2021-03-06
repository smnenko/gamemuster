# Generated by Django 3.1.7 on 2021-06-23 12:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


def default_avatar(apps, schema_editor):
    Avatar = apps.get_model('user', 'Avatar')
    Avatar().save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.IntegerField(default='1', primary_key=True, serialize=False, unique=True)),
                ('avatar', models.ImageField(default='users/default.jpg', upload_to='users')),
                ('date_uploaded', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RunPython(default_avatar),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.avatar'),
        ),
    ]
