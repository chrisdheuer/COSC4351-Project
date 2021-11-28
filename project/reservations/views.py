from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView
from django.contrib import messages

from .forms import GuestReservationForm, UserRegistrationForm, GuestReservationForm, RegisteredReservationForm
from .models import RegisteredUser, Reservation, RestaurantTable

def index(request):
    selection = range(1,13)
    
    return render(request, 'reservations/index.html', {'selection':selection})

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
    
def available_tables(request):
    tables = RestaurantTable.objects.filter(
        is_reserved = False,
        capacity__gte = request.POST['number_of_guests']
    )
            
    if not tables:
        cap = 0
        ids = []
        
        for i in RestaurantTable.objects.all():
            if cap + i.capacity <= int(request.POST['number_of_guests']):
                cap += i.capacity
                ids.append(i.id)
        
        tables = RestaurantTable.objects.filter(id__in = ids)
    
    return render(request, 'reservations/table_list.html', {'tables': tables})
        

def reserve_table(request):
    
    print(request.user.is_authenticated, request.method, request.GET)
    
    if request.method == 'POST':
        number_of_guests = request.GET['number_of_guests']
        
        form = RegisteredReservationForm(request.POST) if request.user.is_authenticated else GuestReservationForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                request.user.reservation_set.create(
                    first_name = request.user.first_name,
                    last_name = request.user.last_name,
                    email_address = request.user.email,
                    phone_number = request.user.phone_no,
                    number_of_guests = number_of_guests,
                    reservation_time = form.cleaned_data('reservation_time')
                )
                
                return redirect('profile')
            else:
                form.save()
                
                return redirect('index')
    else:
        form = GuestReservationForm()
    
    return render(request, 'reservations/reserve_table.html', {'form':form})