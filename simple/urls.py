# example/simple/urls.py

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name = 'search'),
    # url(r'^showchart/$', views.show_chart, name = 'chart')
]