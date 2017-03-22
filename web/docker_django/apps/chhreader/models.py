from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)  #option,
    order = models.IntegerField(default = 1)
    is_valid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    topic = models.ForeignKey(Topic, related_name='topic_item')
    name = models.CharField(max_length=64)  #option,
    sourcelink = models.CharField(max_length = 255, blank=True, null=False, unique=True)
    source_update_at = models.DateTimeField(auto_now_add = True)
    order = models.IntegerField(default = 1)
    is_valid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class ItemData(models.Model):
    item = models.ForeignKey(Item, related_name='item_data')
   
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255, blank=True, null=False, unique=True)
    imageurl = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    postdate = models.CharField(max_length=255, blank=True, null=True)
    
    is_valid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Content(models.Model):
    rootlink = models.CharField(max_length=255, unique=True, null=False)
    content = models.TextField()

    def __unicode__(self):
        return self.rootlink
