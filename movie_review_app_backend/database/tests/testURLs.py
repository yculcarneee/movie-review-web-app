from django.test import SimpleTestCase
from django.urls import reverse, resolve

from database.views import addToWatchedList, removeFromWatchedList, checkPageInWatchedList, updateMovieRating, getCurrentPageMovieRatings

# Tests to check if API endpoints mentioned in urls.py resolve to their definitions in views.py
class TestURLs(SimpleTestCase):

    def testAddToWatchedListURLIsResolved(self):
        url = reverse('addToWatchedList') # Retrieves view function called when we hit addToWatchedList/ endpoint
        self.assertEquals(resolve(url).func, addToWatchedList)

    def testRemoveFromWatchedListURLIsResolved(self):
        url = reverse('removeFromWatchedList') # Retrieves view function called when we hit removeFromWatchedList/ endpoint
        self.assertEquals(ressolve(url).func, removeFromWatchedList)

    def testCheckPageInWatchedListURLIsResolved(self):
        url = reverse('checkPageInWatchedList') # Retrieves view function called when we hit checkPageInWatchedList/ endpoint
        self.assertEquals(resolve(url).func, checkPageInWatchedList)
    
    def testUpdateMovieRatingURLIsResolved(self):
        url = reverse('updateMovieRating') # Retrieves view function called when we hit updateMovieRating/ endpoint
        self.assertEquals(resolve(url).func, updateMovieRating)

    def testGetCurrentPageMovieRatingsURLIsResolved(self):
        url = reverse('getCurrentPageMovieRatings')# Retrieves view function called when we hit getCurrentPageMovieRatings/ endpoint
        self.assertEquals(resolve(url).func, getCurrentPageMovieRatings)