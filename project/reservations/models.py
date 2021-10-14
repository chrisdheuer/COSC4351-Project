from django import forms
from django.db import models
from django.forms.widgets import PasswordInput

from djchoices import ChoiceItem, DjangoChoices

class PaymentMethod(DjangoChoices):
    CASH = ChoiceItem('Cash')
    CREDIT = ChoiceItem('Credit')
    CHECK = ChoiceItem('Check')

class RegisteredUser(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(primary_key = True)
    password = forms.CharField(widget = PasswordInput)
    mailing_address = models.TextField()
    billing_address = models.TextField()
    diner_no = models.IntegerField(null = True)
    payment_method = models.CharField(max_length = 20, choices = PaymentMethod.choices)
