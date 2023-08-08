from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.PROTECT)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)


class Item(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.PROTECT)


class Profile(models.Model):
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, default=None, on_delete=models.PROTECT)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    following = models.ManyToManyField(User, related_name="followers")