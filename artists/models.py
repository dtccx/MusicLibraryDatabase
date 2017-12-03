from django.db import models
from django.core.urlresolvers import reverse

class Artist (models.Model):
    #artist name
    name = models.CharField(max_length = 40)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_song_names(self):
        song_names = [song.name for song in self.song_set.all()]
        return ", ".join(song_names)

    def get_absolute_url(self):
        return reverse("artists:artist_detail", kwargs={"id":self.pk})
