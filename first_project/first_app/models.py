from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=70, null='', verbose_name="نام")
    family = models.CharField(max_length=70, null='', verbose_name="نام خانوادگی")
    age = models.IntegerField(verbose_name="سن")
    country = models.CharField(max_length=50, verbose_name="کشور")


class Auth(models.Model):
    GENDER_CHOICES = (
        ("male", "آقا"),
        ("female", "خانم"),
    )
    # TYPE_CHOICES = (
    #     ("R", "Regular"),
    #     ("P", "Premium"),
    # )
    username = models.CharField(max_length=10, verbose_name="نام کاربری")
    email = models.EmailField(verbose_name="ایمیل")
    signing_date = models.DateTimeField(verbose_name="تاریخ")
    user_type = models.CharField(max_length=1, verbose_name="نوع کاربری")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="آقا", verbose_name="جنسیت")

    class Meta:
        ordering = ('signing_date',)

    def __str__(self):
        return self.username

    # def change_user_type(self):
    #     if self.user_type == 'R':
    #         self.user_type = 'P'
    #     else:
    #         self.user_type = 'R'
    #     self.save()
    #
    # def change_username(self, name):
    #     self.username = name
    #     self.save()


# one-to-many or many-to-one
class Post(models.Model):
    content = models.TextField(verbose_name="محتوا")
    writer = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name="نویسنده")
    timedate = models.DateTimeField(verbose_name="تاریخ")

    def __str__(self):
        return self.content

# many-to-many
# class Post(models.Model):
#     content = models.TextField()
#     writers = models.ManyToManyField(User)
