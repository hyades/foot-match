from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)


class Game(models.Model):
    game_name = models.CharField(max_length=30)
    game_desc = models.CharField(max_length=50)
    users = models.ManyToManyField(User)


class Score(models.Model):
    score_desc = models.CharField(max_length=50)


class Match(models.Model):
    match_time = models.DateTimeField()
    score = models.OneToOneField(Score, null=True)
    game = models.ForeignKey(Game, null=True)
    users = models.ManyToManyField(User)
