from django.test import SimpleTestCase
from django.urls import reverse, resolve

from database.views import addToWatchedList, removeFromWatchedList, checkPageInWatchedList, updateMovieRating, getCurrentPageMovieRatings

class TestURLs(SimpleTestCase):

    def testAddToWatchedListURLIsResolved(self):
        url = reverse('addToWatchedList')
        self.assertEquals(resolve(url).func, addToWatchedList)

    def testRemoveFromWatchedListURLIsResolved(self):
        url = reverse('removeFromWatchedList')
        self.assertEquals(resolve(url).func, removeFromWatchedList)

    def testCheckPageInWatchedListURLIsResolved(self):
        url = reverse('checkPageInWatchedList')
        self.assertEquals(resolve(url).func, checkPageInWatchedList)
    
    def testUpdateMovieRatingURLIsResolved(self):
        url = reverse('updateMovieRating')
        self.assertEquals(resolve(url).func, updateMovieRating)

    def testGetCurrentPageMovieRatingsURLIsResolved(self):
        url = reverse('getCurrentPageMovieRatings')
        self.assertEquals(resolve(url).func, getCurrentPageMovieRatings)