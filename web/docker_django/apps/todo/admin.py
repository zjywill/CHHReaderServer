from django.contrib import admin
from .models import Item

class ItemData(admin.ModelAdmin):
    list_display = ('text', 'date_posted')
    ordering = ('date_posted',)

admin.site.register(Item,ItemData)