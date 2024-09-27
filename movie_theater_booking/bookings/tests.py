from django.test import TestCase
from .models import Movie
from django.utils import timezone

class MovieModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='This is a test movie',
            release_date=timezone.datetime(2024, 9, 27).date(),
            duration=120
        )
    
    def test_movie_model(self):
        movie = Movie.objects.get(id=self.movie.id)
        self.assertEqual(movie.title, 'Test Movie')
        self.assertEqual(movie.description, 'This is a test movie')
        self.assertEqual(movie.release_date, timezone.datetime(2024, 9, 27).date())
        self.assertEqual(movie.duration, 120)
