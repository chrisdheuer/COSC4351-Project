from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class ReservationSystemUserManager(BaseUserManager):
    """
    Custom user manager for Users and Admins that use emails as the primary key rather than the username
    """
    
    def create_user(self, email, password, **extra_fields):
        """
        Creates a user with the given email and password
        """
        email = self.normalize_email(email)

        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a superuser (Admin) with the given email and password
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff') or not extra_fields.get('is_superuser'):
            raise ValueError(_('Error creating superuser! Ensure is_staff=True and is_superuser=True'))

        return self.create_user(email, password, **extra_fields)
    
    
