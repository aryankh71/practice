from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=80, verbose_name='نام خانوادگی')
    write_date = models.DateField(null=True,verbose_name='تاریخ تولد')
    description = models.TextField(blank=True, verbose_name='مختصری از نویسنده')
    is_alive = models.BooleanField(null=True, verbose_name='در قید حیات')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام دسته')

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام کتاب')
    author = models.ForeignKey(Author, models.CASCADE, verbose_name='نویسنده')
    published = models.DateField(verbose_name='تاریخ انتشار', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت کتاب', null=True)
    description = models.TextField(blank=True, verbose_name='مختصری از کتاب')
    categories = models.ForeignKey(Category, models.CASCADE, verbose_name='دسته بندی' , null=True)

    def __str__(self):
        return f"{self.name}"