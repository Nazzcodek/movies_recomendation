from rest_framework.test import APITestCase
from rest_framework import status


class MoviesAPITestCase(APITestCase):
    def test_search_movies(self):
        url = '/search_movies/'
        response = self.client.get(url, {'query': 'The Matrix'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

    def test_get_movie_details(self):
        url = '/get_movie_details/603'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Matrix')