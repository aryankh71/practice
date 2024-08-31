from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser
# from django_comments_xtd.models import XtdComment
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     country = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=50, blank=True, null=True)

# the difference between nationality and country:
# nationality: the brand belong to which country'
# country: the model of this brand assembeled in which country

class Brand(models.Model):
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')

    # created = models.DateTimeField(null=True, default=timezone.now())

    def __str__(self):
        return self.name


# class Design(models.Model):
#     color = models.CharField(max_length=16, verbose_name='رنگ بندی', default='Black')
#
#     def __str__(self):
#         return self.color


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='نام برند')
    model = models.CharField(max_length=32, default='9T Pro', unique=True, verbose_name='نام مدل')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت محصول')
    # color = models.ForeignKey(Design, on_delete=models.CASCADE, verbose_name='رنگ بندی')
    color = models.CharField(max_length=16, verbose_name='رنگ بندی', default='Black')
    display_size = models.CharField(max_length=50, verbose_name='ابعاد صفحه نمایش')
    is_available = models.BooleanField(default=True, verbose_name='محصول فعال')
    country = models.CharField(max_length=90, null=True, verbose_name='کشور')
    photo = models.FileField(upload_to="", verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    # verbose_name_plural = "لیست کالای مربوطه"
    camera = models.CharField(max_length=50, null=True, verbose_name='دوربین')
    memory = models.CharField(max_length=20, null=True, verbose_name='حافطه داخلی')
    card = models.BooleanField(null=True, verbose_name='کارت حافظه')
    Dimensions = models.CharField(max_length=35, null=True, verbose_name='ابعاد')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='وزن')
    have_warranty = models.BooleanField(null=True, verbose_name='دارای گارانتی')
    warranty = models.CharField(max_length=50, default='')
    register = models.BooleanField(null=True, verbose_name='رجیستر شده')
    description = models.TextField(max_length=10000)
    stock = models.PositiveIntegerField(default=1, verbose_name='تعداد موجودی')

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)


class Processor(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='نام تراشه')
    brand = models.CharField(max_length=100, null=True, verbose_name='برند تراشه')


class Comment(models.Model):
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name='متن:')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    @property
    def name(self):
        return self.user.username  # یا self.user.get_full_name() اگر نام کامل کاربر را می‌خواهید

    @property
    def email(self):
        return self.user.email




# class ExtendedComment(XtdComment):
#     commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_by')
#     content_types = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=False, default=None)
#     objects_pk = models.TextField(default='write here...')  # شناسه شیء مربوطه در جدول محتوا
#     extended_comment_field = GenericForeignKey('content_types', 'objects_pk')
#     # اطلاعات نظر
#     comment_text = models.TextField(verbose_name='متن نظر', default='type here...')
#     submit_dates = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
#     is_publiced = models.BooleanField(default=True, verbose_name='عمومی بودن')
#     is_removed_by = models.BooleanField(default=False, verbose_name='حذف شده')
#
#     def __str__(self):
#         return f'{self.commented_by} - {self.comment_text}'

# class ExtendedComment(XtdComment):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


# users comments: explain about product
class Review(models.Model):
    pass


#
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', verbose_name='کاربر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.cartitem_set.all())
        return total

    def __str__(self):
        return f"{self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitem_set', verbose_name='سبد خرید', default=None)
    product = models.ForeignKey('Mobile', on_delete=models.CASCADE, verbose_name='محصول', default=None)
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.model} - {self.quantity} عدد"

    # @property
    # def total_price(self):
    #     return self.product.price * self.quantity


