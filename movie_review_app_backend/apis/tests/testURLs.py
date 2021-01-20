from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apis.views import movies, getMovieDetails

# Tests to check if API endpoints mentioned in urls.py resolve to their definitions in views.py
class TestURLs(SimpleTestCase):

    def testMoviesURLIsResolved(self):
        url = reverse('movies') # Retrieves view function called when we hit movies/ endpoint
        self.assertEquals(resolve(url).func, movies)

    def testMoviesWithPageNumArgURLIsResolved(self):
        url = reverse('moviesWithPageNum', args=['2']) # Retrieves view function called when we hit movies/ endpoint with page number passed as an argument
        self.assertEquals(resolve(url).func, movies)

    def testGetMovieDetailsURLIsResolved(self):
        url = reverse('getMovieDetails', args=['12345']) # Retrieves view function called when we hit getMovieDetails/ endpoint with movie id passed as an argument
        self.assertEquals(resolve(url).func, getMovieDetails)