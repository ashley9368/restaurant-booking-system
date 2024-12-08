from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),             # Homepage
    path('booking/', views.booking_page, name='booking'),  # Booking page
    path('menu/', views.menu_page, name='menu'),           # Menu page
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard
]