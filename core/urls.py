from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user_list/$', views.user_list, name="user_list"),
    url(r'^(?P<id>\d+)user_detail/$', views.user_detail, name="user_detail"),
    url(r'^(?P<id>\d+)user_follow/$', views.user_follow, name="user_follow"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^set_password/$', views.set_password, name="set_password"),
    url(r'^user_like/(?P<id>\d+)/$', views.like_artist, name="like_artist"),
]