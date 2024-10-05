from django import forms
from .models import Booking, Amenity

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'guests_adult', 'guests_children', 'check_in_date', 'check_out_date']

class FilterForm(forms.Form):
    location = forms.CharField(required=False)
    rating = forms.DecimalField(required=False, max_digits=3, decimal_places=2)
    amenities = forms.ModelMultipleChoiceField(queryset=Amenity.objects.all(), required=False)