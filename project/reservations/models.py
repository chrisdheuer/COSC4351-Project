from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from djchoices import ChoiceItem, DjangoChoices

from .managers import ReservationSystemUserManager

class PaymentMethod(DjangoChoices):
    CASH = ChoiceItem('Cash')
    CREDIT = ChoiceItem('Credit')
    CHECK = ChoiceItem('Check')

class RegisteredUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique = True)
    mailing_address = models.TextField()
    billing_address = models.TextField()
    diner_no = models.IntegerField(null = True)
    payment_method = models.CharField(max_length = 20, choices = PaymentMethod.choices)
    earned_points = models.IntegerField(default = 0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ReservationSystemUserManager()

    def __str__(self):
      return self.email

class RestaurantTable(models.Model):
    capacity = models.IntegerField()

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self.capacity not in (2, 4, 6, 8):
            raise ValidationError(
                _('Invalid field: %(value)s! Make sure table capacity is 2, 4, 6, or 8'),
                code = 'invalid',
                params = {'value': self.capacity}
            )
        
        super().self.save(*args, **kwargs)