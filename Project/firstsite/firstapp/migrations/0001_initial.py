# Generated by Django 5.0.2 on 2024-03-10 07:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=70)),
                ('lname', models.CharField(max_length=70)),
                ('age', models.PositiveIntegerField(null=True)),
                ('captcha', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=10)),
                ('project', models.BooleanField(null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('text', models.TextField(null=True)),
                ('Image', models.ImageField(upload_to='uploads')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('writer', models.ForeignKey(default='some string', on_delete=django.db.models.deletion.CASCADE, to='firstapp.person')),
            ],
        ),
    ]