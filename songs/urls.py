from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.song_list, name="song_list"),
    url(r'^(?P<id>\d+)/$', views.song_detail, name="song_detail"),
    url(r'^(?P<id>\d+)/edit/$', views.song_edit, name="song_edit"),
    url(r'^new/$', views.song_new, name="song_new"),
]

