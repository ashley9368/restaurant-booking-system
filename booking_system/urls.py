from django.urls import path
from . import views

urlpatterns = [
    path("make/", views.make_booking, name="make_booking"), 
]