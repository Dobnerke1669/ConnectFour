# Generated by Django 4.1.5 on 2023-01-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0003_rename_current_player_connectfourgame_next_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectfourgame',
            name='grid',
        ),
        migrations.AddField(
            model_name='connectfourgame',
            name='board',
            field=models.CharField(default='                                          ', max_length=42),
        ),
    ]