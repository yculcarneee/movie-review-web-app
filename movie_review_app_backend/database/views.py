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

# addToWatchedList/ endpoint adds given movie in request body into the WatchedMoviesDatabase
@api_view(["POST"])
def addToWatchedList(request: HttpRequest):
    
    data = json.loads(request.body) # Get movie details from request body

    # Checks if movieId, movieName attributes are present in the request body, returns Error if not present
    if('movieId' not in data.keys()):
        return JsonResponse({'message': 'movieId field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if('movieName' not in data.keys()):
        return JsonResponse({'message': 'movieName field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    # Checks if movieId is already present in the database, returns Error if movie is already present
    if(WatchedMoviesDatabase.objects.filter(movieId = data['movieId']).exists()):
        return JsonResponse({'message': 'Movie already present in the watched movies list'}, status=status.HTTP_403_FORBIDDEN)

    # Add (movieId, movieName) entry to the database
    databaseEntry = WatchedMoviesDatabase(movieId = data['movieId'], movieName = data['movieName'])
    databaseEntry.save() # Save the database state

    return Response(status=status.HTTP_200_OK)

# removeFromWatchedList/ endpoint removes given movie from the WatchedMoviesDatabase
@api_view(["POST"])
def removeFromWatchedList(request):

    data = json.loads(request.body) # Get movie details from request body

    # Checks if movieId attribute is present in the request body, returns Error if not present
    if('movieId' not in data.keys()):
        return JsonResponse({'message': 'movieId field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    # If database is empty, return error
    if(WatchedMoviesDatabase.objects.count() == 0):
        return JsonResponse({'message': 'Watched movies list is empty'}, status=status.HTTP_403_FORBIDDEN)

    # Checks if movie is not present in the database, returns error if True
    if(not WatchedMoviesDatabase.objects.filter(movieId = data['movieId']).exists()):
        return JsonResponse({'message': 'Movie doesn\'t exist in the watched movies list'}, status=status.HTTP_403_FORBIDDEN)

    # Remove (movieId) from the database
    databaseEntry = WatchedMoviesDatabase.objects.get(movieId = data['movieId'])
    databaseEntry.delete() # Save the database state

    return Response(status=status.HTTP_200_OK)

# checkPageInWatchedList/ endpoint takes a list of movies and checks if they are present in the WatchedMoviesDatabase
@api_view(["POST"])
def checkPageInWatchedList(request):

    data = json.loads(request.body) # Get movieIds list from request body

    response = {} # Response body to be sent by checkPageInWatchedList/

    for entry in data:
        if('id' not in entry.keys()): # If any of the entries recieved in the request do not have id field, return Error
            return JsonResponse({'message': 'id field missing in recieved movie list'}, status=status.HTTP_404_NOT_FOUND)

        # Set entry to be True or False, based on whether it exists in the database or not
        response[entry['id']] = WatchedMoviesDatabase.objects.filter(movieId = entry['id']).exists()

    return Response(status=status.HTTP_200_OK, data=response)

# updateMovieRating/ endpoint adds/updates the rating given to a movie in the MovieRatingDatabase
@api_view(["POST"])
def updateMovieRating(request: HttpRequest):
    
    data = json.loads(request.body) # Get movie details from the request body

    # Checks if movieId, movieName, movieRating attributes are present in the request body, returns Error if not
    if('movieId' not in data.keys()):
        return JsonResponse({'message': 'movieId field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if('movieName' not in data.keys()):
        return JsonResponse({'message': 'movieName field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    if('movieRating' not in data.keys()):
        return JsonResponse({'message': 'movieRating field missing in recieved movie entry'}, status=status.HTTP_404_NOT_FOUND)

    # Add/update entry of movie in the database
    database = MovieRatingDatabase(movieId = data['movieId'], movieName = data['movieName'], movieRating = data['movieRating'])
    database.save() # Save state of database

    return Response(status=status.HTTP_200_OK)

# getCurrentPageMovieRatings/ endpoint takes a list of movies and returns an object containing the rating of those movies
@api_view(["POST"])
def getCurrentPageMovieRatings(request: HttpRequest):
    
    data = json.loads(request.body) # Get movieIds from the request body

    response = {} # Response body to be returned by getCurrentPageMovieRatings/

    for entry in data:
        if('id' not in entry.keys()): # If any of the entries recieved in the request body do not have id attribute, return Error
            return JsonResponse({'message': 'id field missing in recieved movie list'}, status=status.HTTP_404_NOT_FOUND)

        # If the movie exists in the MovieRatingDatabase, retrieve the rating from the database and assign it to corresponding movieId. Else, set it to 0
        if(MovieRatingDatabase.objects.filter(movieId = entry['id']).exists()):
            response[entry['id']] = MovieRatingDatabase.objects.get(movieId = entry['id']).movieRating
        else:
            response[entry['id']] = 0

    return Response(status=status.HTTP_200_OK, data=response)

# getAllWatchedMoviesList/ endpoint returns all the entries present in the WatchedMoviesDatabase
@api_view(["GET"])
def getAllWatchedMoviesList(request: HttpRequest):
    
    watchedMoviesList = [] # Response body to be sent by getAllWatchedMoviesList/ endpoint

    # Iterating over all entries in WatchedMoviesDatabase
    for entry in WatchedMoviesDatabase.objects.all():

        response = requests.get('http://127.0.0.1:8000/movies/getMovieDetails/'+str(entry.movieId)) # Call getMovieDetails/ endpoint to get other details of the movie such as overview, release date, and poster
        results = response.json()

        watchedMoviesList.append(results) # Add entry to the response to be sent by getAllWatchedMoviesList/

    return Response(status=status.HTTP_200_OK, data=watchedMoviesList)

# getAllRatedMoviesList/ endpoint returns all the entries present in the MovieRatingDatabase
@api_view(["GET"])
def getAllRatedMoviesList(request: HttpRequest):
    
    ratedMoviesList = [] # Response body to be sent by getAllRatedMoviesList/ endpoint

    # Iterating over all entries in MovieRatingDatabase
    for entry in MovieRatingDatabase.objects.all():

        response = requests.get('http://127.0.0.1:8000/movies/getMovieDetails/'+str(entry.movieId)) # Call getMovieDetails/ endpoint to get other details of the movie such as overview, release date, and poster
        results = response.json()

        results['movieRating'] = entry.movieRating # Assign movie rating to entry in response body

        ratedMoviesList.append(results) # Add entry to the response to be sent by getAllRatedMoviesList/

    return Response(status=status.HTTP_200_OK, data=ratedMoviesList)