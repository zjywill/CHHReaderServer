from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chhreader/topic', views.topic, name='topic'),
    url(r'^chhreader/post', views.post, name='post'),
    url(r'^chhreader/updatas', views.updatas, name='updatas'),
    url(r'^chhreader/addcontent', views.updateContent, name='updateContent'),
    url(r'^chhreader/contentexist', views.contentExist, name='contentExist'),
    url(r'^chhreader/content', views.content, name='content'),
]
