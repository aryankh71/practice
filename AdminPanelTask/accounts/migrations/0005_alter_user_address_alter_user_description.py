# Generated by Django 4.2.11 on 2024-07-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
