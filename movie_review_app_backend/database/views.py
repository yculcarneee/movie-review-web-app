from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import WatchedMoviesDatabase, MovieRatingDatabase

import json
import requests

# Create your views here.
@api_view(["POST"])
def addToWatchedList(request: HttpRequest):
    
    data = json.loads(request.body)

    if('movieId' not in data.keys()):
        return JsonResponse({'message': 'movieId field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if('movieName' not in data.keys()):
        return JsonResponse({'message': 'movieName field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if(WatchedMoviesDatabase.objects.filter(movieId = data['movieId']).exists()):
        return JsonResponse({'message': 'Movie already present in the watched movies list'}, status=status.HTTP_403_FORBIDDEN)

    databaseEntry = WatchedMoviesDatabase(movieId = data['movieId'], movieName = data['movieName'])
    databaseEntry.save()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def removeFromWatchedList(request):

    data = json.loads(request.body)

    if('movieId' not in data.keys()):
        return JsonResponse({'message': 'movieId field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if(WatchedMoviesDatabase.objects.count() == 0):
        return JsonResponse({'message': 'Watched movies list is empty'}, status=status.HTTP_403_FORBIDDEN)

    if(not WatchedMoviesDatabase.objects.filter(movieId = data['movieId']).exists()):
        return JsonResponse({'message': 'Movie doesn\'t exist in the watched movies list'}, status=status.HTTP_403_FORBIDDEN)

    databaseEntry = WatchedMoviesDatabase.objects.get(movieId = data['movieId'])
    databaseEntry.delete()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def checkPageInWatchedList(request):

    data = json.loads(request.body)

    response = {}

    for entry in data:
        if('id' not in entry.keys()):
            return JsonResponse({'message': 'id field missing in recieved movie list'}, status=status.HTTP_404_NOT_FOUND)

        response[entry['id']] = WatchedMoviesDatabase.objects.filter(movieId = entry['id']).exists()

    return Response(status=status.HTTP_200_OK, data=json.dumps(response))

@api_view(["POST"])
def updateMovieRating(request: HttpRequest):
    
    data = json.loads(request.body)

    if('movieId' not in data.keys()):
        return JsonResponse({'message': 'movieId field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if('movieName' not in data.keys()):
        return JsonResponse({'message': 'movieName field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if('movieRating' not in data.keys()):
        return JsonResponse({'message': 'movieRating field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    database = MovieRatingDatabase(movieId = data['movieId'], movieName = data['movieName'], movieRating = data['movieRating'])
    database.save()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def getCurrentPageMovieRatings(request: HttpRequest):
    
    data = json.loads(request.body)

    response = {}

    for entry in data:
        if('id' not in entry.keys()):
            return JsonResponse({'message': 'id field missing in recieved movie list'}, status=status.HTTP_404_NOT_FOUND)

        if(MovieRatingDatabase.objects.filter(movieId = entry['id']).exists()):
            response[entry['id']] = MovieRatingDatabase.objects.get(movieId = entry['id']).movieRating
        else:
            response[entry['id']] = 0

    return Response(status=status.HTTP_200_OK, data=json.dumps(response))

@api_view(["GET"])
def getAllWatchedMoviesList(request: HttpRequest):
    
    watchedMoviesList = []

    for entry in WatchedMoviesDatabase.objects.all():

        watchedMoviesListEntry = {}

        watchedMoviesListEntry['movieId'] = entry.movieId
        watchedMoviesListEntry['movieName'] = entry.movieName

        response = requests.get('http://127.0.0.1:8000/movies/getMoviePoster/'+str(entry.movieId))
        watchedMoviesListEntry['poster'] = response.json()

        watchedMoviesList.append(watchedMoviesListEntry)

    return Response(status=status.HTTP_200_OK, data=watchedMoviesList)

@api_view(["GET"])
def getAllRatedMoviesList(request: HttpRequest):
    
    ratedMoviesList = []

    for entry in MovieRatingDatabase.objects.all():

        ratedMoviesListEntry = {}

        ratedMoviesListEntry['movieId'] = entry.movieId
        ratedMoviesListEntry['movieName'] = entry.movieName
        ratedMoviesListEntry['movieRating'] = entry.movieRating

        response = requests.get('http://127.0.0.1:8000/movies/getMoviePoster/'+str(entry.movieId))
        ratedMoviesListEntry['poster'] = response.json()

        ratedMoviesList.append(ratedMoviesListEntry)

    return Response(status=status.HTTP_200_OK, data=ratedMoviesList)