from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import WatchedMoviesDatabase, MovieRatingDatabase

import json

# Create your views here.
@api_view(["POST"])
def addToWatchedList(request: HttpRequest):
    
    data = json.loads(request.body)

    if(WatchedMoviesDatabase.objects.filter(movieId = data['movieId']).exists()):
        return JsonResponse({'message': 'Movie already present in the watched movies list'}, status=status.HTTP_403_FORBIDDEN)

    databaseEntry = WatchedMoviesDatabase(movieId = data['movieId'], movieName = data['movieName'])
    databaseEntry.save()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def removeFromWatchedList(request):

    data = json.loads(request.body)

    databaseEntry = WatchedMoviesDatabase.objects.get(movieId = data['movieId'])
    databaseEntry.delete()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def checkPageInWatchedList(request):

    data = json.loads(request.body)

    response = {}

    for entry in data:
        response[entry['id']] = WatchedMoviesDatabase.objects.filter(movieId = entry['id']).exists()

    return Response(status=status.HTTP_200_OK, data=json.dumps(response))

@api_view(["POST"])
def updateMovieRating(request: HttpRequest):
    
    data = json.loads(request.body)

    database = MovieRatingDatabase(movieId = data['movieId'], movieName = data['movieName'], movieRating = data['movieRating'])
    database.save()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def getCurrentPageMovieRatings(request: HttpRequest):
    
    data = json.loads(request.body)

    response = {}

    for entry in data:
        if(MovieRatingDatabase.objects.filter(movieId = entry['id']).exists()):
            response[entry['id']] = MovieRatingDatabase.objects.get(movieId = entry['id']).movieRating
        else:
            response[entry['id']] = 0

    return Response(status=status.HTTP_200_OK, data=json.dumps(response))