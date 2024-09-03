from django.forms import ModelForm
from App_Auth.models import User, CustomerProfile
from django.contrib.auth.forms import UserCreationForm

# form 
class ProfileForm(ModelForm):
    class Meta:
        model = CustomerProfile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')