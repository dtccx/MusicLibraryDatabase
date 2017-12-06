from django.contrib import admin
from . models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ("album_name", "year_released")
    search_fields = ('album_name',)

admin.site.register(Album, AlbumAdmin)
