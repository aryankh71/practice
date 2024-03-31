from django.contrib import admin

from order_food.models import Food

# admin.site.register(Food)
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','is_available' ,'description')
    list_filter = ('price',)
    search_fields = ('model',)
    # raw_id_fields = ('price',)
    # ordering = ('name','description',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('price')  # Sort queryset by price
        return queryset