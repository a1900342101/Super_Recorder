# coding:utf8

from django.conf.urls import url
from django.contrib import admin
from s_Recorder import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^video/$', views.video),
    url(r'^camera/$', views.camera),
    url(r'^no/$', views.not_found),
]
