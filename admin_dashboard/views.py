from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard_home(request):
    return HttpResponse("This would be your admin dashboard")
