from django.conf.urls import patterns, url

from bsl.core import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^token/(?P<url_token>\w+)$', views.token_authentication, name='token_authentication'),
)
