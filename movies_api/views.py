import os
import requests
import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

api_token = os.environ.get('MOVIE_API_TOKEN')
logger = logging.getLogger(__name__)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_movies(request):
    """
    API endpoint for searching movies using the Free movies API.
    """
    try:
        query = request.query_params.get('query', '')
        api_url = f'https://rapidapi.com/rapidapi/api/movie-database-alternative/search/{query}'

        headers = {
            'X-RapidAPI-Host': 'movie-database-alternative.p.rapidapi.com',
            'X-RapidAPI-Key': api_token,
        }

        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error during API request: {e}")
        return Response({'error': 'An error occurred during the API request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movie_details(request, movie_id):
    """
    API endpoint for getting details of a single movie using the Free movies API.
    """
    try:
        api_url = f'https://rapidapi.com/rapidapi/api/movie-database-alternative/{movie_id}'

        headers = {
            'X-RapidAPI-Host': 'movie-database-alternative.p.rapidapi.com',
            'X-RapidAPI-Key': api_token,
        }

        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error during API request: {e}")
        return Response({'error': 'An error occurred during the API request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
