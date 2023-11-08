from django.urls import path
from .views import search_movies, get_movie_details

urlpatterns = [
    path('search/', search_movies, name='search-movies'),
    path('details/<str:movie_id>/', get_movie_details, name='get-movie-details'),
]
