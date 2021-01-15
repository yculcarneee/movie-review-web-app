from django.shortcuts import render
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import requests
import json

# Create your views here.
@api_view(["GET"])
def main(request):
    endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key='+settings.TMDB_API_KEY+'&language=en-US&sort_by=popularity.desc'
    response = requests.get(endpoint)

    data = response.json()

    movies = {}

    movies['page'] = data['page']
    movies['total_pages'] = data['total_pages']
    movies['total_results'] = data['total_results']
    movies['results'] = []

    for obj in data['results']:
        resultObj = {}

        resultObj['id'] = obj['id']
        resultObj['title'] = obj['title']
        resultObj['overview'] = obj['overview']
        resultObj['release_date'] = obj['release_date']
        resultObj['poster'] = 'https://image.tmdb.org/t/p/w500' + obj['poster_path']

        movies['results'].append(resultObj)

    return Response(status=status.HTTP_200_OK, data=movies)