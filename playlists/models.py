from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Playlist(models.Model):
    playlist_name = models.CharField(max_length=250)
    creator = models.ForeignKey("core.MyUser", related_name='playlist')
    year_released = models.DateField(max_length=8)
    song = models.ManyToManyField('songs.Song', related_name='playlist')

    def __unicode__(self):
        return self.playlist_name

    def get_absolute_url(self):
        return reverse("playlists:playlist_list", kwargs={self.pk})

    def get_song(self):
        return "\n".join([s.name for s in self.song.all()])