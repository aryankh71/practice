# Generated by Django 4.2.11 on 2024-03-15 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_available',
            field=models.BooleanField(null=True),
        ),
    ]
