from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from App_Auth.models import CustomerProfile

# class User(AbstractUser):
#     is_customer = models.BooleanField(default=True)

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hotels')
    description = models.TextField()
    amenities = models.ManyToManyField(Amenity)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='hotels/')
    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=100)  # e.g., Single, Double, Suite, etc.
    number_of_beds = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"

class Booking(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests_adult = models.IntegerField()
    guests_children = models.IntegerField()
    total_guest = models.IntegerField()
    is_confirmed = models.BooleanField(default=False)
    booking_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Booking {self.booking.id}"
