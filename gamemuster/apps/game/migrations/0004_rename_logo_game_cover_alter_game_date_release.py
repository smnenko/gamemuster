# Generated by Django 4.0.4 on 2022-04-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_remove_game_screenshots_screenshot_game_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='logo',
            new_name='cover',
        ),
        migrations.AlterField(
            model_name='game',
            name='date_release',
            field=models.DateField(null=True),
        ),
    ]
