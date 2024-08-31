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


admin.site.register(Processor)


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('model','brand','color','price' ,'is_available','stock','publish')
    # list_display_links = ('model', 'brand')
    list_editable = ['is_available']
    list_filter = ('price','brand')
    verbose_name_plural = "Custom Model Name"
    search_fields = ('model','brand__name','price')
    # preserve_filters =
    # raw_id_fields = ['model',]
    ordering = ('brand', 'model')
    sortable_by = ('price', 'is_available')
    fieldsets = (
        ('مشخصات کالا', {'fields': ('brand', 'model', 'color','photo','country','have_warranty', 'stock')}),
        ('مشخصات فنی', {'fields': ('display_size' ,'weight','Dimensions','camera', 'memory', 'card', 'warranty')}),
        ('موجودی', {'fields': ('price','is_available',)}),
        ('متن خود را بنویسید', {'fields': ('description',)}),
        ('زمان انتشار', {'fields': ('publish',)}),
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality']
    list_display_links = ['name',]
    search_fields = ('name', 'nationality')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','mobile','body' ,'created', 'active']
    list_editable = ['active']
    # def user_email(self, obj):
    #     return obj.user_email
    #
    # user_email.admin_order_field = 'user__email'  # برای مرتب‌سازی بر اساس فیلد کاربر
    # user_email.short_description = 'User Email'


# admin.site.register(Comment)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at','updated_at',]
# admin.site.register(Cart)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity']
# admin.site.register(CartItem)


# admin.site.register(Design)