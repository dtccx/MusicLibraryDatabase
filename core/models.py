from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    ucity = models.CharField(max_length=16)

    def __unicode__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey('MyUser', related_name='user')
    artists = models.ForeignKey('artists.Artist', related_name='artist')
    timestamp = models.DateTimeField(null=True, blank=True)

class Follow(models.Model):
    fan = models.ForeignKey('MyUser', related_name='user')
    star = models.ForeignKey('MyUser', related_name='user')
    timestamp = models.DateTimeField(null=True, blank=True)