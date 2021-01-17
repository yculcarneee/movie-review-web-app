from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apis.views import movies

class TestURLs(SimpleTestCase):

    def testMoviesURLIsResolved(self):
        url = reverse('movies')
        self.assertEquals(resolve(url).func, movies)

    def testMoviesWithPageNumArgURLIsResolved(self):
        url = reverse('moviesWithPageNum', args=['2'])
        self.assertEquals(resolve(url).func, movies)