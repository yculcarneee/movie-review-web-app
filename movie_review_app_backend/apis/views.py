from django.shortcuts import render
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import requests

# Create your views here.
@api_view(["GET"])
def main(request):
    endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key='+settings.TMDB_API_KEY+'&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
    response = requests.get(endpoint)

    movies = response.json()

    return Response(status=status.HTTP_200_OK, data={"movies": movies})