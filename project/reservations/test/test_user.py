from django.contrib.auth import get_user_model
from django.test import TestCase
from reservations.models import *


class UserModelTest(TestCase):

    def setUp(self):
        self.User = get_user_model()

    def test_canary(self):
        self.assertTrue(True)

    def test_creating_a_user(self):
        user = self.User.objects.create_user(
            first_name = 'John',
            last_name = 'Smith',
            email = 'test123@example.com',
            password = 'pass',
            mailing_address = '123 N Avenue',
            billing_address = '456 S Street',
            diner_no = 1,
            payment_method = PaymentMethod.CASH,
        )
        user.save()

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        self.assertEqual(1, self.User.objects.count())

