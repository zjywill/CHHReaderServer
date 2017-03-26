from django.db import models


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)  # option,
    order = models.IntegerField(default=1)
    source_link = models.CharField(max_length=255, blank=True, null=False, unique=True)
    is_valid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class ItemData(models.Model):
    topic = models.ForeignKey(Topic, related_name='topic_item')
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255, blank=True, null=False, unique=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    postdate = models.CharField(max_length=255, blank=True, null=True)
    is_valid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Content(models.Model):
    root_link = models.CharField(max_length=255, unique=True, null=False)
    content = models.TextField()

    def __unicode__(self):
        return self.root_link
