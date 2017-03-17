from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^chhreader/topic/(?P<topic_id>[0-9]+)', views.subtopic, name='subtopic'),
    url(r'^chhreader/topic', views.topic, name='topic'),
    url(r'^chhreader/item', views.item, name='item'),
    url(r'^chhreader/post', views.post, name='post'),
    url(r'^chhreader/updatas', views.updatas, name='updatas'),
    url(r'^chhreader/addcontent', views.updateContent, name='updateContent'),
    url(r'^chhreader/contentexist', views.contentExist, name='contentExist'),
    url(r'^chhreader/content', views.content, name='content'),
]
