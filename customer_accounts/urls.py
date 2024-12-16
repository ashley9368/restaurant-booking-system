from django.urls import path
from . import views

urlpatterns = [
    path("accounts", views.customer_accounts, name="customer_accounts"), 
]