from django.contrib import admin
from .models import Topic, Item, ItemData, Content

#item
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'sourcelink', 'topic')
    list_display_links = ('name', )
    list_filter = ('topic',)
    ordering = ('topic',)

#website app
def itemdata_name(obj):
    return ("%s ---[%s]" % (obj.name, obj.item))
    
class ItemDataAdmin(admin.ModelAdmin):
    list_display = (itemdata_name, 'link', 'imageurl' ,'item','postdate')
    list_filter = ('item',)
    ordering = ('item',)

class ItemTopic(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


admin.site.register(Topic, ItemTopic)
admin.site.register(Content)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemData, ItemDataAdmin)