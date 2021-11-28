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
    
class ReservationForm(ModelForm):
  class Meta:
    model = Reservation
    fields = '__all__'
  