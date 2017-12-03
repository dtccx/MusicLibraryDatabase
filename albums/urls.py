from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
    url(r'^album_edit$', views.album_edit, name='album_edit'),
    url(r'^album/(?P<pk>\d+)/$', views.album_details, name="album_details"),
]
