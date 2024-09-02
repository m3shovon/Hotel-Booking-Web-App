from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import CustomUser, Location, Hotel, RoomType, Booking
from .serializers import CustomUserSerializer, LocationSerializer, HotelSerializer, RoomTypeSerializer, BookingSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_customer=True)
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
