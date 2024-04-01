from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser
#
#
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     country = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=50, blank=True, null=True)


class Brand(models.Model):
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)
    # publish = models.DateTimeField(null=True, default=timezone.now())
    # created = models.DateTimeField(null=True, default=timezone.now())

    def __str__(self):
        return self.name


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=32, default='9T Pro', unique=True)
    price = models.PositiveIntegerField(default=2097152)
    color = models.CharField(max_length=16, default='Black')
    display_size = models.SmallIntegerField(default=4)
    is_available = models.BooleanField(default=True)
    country = models.CharField(max_length=90, null=True)
    photos = models.ImageField(null=True)

    def __str__(self):
        return '{} {}'.format(self.brand.name, self.model)
