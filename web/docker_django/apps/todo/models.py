from django.db import models


class Item(models.Model):
    text = models.TextField(blank=False, null=False)
    date_posted = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.text