# Generated by Django 4.1.5 on 2023-01-05 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0010_connectfourgame_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectfourgame',
            name='board',
        ),
    ]