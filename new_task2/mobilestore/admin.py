from django.contrib import admin
from .models import *
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
# from .models import CustomUser

#
# @admin.register(CustomUser)
# class UserAdmin(DefaultUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {
#             'fields': (
#                 'first_name',
#                 'last_name',
#                 'email',
#                 'phone_number',
#                 'country'
#             )
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active',
#                 'is_staff',
#                 'is_superuser',
#                 'groups',
#                 'user_permissions'
#             ),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#
#     list_display = (
#         'username',
#         'email',
#         'first_name',
#         'last_name',
#         'phone_number',
#         'is_staff',
#     )
#
#     search_fields = (
#         'username',
#         'first_name',
#         'last_name',
#         'phone_number',
#         'email',
#     )

# admin.site.register(Mobile)
# admin.site.register(Brand)


# class BookAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('General Info', {
#             'fields': ('title', 'publish_date')
#         }),
#         ('Details', {
#             'classes': ('collapse',),
#             'fields': ('pages_count', 'author', 'price')
#         }),
#     )


class ProductInline(admin.StackedInline):
    model = Mobile
    extra = 0


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'is_available', 'price')
    list_display_links = ('model', 'brand')
    list_filter = ('is_available', 'country')
    search_fields = ('model', 'price')
    # preserve_filters =
    # raw_id_fields = ['model',]
    ordering = ('brand', 'model')
    sortable_by = ('price')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality']
    list_display_links = ['name']
    inlines = [ProductInline]
