from django.urls import path

from . import views

urlpatterns = [
    path('', views.movies, name="main"),
    path('page<int:page>/', views.movies, name="main")
]
