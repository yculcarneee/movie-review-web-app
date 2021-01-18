from django.urls import path

from . import views

urlpatterns = [
    path('addToWatchedList/', views.addToWatchedList, name="addToWatchedList"),
    path('removeFromWatchedList/', views.removeFromWatchedList, name="removeFromWatchedList"),
    path('checkPageInWatchedList/', views.checkPageInWatchedList, name="checkPageInWatchedList"),
    path('updateMovieRating/', views.updateMovieRating, name="updateMovieRating"),
    path('getCurrentPageMovieRatings/', views.getCurrentPageMovieRatings, name="getCurrentPageMovieRatings"),
    path('getAllWatchedMoviesList/', views.getAllWatchedMoviesList, name="getAllWatchedMoviesList"),
    path('getAllRatedMoviesList/', views.getAllRatedMoviesList, name="getAllRatedMoviesList"),
]
