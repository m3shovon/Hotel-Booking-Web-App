from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotel, Booking, Room
from .forms import BookingForm, FilterForm
from django.contrib.auth.decorators import login_required


# List hotels with filters
def hotel_list(request):
    hotels = Hotel.objects.all()
    filter_form = FilterForm(request.GET)
    
    if filter_form.is_valid():
        location = filter_form.cleaned_data.get('location')
        rating = filter_form.cleaned_data.get('rating')
        amenities = filter_form.cleaned_data.get('amenities')
        
        if location:
            hotels = hotels.filter(location__icontains=location)
        if rating:
            hotels = hotels.filter(rating__gte=rating)
        if amenities:
            for amenity in amenities:
                hotels = hotels.filter(amenities=amenity)

    return render(request, 'hotel_list.html', {'hotels': hotels, 'filter_form': filter_form})

# Hotel detail view
def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    room_types = Room.objects.filter(hotel=hotel)
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'room_types': room_types})

# Booking view
@login_required
def book_hotel(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            return redirect('payment')  # Assuming a separate payment view
    else:
        form = BookingForm()

    return render(request, 'book_hotel.html', {'form': form, 'room': room})

# Payment view placeholder
@login_required
def payment(request):
    # Here you would implement your payment logic
    return render(request, 'payment.html')

