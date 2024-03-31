from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField(max_length=50, null=True)

    def __str__(self):
        return self.name
