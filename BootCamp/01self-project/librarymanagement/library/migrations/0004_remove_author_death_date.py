# Generated by Django 4.2.11 on 2024-08-27 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_author_death_date_author_is_alive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='death_date',
        ),
    ]