from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from music import conf

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, related_name='myuser')
    nickname = models.CharField(max_length=16)
    ucity = models.CharField(max_length=16)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("core:user_detail", kwargs={"id":self.pk})

    def get_follow(self):
        return "\n".join([s.user.username for s in self.star.all()])

class Like(models.Model):
    user = models.ForeignKey('MyUser', related_name='like')
    artist = models.ForeignKey('artists.Artist', related_name='like')
    timestamp = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        unique_together = ('user', 'artist')

    def get_user(self):
        return str(self.user.user.username)

    def get_artist(self):
        return str(self.artist.name)

class Follow(models.Model):
    fan = models.ForeignKey('MyUser', related_name='star')
    star = models.ForeignKey('MyUser', related_name='fan')
    timestamp = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        unique_together = ('fan', 'star')

    def followee(self):
        return str(self.star.name)

    def follower(self):
        return str(self.fan.user.username)