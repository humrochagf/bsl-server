from django.conf.urls import patterns, include, url

from bsl.core import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
