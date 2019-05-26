from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    #position = models.CharField(max_length=100)

    def __str__(self):
        return self.username
