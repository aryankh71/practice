from django.db import models
from django.utils import timezone


# how to create ImageField()
# field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)

class Person(models.Model):
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female')
    )
    # ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    publish = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    age = models.PositiveIntegerField(null=True)
    # country = CountryField()
    captcha = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='m')
    project = models.BooleanField(blank=False, null=True)
    Email = models.EmailField(null=True)
    text = models.TextField(null=True)
    Image = models.ImageField(upload_to='uploads', null=True)


# tartibe namayeshe postha bar asase publish ya tarikhe entesharesh bashe

    class Meta:
        ordering = ('-publish',)

    # def __str__(self):
    #     return self.name

class Users(models.Model):
    name = models.CharField(max_length=50)
    writer = models.ForeignKey(Person, on_delete=models.CASCADE, default='some string')


class User(models.Model):
    name = models.CharField(max_length=10)