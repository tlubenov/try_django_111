from django.contrib import admin

from .models import RestaurantLocation

class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'category',
        'timestamp',
        'updated'
    )


admin.site.register(RestaurantLocation, RestaurantAdmin)