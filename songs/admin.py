from django.contrib import admin

from . models import Song



class SongAdmin (admin.ModelAdmin):
    search_fields = [
        "name",
    ]

    list_display = [
        "get_artist_names",
        "name", 
        "length",
    ]


admin.site.register(Song, SongAdmin)

