# Generated by Django 4.2.11 on 2024-03-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='is_available',
            field=models.BooleanField(null=True),
        ),
    ]
