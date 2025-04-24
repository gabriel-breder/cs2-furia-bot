from django.db import models

class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    social_media = models.ManyToManyField(SocialMedia, blank=True)

class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, blank=True)
    social_media = models.ManyToManyField(SocialMedia, blank=True)

class Match(models.Model):
    date = models.DateTimeField()
    opponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches')
    result = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(blank=True, null=True)