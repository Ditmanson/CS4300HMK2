from django.test import TestCase
from django.urls import reverse
from .models import *
from rest_framework import status
# Create your tests here.

class MovieModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='This is a test movie',
            release_date='2024-09-27',
            duration=120
        )
    
    def test_movie_model(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.title, 'Test Movie')
        self.assertEqual(movie.description, 'This is a test movie')
        self.assertEqual(movie.release_date, '2024-09-27')
        self.assertEqual(movie.duration, 120)
