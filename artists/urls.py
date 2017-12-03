from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.artist_list, name="artist_list"),
    url(r'^(?P<id>\d+)/$', views.artist_detail, name="artist_detail"),
    url(r'^(?P<id>\d+)/edit/$', views.artist_edit, name="artist_edit"),
    url(r'^new/$', views.artist_new, name="artist_new"),
]
