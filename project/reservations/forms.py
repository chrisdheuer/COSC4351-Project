from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import RegisteredUser

class ReservationSystemAdminCreationForm(UserCreationForm):

  class Meta:
    model = RegisteredUser
    fields = ('email',)

class ReservationSystemAdminChangeForm(UserChangeForm):

  class Meta:
    model = RegisteredUser
    fields = ('email',)