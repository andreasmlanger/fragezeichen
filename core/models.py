from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Episodes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='episodes', null=True)
    episode = models.IntegerField()
