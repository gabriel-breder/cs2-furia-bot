from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='players')
    instagram = models.URLField(blank=True, null=True)
    twitch = models.URLField(blank=True, null=True)


class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()

class Team(models.Model):
    name = models.CharField(max_length=100)

class Match(models.Model):
    date = models.DateTimeField()
    teamA = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamA_matches')
    teamB = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamB_matches')
    teamA_score = models.IntegerField()
    teamB_score = models.IntegerField()
    match_details = models.URLField(blank=True, null=True)
