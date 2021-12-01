from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import RegisteredUser, RestaurantTable, Reservation

@admin.register(RegisteredUser)
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

@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    model = RestaurantTable
    
    list_diplay = ('capacity')
    fields = ['id', 'capacity']
    search_fields = ['capacity']
    list_filter = ['capacity']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    
    list_display = ( 'first_name', 'last_name', 'email_address', 'phone_number', 'number_of_guests', 'reservation_time')
    fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'number_of_guests', 'reservation_time']