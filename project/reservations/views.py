from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist

from .models import RegisteredUser
from .forms import UserRegistrationForm


def index(request):
  user = True if request.user.is_authenticated else False
  
  return render(request, 'reservations/index.html', {'user': user})

def signout(request):
  logout(request)
  
  return redirect('/')

def signup(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
    
    email, password = request.POST['email'], request.POST['password']
    user = authenticate(request, email = email, password = password)
    login(request, user)
    
    return redirect('/')
  else:
    form = UserRegistrationForm()
    
  return render(request, 'registration/signup.html', {'form': form})
  