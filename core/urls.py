from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^accounts/signup/$', views.signup, name="signup"),
    url(r'^accounts/login/$', views.login, name="login"),
    url(r'^accounts/logout/$', views.logout, name="logout"),
    url(r'^accounts/set_password/$', views.set_password, name="set_password"),
    url(r'^accounts/edit/$', views.user_edit, name="user_edit"),
    url(r'^user_list/$', views.user_list, name="user_list"),
    url(r'^(?P<id>\d+)/user_detail/$', views.user_detail, name="user_detail"),
    url(r'^(?P<id>\d+)/user_follow/$', views.user_follow, name="user_follow"),
    url(r'^user_like/$', views.like_artist, name="like_artist"),
    url(r'^like_list/$', views.like_list, name="like_list"),
    url(r'^follow_user/$', views.follow_user, name="follow_user"),
]