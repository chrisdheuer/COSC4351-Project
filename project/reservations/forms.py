from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import RegisteredUser, Reservation

class ReservationSystemAdminCreationForm(UserCreationForm):

    class Meta:
        model = RegisteredUser
        fields = ('email',)

class ReservationSystemAdminChangeForm(UserChangeForm):

    class Meta:
        model = RegisteredUser
        fields = ('email',)
    
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
  
    class Meta:
        model = RegisteredUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'mailing_address', 'billing_address', 'payment_method')
    
class GuestReservationForm(ModelForm):
    reservation_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    ) 
  
    class Meta:
        model = Reservation
        fields = ('first_name', 'last_name', 'email_address', 'phone_number', 'reservation_time')
    
class RegisteredReservationForm(GuestReservationForm):
  
    class Meta:
        model = Reservation
        fields = ('reservation_time',)

  