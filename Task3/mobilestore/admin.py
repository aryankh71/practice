from django.contrib import admin
from .models import Brand, Mobile
# Register your models here.


admin.site.register(Brand)


# admin.site.register(Mobile)
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price','display_size' )
