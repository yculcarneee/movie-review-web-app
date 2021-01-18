from django.test import TestCase, Client
from django.urls import reverse

from database.models import WatchedMoviesDatabase, MovieRatingDatabase

import json

class TestViews(TestCase):

    def testAddToWatchedListView(self):
        
        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(WatchedMoviesDatabase.objects.get().movieName, 'DummyMovieName')
        self.assertEquals(WatchedMoviesDatabase.objects.get().movieId, 1)

    def testAddToWatchedListView_MovieIdFieldMissing(self):

        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'movieId field missing in recieved movie entry')

    def testAddToWatchedListView_MovieNameFieldMissing(self):

        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieId': 1}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'movieName field missing in recieved movie entry')

    def testAddToWatchedListView_MovieAlreadyPresent(self):

        self.testAddToWatchedListView()
    
        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 403)
        self.assertEquals(results['message'], 'Movie already present in the watched movies list')
    
    def testRemoveFromWatchedListView(self):

        WatchedMoviesDatabase.objects.create(
            movieId = 1,
            movieName = 'DummyMovieName'
        )

        self.assertEquals(WatchedMoviesDatabase.objects.count(), 1)

        response = self.client.post(reverse('removeFromWatchedList'), 
                                    {'movieId': 1}, 
                                    content_type="application/json")

        self.assertEquals(response.status_code, 200)
        self.assertEquals(WatchedMoviesDatabase.objects.count(), 0)

    def testRemoveFromWatchedListView_MovieIdFieldMissing(self):

        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'movieId field missing in recieved movie entry')

    def testRemoveFromWatchedListView_DatabaseEmpty(self):

        response = self.client.post(reverse('removeFromWatchedList'), 
                                    {'movieId': 1}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 403)
        self.assertEquals(results['message'], 'Watched movies list is empty')

    def testRemoveFromWatchedListView_MovieNotPresent(self):

        WatchedMoviesDatabase.objects.create(
            movieId = 1,
            movieName = 'DummyMovieName'
        )

        response = self.client.post(reverse('removeFromWatchedList'), 
                                    {'movieId': 2}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 403)
        self.assertEquals(results['message'], 'Movie doesn\'t exist in the watched movies list')

    def testCheckPageInWatchedListView(self):
        
        WatchedMoviesDatabase.objects.bulk_create(
            [WatchedMoviesDatabase(movieId = 1),
             WatchedMoviesDatabase(movieId = 2),
             WatchedMoviesDatabase(movieId = 3)
            ]
        )

        response = self.client.post(reverse('checkPageInWatchedList'), 
                                    [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}], 
                                    content_type="application/json")

        result = json.loads(response.json())

        self.assertEquals(response.status_code, 200)
        self.assertEquals(result['1'], True)
        self.assertEquals(result['2'], True)
        self.assertEquals(result['3'], True)
        self.assertEquals(result['4'], False)
        self.assertEquals(result['5'], False)

    def testCheckPageInWatchedListView_IdFieldMissing(self):
        
        response = self.client.post(reverse('checkPageInWatchedList'), 
                                    [{'movieName': 'DummyMovieName'}], 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'id field missing in recieved movie list')

    def testUpdateMovieRatingView(self):

        MovieRatingDatabase.objects.create(
            movieId = 1,
            movieName = 'DummyMovieName',
            movieRating = 3
        )

        self.assertEquals(MovieRatingDatabase.objects.get().movieRating, 3)

        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName', 'movieRating': 5}, 
                                    content_type="application/json")
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(MovieRatingDatabase.objects.get().movieRating, 5)

    def testUpdateMovieRatingView_MovieIdFieldMissing(self):

        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieName': 'DummyMovieName', 'movieRating': 5}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'movieId field missing in recieved movie entry')

    def testUpdateMovieRatingView_MovieNameFieldMissing(self):

        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieId': 1, 'movieRating': 5}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'movieName field missing in recieved movie entry')

    def testUpdateMovieRatingView_MovieRatingFieldMissing(self):

        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'movieRating field missing in recieved movie entry')

    def testGetCurrentPageMovieRatingsView(self):

        MovieRatingDatabase.objects.bulk_create(
            [MovieRatingDatabase(movieId = 1, movieName = 'DummyMovieName1', movieRating = '5'),
             MovieRatingDatabase(movieId = 2, movieName = 'DummyMovieName2', movieRating = '4'),
             MovieRatingDatabase(movieId = 3, movieName = 'DummyMovieName3', movieRating = '3'),
             MovieRatingDatabase(movieId = 4, movieName = 'DummyMovieName4', movieRating = '2'),
             MovieRatingDatabase(movieId = 5, movieName = 'DummyMovieName5', movieRating = '1')
            ]
        )

        response = self.client.post(reverse('getCurrentPageMovieRatings'), 
                                    [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 6}], 
                                    content_type="application/json")

        result = json.loads(response.json())

        self.assertEquals(response.status_code, 200)
        self.assertEquals(result['1'], 5)
        self.assertEquals(result['2'], 4)
        self.assertEquals(result['3'], 3)
        self.assertEquals(result['4'], 2)
        self.assertEquals(result['5'], 1)
        self.assertEquals(result['6'], 0)

    def testGetCurrentPageMovieRatingsView_MovieIdFieldMissing(self):
        
        response = self.client.post(reverse('getCurrentPageMovieRatings'), 
                                    [{'movieName': 'DummyMovieName'}], 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404)
        self.assertEquals(results['message'], 'id field missing in recieved movie list')


