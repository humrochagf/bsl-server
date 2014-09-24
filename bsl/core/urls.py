from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/token/(?P<url_token>\w+)$', views.token_authentication, name='auth_token'),
    url(r'^restricted/$', views.restricted_area, name='restricted'),
)
