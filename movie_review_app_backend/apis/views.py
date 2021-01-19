from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import requests
import json

# Create your views here.
@api_view(["GET"])
def movies(request, page=1):

    endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key='+settings.TMDB_API_KEY+'&language=en-US&sort_by=popularity.desc&page='+str(page)
    response = requests.get(endpoint)

    data = response.json()

    movies = {}

    movies['page'] = data['page']
    movies['total_pages'] = data['total_pages']
    movies['total_results'] = data['total_results']
    movies['results'] = []

    for obj in data['results']:
        resultObj = {}

        if(obj['id']):
            resultObj['id'] = obj['id']
        else:
            resultObj['id'] = Math.random() * 100000

        if(obj['title']):
            resultObj['title'] = obj['title']
        else:
            resultObj['title'] = 'Title not available'

        if(obj['overview']):
            resultObj['overview'] = obj['overview']
        else:
            resultObj['overview'] = 'Overview not available'

        if(obj['release_date']):
            resultObj['release_date'] = obj['release_date']
        else:
            resultObj['release_date'] = 'Release date not available'

        if(obj['poster_path']):
            resultObj['poster'] = 'https://image.tmdb.org/t/p/w500' + obj['poster_path']
        else:
            resultObj['poster'] = 'https://via.placeholder.com/500'

        movies['results'].append(resultObj)

    return Response(status=status.HTTP_200_OK, data=movies)

@api_view(["GET"])
def getMovieDetails(request, movieId=1):
    
    endpoint = 'https://api.themoviedb.org/3/movie/' + str(movieId) + '?api_key=' + settings.TMDB_API_KEY + '&language=en-US'
    response = requests.get(endpoint)
    results = response.json()

    movieDetails = {}

    movieDetails['movieId'] = str(movieId)

    if(results['title']):
        movieDetails['movieName'] = results['title']
    else:
        movieDetails['movieName'] = 'Title not available'

    if(results['overview']):
        movieDetails['movieOverview'] = results['overview']
    else:
        movieDetails['movieOverview'] = 'Overview not available'

    if(results['release_date']):
        movieDetails['movieReleaseDate'] = results['release_date']
    else:
        movieDetails['movieReleaseDate'] = 'Release date not available'
    
    if(results['poster_path']):
        movieDetails['moviePoster'] = 'https://image.tmdb.org/t/p/w500' + results['poster_path']
    else:
        movieDetails['moviePoster'] = 'https://via.placeholder.com/500'

    return Response(status=status.HTTP_200_OK, data=movieDetails)

