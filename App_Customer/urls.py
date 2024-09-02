from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, LocationViewSet, HotelViewSet, RoomTypeViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'roomtypes', RoomTypeViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
