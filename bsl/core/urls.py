from django.conf.urls import patterns, url

from bsl.core import views

urlpatterns = patterns('',
    url(r'^$', views.login_page, name='login'),
    url(r'^(?P<url_token>\w+)$', views.login_page, name='login'),
)
