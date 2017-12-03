from django.contrib import admin

from . models import Song



class SongAdmin (admin.ModelAdmin):
    search_fields = [
        "name", 
        "track_number",  
    ]

    list_display = [
        "get_artist_names",
        "name", 
        "length",
        "track_number",
    ]


admin.site.register(Song, SongAdmin)

