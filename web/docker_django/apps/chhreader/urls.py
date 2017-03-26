from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chhreader/topics', views.topics, name='topics'),
    url(r'^chhreader/articles', views.articles, name='articles'),
    url(r'^chhreader/addcontent', views.updateContent, name='updateContent'),
    url(r'^chhreader/contentexist', views.contentExist, name='contentExist'),
    url(r'^chhreader/content', views.content, name='content'),
]
