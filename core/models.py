from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from music import conf

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    ucity = models.CharField(max_length=16)

    def __unicode__(self):
        return self.user.username

    def get_user_city(self):
        return self.ucity

    def get_absolute_url(self):
        return reverse("core:user_detail", kwargs={"id":self.pk})

class Like(models.Model):
    user = models.ForeignKey('MyUser', related_name='like')
    artists = models.ForeignKey('artists.Artist', related_name='like')
    timestamp = models.DateTimeField(null=True, blank=True)

class Follow(models.Model):
    fan = models.ForeignKey('MyUser', related_name='fan')
    star = models.ForeignKey('MyUser', related_name='star')
    timestamp = models.DateTimeField(null=True, blank=True)