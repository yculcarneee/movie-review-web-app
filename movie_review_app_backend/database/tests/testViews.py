from django.test import TestCase, Client
from django.urls import reverse

from database.models import WatchedMoviesDatabase, MovieRatingDatabase

import json

class TestViews(TestCase):
    # Test checks if addToWatchedList/ actually adds an entry in the database
    def testAddToWatchedListView(self):
        
        # Send a POST request to addToWatchedList/ endpoint with movie details
        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")
        
        self.assertEquals(response.status_code, 200) # Verify response status code is 200
        self.assertEquals(WatchedMoviesDatabase.objects.get().movieName, 'DummyMovieName') # Verify movie name in response is correct
        self.assertEquals(WatchedMoviesDatabase.objects.get().movieId, 1) # Verify movie id in response is correct

    # Test checks if addToWatchedList/ verifies that movieId attribute is present in the request body
    def testAddToWatchedListView_MovieIdFieldMissing(self):

        # Send a POST request to addToWatchedList/ endpoint with incomplete movie details
        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify response status code is 404
        self.assertEquals(results['message'], 'movieId field missing in recieved movie entry') # Verify error message recieved is correct

    # Test checks if addToWatchedList/ verifies that movieName attribute is present in the request body
    def testAddToWatchedListView_MovieNameFieldMissing(self):

        # Send a POST request to addToWatchedList/ endpoint with incomplete movie details
        response = self.client.post(reverse('addToWatchedList'),  
                                    {'movieId': 1}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify response status code is 404
        self.assertEquals(results['message'], 'movieName field missing in recieved movie entry') # Verify error message is correct
    
    # Test checks if addToWatchedList/ verifies that movie in the request body is already present in the WatchedMovieDatabase
    def testAddToWatchedListView_MovieAlreadyPresent(self):

        self.testAddToWatchedListView() # Add an entry into WatchedMoviesDatabase
    
        # Send a POST request to addToWatchedList/ endpoint with movie details
        response = self.client.post(reverse('addToWatchedList'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 403) # Verify status code is 404
        self.assertEquals(results['message'], 'Movie already present in the watched movies list') # Verify error message is correct
    
    # Test checks if removeFromWatchedList/ actually removes an entry from the database
    def testRemoveFromWatchedListView(self):

        # Add an entry into WatchedMoviesDatabase
        WatchedMoviesDatabase.objects.create(
            movieId = 1,
            movieName = 'DummyMovieName'
        )

        self.assertEquals(WatchedMoviesDatabase.objects.count(), 1) # Verify that an entry is present in WatchedMoviesDatabase

        # Send a POST request to removeFromWatchedList/ endpoint with movie details 
        response = self.client.post(reverse('removeFromWatchedList'), 
                                    {'movieId': 1}, 
                                    content_type="application/json")

        self.assertEquals(response.status_code, 200) # Verify status code is 200
        self.assertEquals(WatchedMoviesDatabase.objects.count(), 0) # Verify that no entry exists in WatchedMoviesDatabase

    # Test checks if removeFromWatchedList/ verifies that movieId attribute is present in the request body
    def testRemoveFromWatchedListView_MovieIdFieldMissing(self):

        # Send a POST request to removeFromWatchedList/ endpoint with incomplete movie details
        response = self.client.post(reverse('removeFromWatchedList'), 
                                    {'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify status code is 404
        self.assertEquals(results['message'], 'movieId field missing in recieved movie entry') # Verify error message is correct

    # Test checks if removeFromWatchedList/ verifies that WatchedMoviesDatabase is not empty before attempting to remove entry
    def testRemoveFromWatchedListView_DatabaseEmpty(self):

        # Send a POST request to removeFromWatchedList/ endpoint to remove an entry from the database
        response = self.client.post(reverse('removeFromWatchedList'), 
                                    {'movieId': 1}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 403) # Verify status code is 403
        self.assertEquals(results['message'], 'Watched movies list is empty') # Verify error message is correct

    # Test checks if removeFromWatchedList/ verifies that movie is not present in the database before attempting to remove that entry
    def testRemoveFromWatchedListView_MovieNotPresent(self):

        # Add an entry into the database
        WatchedMoviesDatabase.objects.create(
            movieId = 1,
            movieName = 'DummyMovieName'
        )

        # Send a POST request to removeFromWatchedList/ endpoint to remove an entry from the database
        response = self.client.post(reverse('removeFromWatchedList'), 
                                    {'movieId': 2}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 403) # Verify status code is 403
        self.assertEquals(results['message'], 'Movie doesn\'t exist in the watched movies list') # Verify error message is correct

    # Test checks if checkPageInWatchedList/ correctly returns True or False values based on entries in the database
    def testCheckPageInWatchedListView(self):
        
        # Add 3 entries into WatchedMoviesDatabase
        WatchedMoviesDatabase.objects.bulk_create(
            [
                WatchedMoviesDatabase(movieId = 1),
                WatchedMoviesDatabase(movieId = 2),
                WatchedMoviesDatabase(movieId = 3)
            ]
        )

        # Send a POST request to checkPageInWatchedList/ endpoint to check if given array entries are present in WatchedMoviesDatabase
        response = self.client.post(reverse('checkPageInWatchedList'), 
                                    [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}], 
                                    content_type="application/json")

        result = json.loads(response.json())

        self.assertEquals(response.status_code, 200) # Verify response status code is 200

        # Verify response entries are correct
        self.assertEquals(result['1'], True)
        self.assertEquals(result['2'], True)
        self.assertEquals(result['3'], True)
        self.assertEquals(result['4'], False)
        self.assertEquals(result['5'], False)

    # Test checks if checkPageInWatchedList/ verifies that movieId attribute is present in the request body
    def testCheckPageInWatchedListView_IdFieldMissing(self):
        
        # Send a POST request to checkPageInWatchedList/ with incomplete movie details
        response = self.client.post(reverse('checkPageInWatchedList'), 
                                    [{'movieName': 'DummyMovieName'}], 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify status code is 404
        self.assertEquals(results['message'], 'id field missing in recieved movie list') # Verify error message is correct

    # Test checks if updateMovieRating/ updates the entry corresponding to the given movieId in MovieRatingDatabase
    def testUpdateMovieRatingView(self):

        # Add an entry into MovieRatingDatabase
        MovieRatingDatabase.objects.create(
            movieId = 1,
            movieName = 'DummyMovieName',
            movieRating = 3
        )

        self.assertEquals(MovieRatingDatabase.objects.get().movieRating, 3) # Verify that the entry in the database is correct

        # Send a POST request to updateMovieRating/ with movie details
        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName', 'movieRating': 5}, 
                                    content_type="application/json")
        
        self.assertEquals(response.status_code, 200) # Verify status code is 200
        self.assertEquals(MovieRatingDatabase.objects.get().movieRating, 5) # Verify that the entry in the database is updated

    # Test checks if updateMovieRating/ verifies that movieId attribute is present in the request body
    def testUpdateMovieRatingView_MovieIdFieldMissing(self):

        # Send a POST request to updateMovieRating/ with incomplete movie details
        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieName': 'DummyMovieName', 'movieRating': 5}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify status code is 404
        self.assertEquals(results['message'], 'movieId field missing in recieved movie entry') # Verify error message is correct

    # Test checks if updateMovieRating/ verifies that movieName attribute is present in the request body
    def testUpdateMovieRatingView_MovieNameFieldMissing(self):

        # Send a POST request to updateMovieRating/ with incomplete movie details
        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieId': 1, 'movieRating': 5}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify status code is 404
        self.assertEquals(results['message'], 'movieName field missing in recieved movie entry') # Verify error message is correct
    
    # Test checks if updateMovieRating/ verifies that movieRating attribute is present in the request body
    def testUpdateMovieRatingView_MovieRatingFieldMissing(self):

        # Send a POST request to updateMovieRating/ with incomplete movie details
        response = self.client.post(reverse('updateMovieRating'), 
                                    {'movieId': 1, 'movieName': 'DummyMovieName'}, 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify status code is 404
        self.assertEquals(results['message'], 'movieRating field missing in recieved movie entry') # Verify error message is correct

    # Test checks if getCurrentPageMovieRatings/ returns the ratings of movies mentioned in the request body
    def testGetCurrentPageMovieRatingsView(self):

        # Add 5 entries into MovieRatingDatabase
        MovieRatingDatabase.objects.bulk_create(
            [MovieRatingDatabase(movieId = 1, movieName = 'DummyMovieName1', movieRating = '5'),
             MovieRatingDatabase(movieId = 2, movieName = 'DummyMovieName2', movieRating = '4'),
             MovieRatingDatabase(movieId = 3, movieName = 'DummyMovieName3', movieRating = '3'),
             MovieRatingDatabase(movieId = 4, movieName = 'DummyMovieName4', movieRating = '2'),
             MovieRatingDatabase(movieId = 5, movieName = 'DummyMovieName5', movieRating = '1')
            ]
        )

        # Send a POST request to getCurrentPageMovieRatings/ endpoint with a list of movie ids
        response = self.client.post(reverse('getCurrentPageMovieRatings'), 
                                    [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 6}], 
                                    content_type="application/json")

        result = json.loads(response.json())

        self.assertEquals(response.status_code, 200) # Verify status code is 200

        # Verify response entries are correct
        self.assertEquals(result['1'], 5)
        self.assertEquals(result['2'], 4)
        self.assertEquals(result['3'], 3)
        self.assertEquals(result['4'], 2)
        self.assertEquals(result['5'], 1)
        self.assertEquals(result['6'], 0)

    # Test checks if getCurrentPageMovieRatings/ verifies that movieId attribute is present in the request body
    def testGetCurrentPageMovieRatingsView_MovieIdFieldMissing(self):
        
        # Send a POST request to getCurrentPageMovieRatings/ with incomplete movie details
        response = self.client.post(reverse('getCurrentPageMovieRatings'), 
                                    [{'movieName': 'DummyMovieName'}], 
                                    content_type="application/json")

        results = response.json()

        self.assertEquals(response.status_code, 404) # Verify status code is 404
        self.assertEquals(results['message'], 'id field missing in recieved movie list') # Verify error message is correct


