from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    release_year = models.IntegerField()
    players_number = models.IntegerField()
    play_time = models.IntegerField(help_text="Time in minutes")
    min_age = models.IntegerField(help_text="Minimum age recommendation")