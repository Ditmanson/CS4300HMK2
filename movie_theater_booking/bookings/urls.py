from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('',  index, name='index'),
    path('api/', include(router.urls)),
    path('api/test/', getTestData, name='test-data'),
    # webpages
    path('movies/', get_movie_list_template, name='movie_list_template'),
    path('seating/', seating, name='seating'),
    path('booking/', booking_history, name='booking_history'),
    ]
