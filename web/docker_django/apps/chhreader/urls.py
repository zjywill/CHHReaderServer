from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chhreader/topics', views.topics, name='topics'),
    url(r'^chhreader/articles', views.articles, name='articles'),
    url(r'^chhreader/content/(\d+)', views.viewContent, name='viewContent'),
    url(r'^chhreader/content', views.content, name='content'),
]
