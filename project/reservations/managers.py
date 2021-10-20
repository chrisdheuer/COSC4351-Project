from django.contrib.auth.base_user import BaseUserManager

class ReservationsSystemUserManager(BaseUserManager):
    """
    Custom user manager for Users and Admins that use emails as the primary key rather than the username
    """
    
    def create_user(self, email, password, **extra_fields):
        """
        Creates a user with the given email and password
        """
        email = self.normalize_email(email)

        user = self.model(email = email, password = password, **extra_fields)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a superuser (Admin) with the given email and password
        """
        extra_fields.set_default('is_active', True)
        extra_fields.set_default('is_staff', True)
        extra_fields.set_default('is_superuser', True)
    
    