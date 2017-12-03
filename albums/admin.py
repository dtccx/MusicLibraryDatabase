from django.contrib import admin
from . models import Album

class AlbumAdmin (admin.ModelAdmin):
    list_display = ("artist_name", "album_name", "collection_or_greatest_hits", "studio_or_live", "year_released")
    search_fields = ('artist_name', 'album_name')

admin.site.register(Album, AlbumAdmin)
