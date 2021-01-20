from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import requests
import json

# movies/ endpoint fetches most popular movies from TMDB based on given page name and returns filtered results
@api_view(["GET"])
def movies(request, page=1):

    # Fetch most popular movies from TMDB based on given page name
    endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key='+settings.TMDB_API_KEY+'&language=en-US&sort_by=popularity.desc&page='+str(page)
    
    try:
        response = requests.get(endpoint)
    except (requests.ConnectTimeout, requests.HTTPError, requests.ReadTimeout, requests.Timeout, requests.ConnectionError):
        return Response(status=status.HTTP_408_TIMEOUT, data={})
    

    data = response.json()

    # Response object to be sent by API
    movies = {}

    # Extract page number, total number of pages, total number of results from recieved data
    movies['page'] = data['page']
    movies['total_pages'] = data['total_pages']
    movies['total_results'] = data['total_results']
    movies['results'] = []

    # Extract movie id, title, overview, release date and poster path from results array 
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

# getMovieDetails/ endpoint fetches movie details from TMDB such as movie name, overview, releae date, and poster path and returns result object
@api_view(["GET"])
def getMovieDetails(request, movieId=1):
    
    # Fetch movie details from TMDB based on movie id
    endpoint = 'https://api.themoviedb.org/3/movie/' + str(movieId) + '?api_key=' + settings.TMDB_API_KEY + '&language=en-US'
    response = requests.get(endpoint)
    results = response.json()

    # Response object to be sent by API
    movieDetails = {}

    movieDetails['movieId'] = str(movieId)

    # Filter out movie name, overview, release date, and poster path from results object and copy it into movieDetails object
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

