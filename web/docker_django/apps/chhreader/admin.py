from django.contrib import admin
from .models import Topic, ItemData, Content


# website app
def item_data_name(obj):
    return ("%s ---[%s]" % (obj.name, obj.topic))


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'source_link', 'is_valid')
    ordering = ('id',)


class ItemDataAdmin(admin.ModelAdmin):
    list_display = ('id', item_data_name, 'link', 'image_url', 'topic', 'postdate', 'is_valid')
    list_filter = ('topic',)
    ordering = ('postdate',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(ItemData, ItemDataAdmin)
admin.site.register(Content)
