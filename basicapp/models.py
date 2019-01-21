from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfoModel(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username