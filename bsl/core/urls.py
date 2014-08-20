from django.conf.urls import patterns, include, url

from bsl.core import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),

    url(r'^(?P<token>[0-9a-fA-F]{40})$',
        views.barcode_login,
        name='barcode_login'),
)
