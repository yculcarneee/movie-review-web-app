from django.shortcuts import render
from django.http import HttpRequest 
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import WatchedMoviesDatabase

import json

# Create your views here.
@api_view(["POST"])
def addToWatchedList(request: HttpRequest):
    
    data = json.loads(request.body)

    databaseEntry = WatchedMoviesDatabase(movieId = data['movieId'], movieName = data['movieName'])
    databaseEntry.save()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def removeFromWatchedList(request):

    data = json.loads(request.body)

    databaseEntry = WatchedMoviesDatabase.objects.get(movieId = data['movieId'])
    databaseEntry.delete()

    return Response(status=status.HTTP_200_OK)