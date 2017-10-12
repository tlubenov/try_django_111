from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'restaurant',
        'name',
        'contents',
        'excludes',
        'public',
        'timestamp',
        'updated'
    )


admin.site.register(Item, ItemAdmin)

