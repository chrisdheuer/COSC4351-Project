from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView
from django.contrib import messages

from .forms import UserRegistrationForm, ReservationForm
from .models import RegisteredUser, Reservation

def index(request):
    return render(request, 'reservations/index.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email = email, password = password)
            
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid email address or password.")
        else:
            messages.error(request, "Invalid email address or password.")
            
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
    
def logout_request(request):
    logout(request)
    
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

class user_profile(DetailView):
    model = RegisteredUser
    template_name = 'accounts/profile.html'

def search_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone_number = form.cleaned_data.get('phone_number')
            email_address = form.cleaned_data.get('email_address')
            number_of_guests = form.cleaned_data.get('number_of_guests')
            reservation_time = form.cleaned_data.get('reservation_time')
            
            reservation = Reservation(first_name = first_name, last_name = last_name, phone_number = phone_number, email_address = email_address, number_of_guests = number_of_guests, reservation_time = reservation_time)
            reservation.save()
        
    form = ReservationForm()
    
    return render(request, 'reservations/search_table.html', {'form':form})