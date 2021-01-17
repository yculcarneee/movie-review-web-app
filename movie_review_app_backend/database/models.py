# models.py
from django.db import models

# Create your models here.
class WatchedMoviesDatabase(models.Model):
    movieId = models.IntegerField(primary_key=True)
    movieName = models.TextField()

class MovieRatingDatabase(models.Model):
    movieId = models.IntegerField(primary_key=True)
    movieName = models.TextField()
    movieRating = models.IntegerField()
    