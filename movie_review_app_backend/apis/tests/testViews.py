from unittest.mock import Mock, patch
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

class TestViews(TestCase):
    # Test checks if the movies/ API endpoint filters movie details correctly in its response
    @patch('apis.views.requests.get')
    def testMoviesView(self, mock_get):
        mock_response = Mock() # Mock requests.get() call made to TMDB by movies/ endpoint
        
        expected_response = { 
            'page': 1,
            'total_pages': 500,
            'total_results': 1000,
            'results': [
                {
                      'adult': False, 
                      'backdrop_path': '/srYya1ZlI97Au4jUYAktDe3avyA.jpg', 
                      'genre_ids': [14, 28, 12], 
                      'id': 1, 
                      'original_language': 'en', 
                      'original_title': 'Dummy Text', 
                      'overview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam', 
                      'popularity': 4160.738, 
                      'poster_path': '/kqjL17yufvn9OVLyXYpvtyrFfak.jpg', 
                      'release_date': '2020-12-16', 
                      'title': 'Dummy Movie Name', 
                      'video': False, 
                      'vote_average': 7.1, 
                      'vote_count': 2781
                }
            ]
        }

        mock_response.json.return_value = expected_response # Set expected response to the mock function's response's json component
        mock_response.status_code = 200 # Set 200 status code for mock function's response

        mock_get.return_value = mock_response 

        response = self.client.get(reverse('movies')) # Issue GET call to movies/ endpoint

        results = response.json() # Recieve response from movies/ endpoint

        # Check if response sent by movies/ endpoint properly filters response sent by TMDB
        self.assertEquals(results, {
            'page': 1,
            'total_pages': 500,
            'total_results': 1000,
            'results': [
                {
                    'id': 1,
                    'title': 'Dummy Movie Name',
                    'overview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
                    'release_date': '2020-12-16',
                    'poster': 'https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg'
                }
            ]
        })

        page = 1
        endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key='+settings.TMDB_API_KEY+'&language=en-US&sort_by=popularity.desc&page='+str(page)

        mock_get.assert_called_once_with(endpoint) # Asserts that the call to movies/ API called above endpoint at least once

    # Test checks if the API endpoint filters movie details correctly in its response
    @patch('apis.views.requests.get')
    def testMoviesWithPageNumView(self, mock_get):
        mock_response = Mock() # Mock requests.get() call made to TMDB by movies/ endpoint
        
        expected_response = {
            'page': 3,
            'total_pages': 500,
            'total_results': 1000,
            'results': [
                {
                      'adult': False, 
                      'backdrop_path': '/srYya1ZlI97Au4jUYAktDe3avyA.jpg', 
                      'genre_ids': [14, 28, 12], 
                      'id': 1, 
                      'original_language': 'en', 
                      'original_title': 'Dummy Text', 
                      'overview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam', 
                      'popularity': 4160.738, 
                      'poster_path': '/kqjL17yufvn9OVLyXYpvtyrFfak.jpg', 
                      'release_date': '2020-12-16', 
                      'title': 'Dummy Movie Name', 
                      'video': False, 
                      'vote_average': 7.1, 
                      'vote_count': 2781
                }
            ]
        }

        mock_response.json.return_value = expected_response # Set expected response to the mock function's response's json component
        mock_response.status_code = 200 # Set 200 status code for mock function's response

        mock_get.return_value = mock_response

        response = self.client.get(reverse('moviesWithPageNum', args=['2'])) # Issue GET call to movies/ endpoint with page number 2 as argument

        results = response.json() # Recieve response from movies/ endpoint

        # Check if response sent by movies/ endpoint properly filters response sent by TMDB
        self.assertEquals(results, {
            'page': 3,
            'total_pages': 500,
            'total_results': 1000,
            'results': [
                {
                    'id': 1,
                    'title': 'Dummy Movie Name',
                    'overview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
                    'release_date': '2020-12-16',
                    'poster': 'https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg'
                }
            ]
        })

        page = 2
        endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key='+settings.TMDB_API_KEY+'&language=en-US&sort_by=popularity.desc&page='+str(page)

        mock_get.assert_called_once_with(endpoint) # Asserts that the call to movies/ API called above endpoint at least once
    
    # Test checks if the movies/page<page_num> API endpoint filters movie details correctly in its response
    @patch('apis.views.requests.get')
    def testGetMovieDetailsView(self, mock_get):
        mock_response = Mock()
        
        expected_response = {    
            'adult': False, 
            'backdrop_path': '/srYya1ZlI97Au4jUYAktDe3avyA.jpg', 
            'genre_ids': [14, 28, 12], 
            'id': 1, 
            'original_language': 'en', 
            'original_title': 'Dummy Text', 
            'overview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam', 
            'popularity': 4160.738, 
            'poster_path': '/kqjL17yufvn9OVLyXYpvtyrFfak.jpg', 
            'release_date': '2020-12-16', 
            'title': 'Dummy Movie Name', 
            'video': False, 
            'vote_average': 7.1, 
            'vote_count': 2781
        }

        mock_response.json.return_value = expected_response
        mock_response.status_code = 200

        mock_get.return_value = mock_response

        response = self.client.get(reverse('getMovieDetails', args=['1']))
        results = response.json()

        self.assertEquals(results, {
            'movieName': 'Dummy Movie Name',
            'movieOverview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
            'movieReleaseDate': '2020-12-16',
            'moviePoster': 'https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg'
        })

        movieId = 1
        endpoint = 'https://api.themoviedb.org/3/movie/' + str(movieId) + '?api_key=' + settings.TMDB_API_KEY + '&language=en-US'

        mock_get.assert_called_once_with(endpoint)