# Generated by Django 4.0.4 on 2022-04-27 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_rename_logo_game_cover_alter_game_date_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.rating'),
        ),
    ]
