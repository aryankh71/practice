from django.contrib import admin
from .models import Book, Author, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name','write_date', 'is_alive']

    # def full_name(self, obj):
    #     return str(obj)
    # full_name.admin_order_field = 'first_name'
    # full_name.short_description = 'Full Name'
# admin.site.register(Author)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'categories', 'published', 'price']
    search_fields = ['name', 'author__first_name', 'author__last_name']
# admin.site.register(Book)

admin.site.register(Category)

