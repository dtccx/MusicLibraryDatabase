from django.contrib import admin
from . models import Playlist



class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("playlist_name", "year_released", "get_song", "creator")
    search_fields = ('playlist_name',)

admin.site.register(Playlist, PlaylistAdmin)
