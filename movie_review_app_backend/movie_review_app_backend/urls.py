"""movie_review_app_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apis.views import main
from database.views import addToWatchedList, removeFromWatchedList, checkPageInWatchedList, updateMovieRating

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('movies/', main, name="main"),
    path('movies/page<int:page>', main, name="main"),
    path('addToWatchedList/', addToWatchedList, name="addToWatchedList"),
    path('removeFromWatchedList/', removeFromWatchedList, name="removeFromWatchedList"),
    path('checkPageInWatchedList/', checkPageInWatchedList, name="checkPageInWatchedList"),
    path('updateMovieRating/', updateMovieRating, name="updateMovieRating"),
]
