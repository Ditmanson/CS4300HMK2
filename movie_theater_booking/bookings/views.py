from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'bookings/base.html')

def get_movie_list_template(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seating(request):
    seats = Seat.objects.all()
    return render(request, 'bookings/seat_booking.html', {'seats': seats})

def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})



@api_view(['GET'])
def getTestData(request):
    data = {
        'message': 'Hello World',
        'more_message': 'This is a test message'
    }
    return Response(data)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view(['GET'])
def movieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movieDetail(request, pk):
    movies = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movies, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def movieCreate(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def movieUpdate(request, pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(instance=movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def movieDelete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return Response('Movie deleted successfully')

@api_view(['DELETE'])
def seatDelete(request, pk):
    try:
        seat = Seat.objects.get(id=pk)
        seat.delete()
        return Response({'message': 'Seat deleted successfully'}, status=204)
    except Seat.DoesNotExist:
        return Response({'error': 'Seat not found'}, status=404)
