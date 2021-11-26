from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import UserRegistrationForm

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
