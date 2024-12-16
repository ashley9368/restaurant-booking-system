from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customer_accounts(request):
    return HttpResponse("Customer accounts page!")