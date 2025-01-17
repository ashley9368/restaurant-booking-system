"""
URL configuration for restaurant_booking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking_system import views as booking_views
from booking_system.views_manage import manage_booking
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('accounts/', include('customer_accounts.urls')),
    path('make/', booking_views.make_booking, name='make_booking'),
    path('manage/', manage_booking, name='manage_booking'),
    path('menu/', views.menu, name='menu'),
    path('admin/', admin.site.urls),
]
