from django.urls import path

from . import views

urlpatterns = [
    path('', views.movies, name="movies"), # Default endpoint to retrieve list of movies, assumes page number is 1
    path('page<int:page>/', views.movies, name="moviesWithPageNum"), # Endpoint to get movies list for a specific page number
    path('getMovieDetails/<int:movieId>', views.getMovieDetails, name="getMovieDetails") # Endpoint to get relevant details for a movie with given movie id
]
