# Generated by Django 4.2.11 on 2024-07-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilestore', '0004_remove_comment_email_remove_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='پیام خود را بنویسید:'),
        ),
    ]