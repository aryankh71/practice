from django.contrib import admin
from.models import *


@admin.register(Auth)
class AuthAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'signing_date', 'user_type', 'gender')
    list_filter = ('username', 'signing_date', 'user_type')
    search_fields = ('username', 'signing_date')
    # prepopulated_fields = {'user_type': ('username',)}
    # raw_id_fields = ('username') --> (admin.E003) The value of 'raw_id_fields[0]' must be a foreign key or a many-to-many field.
    # date_hierarch
    ordering = ('username', 'signing_date')


@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'family')


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('writer', 'timedate')


# admin.site.register(Auth, AuthAdmin)


# admin.site.register(Post)
# admin.site.register(Person)
