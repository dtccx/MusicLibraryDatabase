from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    ucity = models.CharField(max_length=16)

    def __unicode__(self):
        return self.user.username