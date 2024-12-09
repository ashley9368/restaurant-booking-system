from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def make_booking(request):
    return HttpResponse("Make a Booking!")