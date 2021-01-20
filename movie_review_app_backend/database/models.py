# models.py
from django.db import models

# WatchedMoviesDatabase contains two fields
# movieId - Integer (Primary Key)
# movieName - TextField 
class WatchedMoviesDatabase(models.Model):
    movieId = models.IntegerField(primary_key=True)
    movieName = models.TextField()

# MovieRatingDatabase contains three fields
# movieId - Integer (Primary Key)
# movieName - TextField
# movieRating - Integer
class MovieRatingDatabase(models.Model):
    movieId = models.IntegerField(primary_key=True)
    movieName = models.TextField()
    movieRating = models.IntegerField()
    