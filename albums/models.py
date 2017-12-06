from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime

class Album(models.Model):
    album_name = models.CharField(max_length=250)
    year_released = models.DateField(max_length=8)
    track = models.ManyToManyField('songs.Song', related_name='album')

    def __unicode__(self):
        return self.album_name

    def get_absolute_url(self):
        return reverse("albums:album_list", kwargs={self.pk})
