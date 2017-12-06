

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artists/', include ("artists.urls", namespace="artists")),
    url(r'^', include('core.urls', namespace="core")),
    url(r'^songs/', include ("songs.urls", namespace="songs")),
    url(r'^albums/', include ("albums.urls", namespace="album")),
]
