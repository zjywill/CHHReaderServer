from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^stream/play', views.streamPlayList, name='streamPlayList'),
    url(r'^stream/push', views.streamPushList, name='streamPushList'),
    url(r'^stream/status', views.streamStatus, name='streamStatus'),
]
