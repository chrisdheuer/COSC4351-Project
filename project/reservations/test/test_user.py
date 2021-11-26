from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.exceptions import ValidationError

class UserModelTest(TestCase):

    def setUp(self):
        self.User = get_user_model()
        
    def create_a_user(self, first_name = 'John', last_name = 'Smith', email = 'test123@example.com', password = 'pass', mailing_address = '123 N Avenue', billing_address = '123 N Avenue'):
        return self.User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            mailing_address = mailing_address,
            billing_address = billing_address,
        )

    def test_canary(self):
        self.assertTrue(True)

    def test_creating_a_user(self):
        user = self.create_a_user()
        
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        self.assertEqual(1, self.User.objects.count())
        
    def test_user_password_is_encrypted_upon_creation(self):
        user = self.create_a_user()
        
        self.assertNotEqual(user.password, 'pass')
    