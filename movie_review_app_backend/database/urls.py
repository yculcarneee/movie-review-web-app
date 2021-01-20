from django.urls import path

from . import views

urlpatterns = [
    path('addToWatchedList/', views.addToWatchedList, name="addToWatchedList"), # Endpoint to add a given movie into the WatchedListDatabase
    path('removeFromWatchedList/', views.removeFromWatchedList, name="removeFromWatchedList"), # Endpoint to remove a given movie from the WatchedListDatabase
    path('checkPageInWatchedList/', views.checkPageInWatchedList, name="checkPageInWatchedList"), # Endpoint to check which of the movies in the current page are present in the WatchedListDatabase
    path('updateMovieRating/', views.updateMovieRating, name="updateMovieRating"), # Endpoint to add/update the rating given to a movie in the MovieRatingDatabase
    path('getCurrentPageMovieRatings/', views.getCurrentPageMovieRatings, name="getCurrentPageMovieRatings"), # Endpoint to get the ratings of the movies present in the current page from the MovieRatingDatabase
    path('getAllWatchedMoviesList/', views.getAllWatchedMoviesList, name="getAllWatchedMoviesList"), # Endpoint to get all the entries from the WatchedMoviesDatabase
    path('getAllRatedMoviesList/', views.getAllRatedMoviesList, name="getAllRatedMoviesList"), # Endpoint to get all the entries from the RatedMoviesDatabase
]
