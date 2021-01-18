from django.urls import path

from . import views

urlpatterns = [
    path('', views.movies, name="movies"),
    path('page<int:page>/', views.movies, name="moviesWithPageNum"),
    path('getMoviePoster/<int:movieId>', views.getMoviePoster, name="getMoviePoster")
]
