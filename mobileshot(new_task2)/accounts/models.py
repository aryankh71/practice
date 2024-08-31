from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User


# class Users(AbstractUser):
#     GENDER_CHOICES=(
#         ('M', 'Male'),
#         ('F', 'Female')
#     )
#     first_name = models.CharField(max_length=100, null=True, verbose_name='نام')
#     last_name = models.CharField(max_length=150, null=True, verbose_name='نام خانوادگی')
#     email = models.EmailField(null=True, verbose_name='ایمیل')
#     phone = models.CharField(max_length=15, verbose_name='شماره تماس')
#     is_staff = models.BooleanField(null=True, blank=True, verbose_name='عضویت')
#     is_superuser = models.BooleanField(null=True, blank=True, verbose_name='کاربر کلیدی')
#     is_active = models.BooleanField(null=True, blank=True, verbose_name='فعال')
#     description = models.CharField(max_length=250, verbose_name='توضیحات')
#     date_joined = models.DateTimeField(null=True, verbose_name='تاریخ عضویت', auto_now_add=True)
#     last_login = models.DateTimeField(null=True, verbose_name='تاریخ آخرین بازدید')
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
#     username = models.CharField(max_length=20, null=True, verbose_name='نام کاربری')
#     pasword = models.CharField(max_length=20, null=True)

    #
    # def user_name(self):
    #     letter = []
    #     for let in self.username:
    #         letter.append(let)
    #     if letter[0].isupper() == True:
    #         word = ''.join(letter)
    #         return (f'your name {word} is currect')
    #     else:
    #         return "please check your username \n do not use this symbols: ! @ # $ % ^ & * on ur"
