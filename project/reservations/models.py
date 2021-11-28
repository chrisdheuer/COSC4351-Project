from django.core.exceptions import ValidationError
from django.db.models.deletion import SET_NULL
from django.db.models.fields import AutoField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from djchoices import ChoiceItem, DjangoChoices

from .managers import ReservationSystemUserManager

import random

class PaymentMethod(DjangoChoices):
    CASH = ChoiceItem('Cash')
    CREDIT = ChoiceItem('Credit')
    CHECK = ChoiceItem('Check')

class RegisteredUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique = True)
    phone_no = models.CharField(max_length = 20)
    mailing_address = models.CharField(max_length = 60)
    billing_address = models.CharField(max_length = 60)
    diner_no = models.IntegerField(null = True)
    payment_method = models.CharField(max_length = 20, choices = PaymentMethod.choices)
    earned_points = models.IntegerField(default = 0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ReservationSystemUserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.diner_no = random.randint(1,10)
        
        super().save(*args, **kwargs)

class RestaurantTable(models.Model):
    id = models.IntegerField(primary_key = True)
    capacity = models.IntegerField()
    is_reserved = models.BooleanField(default = False)
    reservation = models.ForeignKey('Reservation', on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f'Table #{self.id} with capacity {self.capacity}'

    def save(self, *args, **kwargs):
        if self.capacity not in (2, 4, 6, 8):
            raise ValidationError(
                _('Invalid field: %(value)s! Make sure table capacity is 2, 4, 6, or 8'),
                code = 'invalid',
                params = {'value': self.capacity}
            )
        
        super().save(*args, **kwargs)
        
class Reservation(models.Model):
    registered_user = models.ForeignKey(RegisteredUser, on_delete = SET_NULL, null = True)
    first_name = models.CharField(max_length = 20, blank = True)
    last_name = models.CharField(max_length = 20, blank = True)
    email_address = models.EmailField(blank = True)
    phone_number = models.CharField(max_length = 20, blank = True)
    number_of_guests = models.IntegerField()
    reservation_time = models.DateTimeField()
    
    def __str__(self):
        name = (self.registered_user.first_name, self.registered_user.last_name) if self.registered_user else (self.first_name, self.last_name)
        
        return f'Reservation for {name[0]}  {name[1]} with {self.number_of_guests} guests at {self.reservation_time}'
    