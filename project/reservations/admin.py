from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import RegisteredUser

class ReservationSystemUserAdmin(UserAdmin):
    """
    Form for creating superuser on Admin site
    """
    add_form = ReservationSystemAdminCreationForm
    form = ReservationSystemAdminChangeForm
    model = RegisteredUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(RegisteredUser, ReservationSystemUserAdmin)
