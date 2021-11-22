from django.shortcuts import render
from .models import RegisteredUser

def index(request, user_id = None):
  user = RegisteredUser.objects.get(id = user_id) if user_id else None
  
  return render(request, 'reservations/index.html', {'user': user})
  