from django.contrib.auth.models import AbstractUser
from django.db import models

from djchoices import ChoiceItem, DjangoChoices

from .managers import ReservationsSystemUserManager

class PaymentMethod(DjangoChoices):
    CASH = ChoiceItem('Cash')
    CREDIT = ChoiceItem('Credit')
    CHECK = ChoiceItem('Check')

class RegisteredUser(AbstractUser):
    username = None
    email = models.EmailField(unique = True)
    mailing_address = models.TextField()
    billing_address = models.TextField()
    diner_no = models.IntegerField(null = True)
    payment_method = models.CharField(max_length = 20, choices = PaymentMethod.choices)
    earned_points = models.IntegerField(default = 0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ReservationsSystemUserManager()

    def __str__(self):
      return self.email

