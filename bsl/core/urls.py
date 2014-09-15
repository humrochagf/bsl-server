from django.conf.urls import patterns, include, url

from bsl.core import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),

    url(r'^barcode_login$', views.barcode_login, name='barcode_login'),

    url(r'^restricted_area$', views.restricted_area, name='restricted_area'),

    url(r'^barcode_loggoff$', views.barcode_loggoff, name='barcode_loggoff'),

    url(r'^mobile_simulation$', views.mobile_simulation, name='mobile_simulation'),
)
