# Generated by Django 4.1.5 on 2023-01-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0004_remove_connectfourgame_grid_connectfourgame_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectfourgame',
            name='board',
            field=models.TextField(default='                                          ', max_length=42),
        ),
    ]
