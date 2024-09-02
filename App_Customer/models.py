from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=False)

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    star_rating = models.IntegerField()
    amenities = models.CharField(max_length=255)
    price_range = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.hotel.name}"

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.IntegerField()
    additional_services = models.CharField(max_length=255, null=True, blank=True)
    promo_code = models.CharField(max_length=50, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.user.username} at {self.hotel.name}"
