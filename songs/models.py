from django.db import models
from django.core.urlresolvers import reverse

class Song (models.Model):
    #song name
    name = models.CharField(max_length=100)
    #song length
    length = models.DurationField()
    #song track number
    track_number = models.IntegerField()
    #song artists
    artists = models.ManyToManyField("artists.Artist", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_artist_names(self):
        artist_names = [artist.name for artist in self.artists.all()]
        return ", ".join(artist_names)

    def get_absolute_url(self):
        return reverse("songs:song_detail", kwargs={"id":self.pk})
