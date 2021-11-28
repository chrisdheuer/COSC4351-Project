from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name = 'index'),
  path('register/', views.register, name = 'register'),
  path('login/', views.login_request, name = 'login'),
  path('logout/', views.logout_request, name = 'logout'),
  path('profile/<int:pk>', views.user_profile.as_view(), name = 'profile'),
  path('tables/', views.available_tables, name = 'tables'),
  path('reserve/', views.reserve_table, name = 'reserve'),
]