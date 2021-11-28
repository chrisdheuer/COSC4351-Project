from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name = 'index'),
  path('register/', views.register, name = 'register'),
  path('login/', views.login_request, name = 'login'),
  path('logout/', views.logout_request, name = 'logout'),
  path('profile/<int:pk>', views.user_profile.as_view(), name = 'profile'),
  path('make_reservation', views.make_reservation, name = 'make_reservation'),
]