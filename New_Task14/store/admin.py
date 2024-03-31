from django.contrib import admin

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_active']
    # list_display_links = ['id', 'name']
    fieldsets = [
        ('identification',{
            'fields': ('name', 'price', 'is_active')
        }),
        ('details', {'classes': ('collapse',),'fields': ('category', 'company')
        })
    ]
    list_editable = ['is_active']
    actions = ['make_inactive']

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    # make_inactive.short_description = "Make selected products inactive"
# admin.site.register(Product, ProductAdmin)
# class ProductAdmin(admin.ModelAdmin):
#     # Define fieldsets for the admin detail page
#     fieldsets = [
#         # Identification section
#         ('Identification', {
#             'fields': ('name', 'price', 'is_active'),
#         }),
#         # Details section (with collapsible ability)
#         ('Details', {
#             'classes': ('collapse',),  # Add 'collapse' class for collapsible section
#             'fields': ('category', 'company'),
#         }),
#     ]
#     # Optionally, you can define list_display, search_fields, etc. for the admin list page
#
# # Register the Product model with the ProductAdmin
# admin.site.register(Product, ProductAdmin)

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Address)