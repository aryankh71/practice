# Generated by Django 5.0.2 on 2024-03-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Image',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
