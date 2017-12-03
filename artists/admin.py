from django.contrib import admin

from . models import Artist

class ArtistAdmin (admin.ModelAdmin):
    list_display = (
        "name",
        "get_song_names",
    )

admin.site.register(Artist, ArtistAdmin)

