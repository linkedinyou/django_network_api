from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<router_name>[a-z0-9]+\.[a-z0-9]+)/$', views.router, name='router'),
]
