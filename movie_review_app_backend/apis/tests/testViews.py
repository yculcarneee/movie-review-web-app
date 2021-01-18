from unittest.mock import Mock, patch
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

class TestViews(TestCase):

    @patch('apis.views.requests.get')
    def testMoviesView(self, mock_get):
        mock_response = Mock()
        
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

        mock_response.json.return_value = expected_response
        mock_response.status_code = 200

        mock_get.return_value = mock_response

        response = self.client.get(reverse('movies'))

        results = response.json()

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

        mock_get.assert_called_once_with(endpoint)

    @patch('apis.views.requests.get')
    def testMoviesWithPageNumView(self, mock_get):
        mock_response = Mock()
        
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

        mock_response.json.return_value = expected_response
        mock_response.status_code = 200

        mock_get.return_value = mock_response

        response = self.client.get(reverse('moviesWithPageNum', args=['2']))

        results = response.json()

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

        mock_get.assert_called_once_with(endpoint)