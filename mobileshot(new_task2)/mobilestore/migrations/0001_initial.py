# Generated by Django 4.2.11 on 2024-07-20 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('nationality', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام تراشه')),
                ('brand', models.CharField(max_length=100, null=True, verbose_name='برند تراشه')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='9T Pro', max_length=32, unique=True, verbose_name='نام مدل')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='قیمت محصول')),
                ('color', models.CharField(default='Black', max_length=16, verbose_name='رنگ بندی')),
                ('display_size', models.CharField(max_length=50, verbose_name='ابعاد صفحه نمایش')),
                ('is_available', models.BooleanField(default=True, verbose_name='محصول فعال')),
                ('country', models.CharField(max_length=90, null=True, verbose_name='کشور')),
                ('photo', models.FileField(upload_to='', verbose_name='تصویر')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('camera', models.CharField(max_length=50, null=True, verbose_name='دوربین')),
                ('memory', models.CharField(max_length=20, null=True, verbose_name='حافطه داخلی')),
                ('card', models.BooleanField(null=True, verbose_name='کارت حافظه')),
                ('Dimensions', models.CharField(max_length=35, null=True, verbose_name='ابعاد')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='وزن')),
                ('have_warranty', models.BooleanField(null=True, verbose_name='دارای گارانتی')),
                ('warranty', models.CharField(default='', max_length=50)),
                ('register', models.BooleanField(null=True, verbose_name='رجیستر شده')),
                ('description', models.TextField(max_length=10000)),
                ('stock', models.PositiveIntegerField(default=1, verbose_name='تعداد موجودی')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mobilestore.brand', verbose_name='نام برند')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='متن:')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mobilestore.mobile')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='تعداد')),
                ('cart', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cartitem_set', to='mobilestore.cart', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mobilestore.mobile', verbose_name='محصول')),
            ],
        ),
    ]
